from dotenv import load_dotenv
import os 
import base64
from requests import post, get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name exists...")
        return None

    return json_result[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

token = get_token()
user_input = input("Enter the artist that you would like to see the top 10 songs for: ")

result = search_for_artist(token, user_input)



if result:
    artist_id = result["id"]
    songs = get_songs_by_artist(token, artist_id)
    for idx, song in enumerate(songs):
        print(f"{idx + 1}. {song['name']}")


import matplotlib.pyplot as plt
import numpy as np

def plot_top_tracks_stacked(tracks):
    track_names = [track['name'] for track in tracks]

    fig, ax = plt.subplots(figsize=(10, 8))
    
    y_positions = np.arange(len(track_names))
    ax.barh(y_positions, np.ones_like(y_positions), color='skyblue', edgecolor='black')
    ax.set_yticks(y_positions)
    ax.invert_yaxis()  # Invert the y-axis to have the top track at the top
    ax.set_xticks([])  # Hide x-axis ticks
    ax.set_yticks([])  # Hide x-axis ticks
    ax.set_ylabel('Rank')
    ax.set_title('Top Tracks by Rank')

    for i, track in enumerate(track_names):
        ax.text(0, i, f"{i + 1}. {track}", ha='left', va='center', color='black', fontsize=10, weight='bold')

    plt.tight_layout()
    plt.show()

# Assume we have already fetched the token and artist ID
token = get_token()
result = search_for_artist(token, user_input)
if result:
    artist_id = result["id"]
    songs = get_songs_by_artist(token, artist_id)
    plot_top_tracks_stacked(songs)
