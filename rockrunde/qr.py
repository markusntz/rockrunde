import segno

from PIL import Image, ImageFont, ImageDraw

from random import choice

import textwrap


def generate_qr_code(url: list, filename: str) -> None:
    qrcode = segno.make_qr(url)

    qrcode.save(f"png_qr/{filename}.png", scale=50, dark="white", light="black")


def generate_text_img(artist, year, song, filename):
    # size = (300, 300)
    size = (550, 550)
    W, H = size

    background_color_list = [(221, 97, 55), (227, 169, 96), (82, 148, 107), (79, 133, 154), (108, 182, 177)]
    background_color = choice(background_color_list)

    img = Image.new("RGB", size, background_color)
    draw = ImageDraw.Draw(img)
    fontpath = "Library/Fonts/TiltNeon-Regular-VariableFont_XROT,YROT.ttf"
    font_artist_song = ImageFont.truetype(fontpath, 55)
    font_year = ImageFont.truetype(fontpath, 200)

    # 2 zeilig
    lines = textwrap.wrap(artist, width=20)
    y_text = 6
    for line in lines:
        # width, height = font_artist_song.getsize(line)
        draw.text((W / 2, H / y_text), line, fill="#000", font=font_artist_song, anchor="mm")
        y_text = 3.8

    # lines = textwrap.wrap(artist, width=20)
    # # y_text = 10
    # y_text = 5 if len(lines) == 1 else 10

    # for i, line in enumerate(lines):
    #     # width, height = font_artist_song.getsize(line)
    #     draw.text((W/2, H/y_text), line, fill="#000", font=font_artist_song, anchor="mm")
    #     y_text = 5.2 if i == 0 else 3.5

    draw.text((W / 2, H / 1.9), year, fill="#000", font=font_year, anchor="mm")

    lines = textwrap.wrap(song, width=20)
    y_text = 1.3
    for i, line in enumerate(lines):
        # width, height = font_artist_song.getsize(line)
        draw.text((W / 2, H / y_text), line, fill="#000", font=font_artist_song, anchor="mm")
        y_text = 1.165 if i == 0 else 1.05

    # img.show()
    img.save(f"png_text/{filename}.png")


# generate_qr_code("hello", "qr_test")
# generate_qr_code("hello", "qr_test_2")
# generate_text_img("Markus Blues Band with other people", "2012", "Thunder in your pants", "text_img_test")
# generate_text_img("Nick Cave and another very long band name", "1999", "Meine Beine sind schwer, aber egal, ja wirklich", "text_img_test_2")
