import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret= os.getenv('CLIENT_SECRET')

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_artist_uri(artist_name):
    results = sp.search(q=f'artist:{artist_name}', type='artist')
    artists = results['artists']['items']
    if artists:
        # Taking the first artist found in the search results
        artist_uri = artists[0]['uri']
        return artist_uri
    else:
        return None

def get_artist_catalogue(artist_name):
    artist_id = get_artist_uri(artist_name)
    results = sp.artist_albums(artist_id, album_type='album')
    items = results['items']
    return items

def get_artist_albums(artist_name):
    catalogue = get_artist_catalogue(artist_name)
    albums = [catalogue['name'] for catalogue in catalogue if 'name' in catalogue]
    return albums

