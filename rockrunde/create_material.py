import pandas as pd

from rockrunde.qr import generate_qr_code, generate_text_img

df_all_tracks = pd.read_excel("overview.xlsx", dtype=str)

for index, row in df_all_tracks.iterrows():
    generate_qr_code(row["url"], f"qr_{index}")
    generate_text_img(row["artist"], row["release_year"], row["track"], f"info_{index}")
