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

def get_album_and_image(artist_name, album_name):
    # Convert both strings to lowercase and strip whitespaces
    catalogue = get_artist_catalogue(artist_name)
    
    artist_name = artist_name.lower().strip()
    album_name = album_name.lower().strip()
    
    name = None
    middle_image_url = None
    
    for i in catalogue:
        # Convert album name from the catalogue to lowercase and strip whitespaces
        current_album_name = i['name'].lower().replace(" ", "")
        # Check if the specified album name is a case-insensitive substring of the current album name
        if album_name in current_album_name:
            name = i['name']
            images = i.get('images', [])  # Retrieve the 'images' list, default to an empty list if it doesn't exist

            # Check if there are images in the list
            if images:
                # Find the middle-sized image (assuming the list is sorted by size)
                middle_index = len(images) // 2
                middle_image_url = images[middle_index].get('url')

            break  # Break out of the loop once a match is found

    if name is None and middle_image_url is None:
        print(f"There is no matching album for '{album_name}' by {artist_name}")

    return name, middle_image_url