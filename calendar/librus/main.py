import pytz
import librus
from librus import LibrusSession
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import json

def __init__(self, login, password):
    self.login = login
    self.password = password

class Librus(LibrusSession):
    exams = []
    ignored_subjects = ['Język francuski', 'Religia']  # Add the subjects you want to skip
    
    def __init__(self, login, password):
        self.login(login, password)
        for exam in self.list_exams():
            if exam.subject not in self.ignored_subjects:  # Only add the exam if the subject is not in the ignored_subjects list
                self.exams.append(
                    self.generate_body(
                        exam.date,
                        exam.category,
                        exam.subject,
                        exam.specification,
                        exam.lesson,
                    )
                )
    def generate_body(self, date, category, subject, specification, lesson):
        date_object = datetime.strptime(date, "%Y-%m-%d")
        date_object = pytz.timezone('Europe/Warsaw').localize(date_object) # localize the datetime object
        start_date = date_object.isoformat() 
        end_date = (date_object + timedelta(hours=1)).isoformat() 
        return {
            'summary': f'{category}: {subject}',
            'description': f'Specification: {specification}, Lesson: {lesson}',
            'start': {
                'dateTime': start_date,
                'timeZone': 'Europe/Warsaw',
            },
            'end': {
                'dateTime': end_date,
                'timeZone': 'Europe/Warsaw',
            }
        }
    
class Calendar():
    def __init__(self):
        self.SCOPE = 'https://www.googleapis.com/auth/calendar'
        self.store = file.Storage('token.json')
        self.creds = self.store.get()
        if not self.creds or self.creds.invalid:
            self.flow = client.flow_from_clientsecrets(
                'credentials.json', self.SCOPE)
            self.creds = tools.run_flow(self.flow, self.store)
        self.service = build(
            'calendar',
            'v3',
            http=self.creds.authorize(
                Http()))

    def add_exam(self, body):
        # Get list of events for the time range of the exam
        events_result = self.service.events().list(calendarId='primary', 
                                                timeMin=body['start']['dateTime'], 
                                                timeMax=body['end']['dateTime']).execute()
        events = events_result.get('items', [])

        if not events:  # If no existing event is found, add the exam
            self.service.events().insert(calendarId='primary', body=body).execute()


if __name__ == "__main__":
    l = Librus(login='9732283u', password='Lena2006')
    cal = Calendar()
    for exam in l.exams:
        if not cal.service.events().list(calendarId='primary',
                                         timeMin=exam['start']['dateTime'], timeMax=exam['end']['dateTime']).execute()['items']:
            cal.add_exam(exam)