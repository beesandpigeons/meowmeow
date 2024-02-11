import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import datetime

client_id = '606fd71f49ad436692ba263a937d63ff'
client_secret = 'b8eb6d4186684c39ab35e10b731d719d'
scope = 'user-read-recently-played'
credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret,)
sp = spotipy.Spotify(auth_manager=credentials_manager)

year_start = datetime.datetime(datetime.datetime.now().year, 1, 1)
year_start_timestamp = int(year_start.timestamp()) * 1000

all_results = []
results = sp.current_user_recently_played(limit=50, after=year_start_timestamp)
while results(next):
    results = sp.next(results)
    all_results.extend(results['items'])

print(all_results)