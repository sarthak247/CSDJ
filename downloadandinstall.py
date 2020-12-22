from youtube_search import YoutubeSearch
import json
import pafy
import os
import subprocess
import shutil

csgodir = ""


def search(name):
    # To get all the video links
    results = YoutubeSearch(name, max_results=5).to_json()
    best = json.loads(results)  # The top video
    # Complete Download Link
    download_link = f'https://youtube.com{best["videos"][0]["url_suffix"]}'
    print(download_link)  # Printing for debuggind
    return download_link  # Returning it to the download functon


def download(name):
    link = search(name)  # Searching the song on YT
    song = pafy.new(link)  # Finding the song using PAFY
    dl = song.getbestaudio()  # Getting the best song and audio quality
    title = song.title
    path = f"{os.getcwd()}/{name}.webm"
    # Downloading it with output to console
    dl.download(quiet=False, filepath=path)
    #os.rename(title, name)
    ffmpeg_cmd = "ffmpeg -i " + "'" + name + '.webm' + "'" + \
        " -acodec pcm_s16le -ar 22050 -ac 1 -fflags +bitexact -flags:v +bitexact -flags:a +bitexact  voice_input.wav -y"
    # Call to ffmpeg to run the conversion
    subprocess.call(ffmpeg_cmd, shell=True)


def movetodir():
    try:
        cfg = open('csdj.cfg')
        dest = str(cfg.read())
        shutil.copy(f'{os.getcwd()}/voice_input.wav', f"{dest}/")
        print("Copied!")
    except FileNotFoundError:  # File does not exist!
        filedir = input("Enter your CSGO install dir : ")
        cfg = open('csdj.cfg', 'w')
        cfg.write(filedir)
        movetodir()
    finally:
        cfg.close()


download(input("Enter song you want! : "))
movetodir()
