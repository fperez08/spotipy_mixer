# Spotipy Playlist mix

This simple script shuffles the tracks in a Spotify playlist randomly. I created this because when I have a playlist with a lot of tracks and I play them with the aleatory option Spotify always reproduces the same songs in a different order but not all the tracks, for example, if you have 100 tracks in a playlist and you reproduce 25 songs, every time you get the same 25 songs in a different order.
Now after running the script the tracks are shuffled and I can reproduce them from top to bottom.

## Requirements

Before running the script install the following:

- Python 3.9 or higher
- [Poetry](https://python-poetry.org/docs/#installation)

The script uses the [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/) library to interact with the Spotify Web API, before running the script for the fist time create a new application in [My Dashboard](https://developer.spotify.com/dashboard), then get the client id, client secret and redirect URI here is a [video](https://www.youtube.com/watch?v=3RGm4jALukM) about how to do it.


## Installation

Clone this repo and at the root folder execute:
```
poetry install
```
## Usage
1. Creates a .env file at the root folder of the project and set the following variables:
```
SPOTIPY_CLIENT_ID=
SPOTIPY_CLIENT_SECRET=
SPOTIPY_REDIRECT_URI=
```
2. Open your terminal and run the command:
```
python3 mix.py --name "{playlist_name}"
```
Note.- When you run the script for the first time a browser is going to open so you can give access to your Spotify application, then you are going to be redirected to the URI you set previously, copy the whole URL and pasted it into the terminal, after that the token is going to be saved in a .cache file to be reused for the next's executions.