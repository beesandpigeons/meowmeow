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
        print(event.prettify())
        #title = event.find('h2', class_='title').text
        #if 'DKKQ' in title:          
else:
    print('Failed to fetch the events page.')