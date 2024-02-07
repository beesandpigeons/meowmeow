import requests
import json
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from bs4 import BeautifulSoup

class Calendar():
    def __init__(self):
        self.SCOPES = 'https://www.googleapis.com/auth/calendar'
        self.store = file.Storage('credentials.json')
        self.creds = self.store.get()
        if not self.creds or self.creds.invalid:
            self.creds = tools.run_flow(self.flow, self.store)
        self.service = build('calendar', 'v3', http=self.creds.authorize(Http()))
    
    def add(self, body):
        events_result = self.service.events().list(calendarId='primary', 
                                                timeMin=body['start']['dateTime'], 
                                                timeMax=body['end']['dateTime']).execute()
        events = events_result.get('items', [])
        if not events:
            self.service.events().insert(calendarId='primary', body=body).execute()

class Library():
    url = 'https://www.biblioteka.lodz.pl/wydarzenia/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for event in self.events:
            events = soup.find_all('div', class_='event')    
            if 'DKKQ' in title:
                date = event.find('time')['datetime']
                calendar = Calendar()
                calendar.add(title, date)    
    else:
        print('Failed to fetch the events page.')

