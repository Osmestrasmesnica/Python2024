import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
from dotenv import load_dotenv
import os

#Applay Secrets from .env file
load_dotenv()

YOUR_APP_CLIENT_ID = os.getenv("YOUR_APP_CLIENT_ID")
YOUR_APP_CLIENT_SECRET = os.getenv("YOUR_APP_CLIENT_SECRET")
YOUR_APP_REDIRECT_URI = os.getenv("YOUR_APP_REDIRECT_URI")
YOUR_SPOTIFY_DISPLAY_NAME = os.getenv("YOUR_SPOTIFY_DISPLAY_NAME")

# Authenticate with Spotify API
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=YOUR_APP_CLIENT_ID,
        client_secret=YOUR_APP_CLIENT_SECRET,
        redirect_uri=YOUR_APP_REDIRECT_URI,
        cache_path="Dan46_WebScraping_Spotify/token.txt",
        username=YOUR_SPOTIFY_DISPLAY_NAME,
        show_dialog=True,
        scope="playlist-modify-public playlist-modify-private"
    )
)

# Get current user ID
user_id = sp.current_user()["id"]
print("Current User ID:", user_id)

# Input year from the user
datum = input("Which year do you want to travel to? Type date in this format YYYY-MM-DD:\n")

# Extract year from the input date
year = datum.split("-")[0]
print("Year:", year)

# Fetch Billboard Hot 100 page for the given date
URL = "https://www.billboard.com/charts/hot-100/"
response = requests.get(URL + datum)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract song names from the webpage
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print("Song Names:", song_names)

# Search for each song on Spotify and collect their URIs
uri_songs = []

for song in song_names:
    try:
        search_result = sp.search(
            q=f"track:{song} year:{year}",
            limit=1,
            type="track",
            market="AT"
        )
        uri = search_result["tracks"]["items"][-1]["uri"]
        uri_songs.append(uri)
        pprint.pprint(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create a new playlist on Spotify
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{datum} Billboard 100",
    public=True,
    description="Playlist created from Python using Billboard Top 100. Made by WLQ."
)

# Get the playlist ID of the newly created playlist
playlist_id = playlist["id"]
print("Playlist ID:", playlist_id)

# Add each song to the newly created playlist
for song_uri in uri_songs:
    sp.playlist_add_items(
        playlist_id=playlist_id,
        items=[song_uri],
        position=None
    )
    print("Added to playlist")

print("All songs from Billboard Hot 100 have been added to the Spotify playlist. Made by WLQ")