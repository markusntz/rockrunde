import os

import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"), client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
    )
)


def generate_url(urn: str) -> str:
    track_id = urn.split(":")[-1]
    return f"https://open.spotify.com/track/{track_id}"


def get_track_info(track_id: str) -> dict:
    urn = f"spotify:track:{track_id}"
    track = sp.track(urn)

    track_name = track.get("name")

    track_artist = track.get("artists")
    track_artist_names = [e.get("name") for e in track_artist]
    track_artist_names_fin = " & ".join(track_artist_names)

    track_album = track.get("album")
    track_album_release_date = track_album.get("release_date")
    track_album_release_date

    track_info = {}
    track_info["track"] = track_name
    track_info["artist"] = track_artist_names_fin
    track_info["release_year"] = track_album_release_date[0:4]
    track_info["url"] = generate_url(urn)

    return track_info


def get_tracks_from_playlist(playlist_id: str) -> list:
    pl_id = f"spotify:playlist:{playlist_id}"
    offset = 0

    response = sp.playlist_items(
        pl_id, offset=offset, fields="items.track.id,total", additional_types=["track"], limit=100
    )

    track_ids = [e.get("track").get("id") for e in response["items"]]

    return track_ids


def export_tracks_xlsx(res) -> None:
    df = pd.DataFrame(res)
    df.sort_values("release_year").to_excel("overview.xlsx", index=False)
