from flask import Flask, render_template
from get_functions import *
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret= os.getenv('CLIENT_SECRET')

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

app = Flask(__name__)

# Assuming you have the get_album_and_middle_image function defined here

# Example route to display album name and middle-sized image
@app.route('/album/<artist>/<album>')
def show_album(artist, album):
    album_name, middle_image_url = get_album_and_image(artist, album)
    if album_name and middle_image_url:
        return render_template('index.html', album_name=album_name, image_url=middle_image_url)
    else:
        return "Album not found."


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
