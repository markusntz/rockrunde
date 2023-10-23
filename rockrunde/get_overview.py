from tqdm import tqdm

from rockrunde.spotify import get_tracks_from_playlist, get_track_info, export_tracks_xlsx

tracks_60 = get_tracks_from_playlist("1LYRf9mxmB27XdVXcmVNq1")
tracks_70 = get_tracks_from_playlist("0mBAzfRc1YXdM2dFp04BKS")
tracks_80 = get_tracks_from_playlist("7rzublEWshabpOQGZLs7U2")
tracks_90 = get_tracks_from_playlist("3CjPiMTeS9xh4RUW2oJZ1k")
tracks_00 = get_tracks_from_playlist("0hwYMqYC4tKJU0iwvmCpau")
tracks_10 = get_tracks_from_playlist("1PtH4FoWGCuzbZmZsIh9Ev")

all_tracks = [tracks_60, tracks_70, tracks_80, tracks_90, tracks_00, tracks_10]

res = []
for tracks in tqdm(all_tracks):
    for track in tracks:
        ti = get_track_info(track)
        res.append(ti)

export_tracks_xlsx(res)
