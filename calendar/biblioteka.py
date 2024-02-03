import requests
import json
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from bs4 import BeautifulSoup

url = 'https://www.biblioteka.lodz.pl/wydarzenia/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    events = soup.find_all('div', class_='event')
    for event in events:
        title = event.find('h2', class_='title').text
        if 'DKKQ' in title:
            event = {
                'summary': title,
                'start': {
                    'dateTime': f'{meeting_date}T{start_time}:00',
                    'timeZone': 'Europe/Warsaw',
                },
                'end': {
                    'dateTime': f'{meeting_date}T{end_time}:00',
                    'timeZone': 'Europe/Warsaw',
                }
            }
else:
    print('Failed to fetch the events page.')