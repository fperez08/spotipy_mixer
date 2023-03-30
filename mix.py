import spotipy
import random
import argparse
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

scope = "user-library-read,playlist-modify-private,playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
my_parser = argparse.ArgumentParser(allow_abbrev=False)
my_parser.add_argument("--name", action="store", type=str, required=True)
target_playlist_name = my_parser.parse_args().name

results = sp.current_user_playlists()
found_playlist = [
    playlist
    for playlist in results.get("items", None)
    if target_playlist_name == playlist.get("name", None)
]

if not found_playlist:
    print("Playlist not found")

playlist_uri = found_playlist[0].get("id", None)
playlist_name = found_playlist[0].get("name", None)
total_tracks = found_playlist[0]["tracks"]["total"]

random_list = [random.randint(0, total_tracks) for _ in range(total_tracks)]
for number in random_list:
    print(
        f"Moving the first track of {playlist_name} playlist before the {number} position"
    )
    sp.playlist_reorder_items(
        playlist_id=playlist_uri,
        range_start=0,
        range_length=1,
        insert_before=number,
    )
