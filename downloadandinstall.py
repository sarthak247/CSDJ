
from youtube_search import YoutubeSearch
import json
import pafy
import os
import subprocess
import shutil
import platform


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
    if platform.system()=='Windows':
    	ffmpeg_cmd = f"{os.path.join(os.getcwd(),'ffmpegw.exe')} -i " + '"' + name + '.webm' + '"' + \
        	" -acodec pcm_s16le -ar 22050 -ac 1 -fflags +bitexact -flags:v +bitexact -flags:a +bitexact " + f'"{os.path.join(os.getcwd(),"voice_input.wav")}"' +  " -y"
    	print(ffmpeg_cmd)
    	subprocess.call(f"{ffmpeg_cmd}",shell=True)
    # Call to ffmpeg to run the conversion
    elif platform.system()=="Linux":
    	ffmpeg_cmd = "./ffmpeglinux -i " + "'" + name + '.webm' + "'" + \
        	" -acodec pcm_s16le -ar 22050 -ac 1 -fflags +bitexact -flags:v +bitexact -flags:a +bitexact  voice_input.wav -y"
    	subprocess.call(ffmpeg_cmd, shell=True)
    


def movetodir():
    try:
        cfg = open('csdir.cfg')
        dest = str(cfg.read())
        if platform.system()=='Windows':
            path = os.path.join(os.getcwd(),'voice_input.wav')
            shutil.copy(path, f"{dest}\\")
        elif platform.system()=="Linux":
            shutil.copy(f'{os.getcwd()}/voice_input.wav', f"{dest}/")
        print("Copied!")
        if os.path.exists(os.path.join(dest,'csgo','cfg','csdj.cfg'))==False:
           shutil.copy(f'{os.path.join(os.getcwd(),"csdj.cfg")}', f"{os.path.join(dest,'csgo','cfg')}")
        cfg.close()
    except FileNotFoundError:  # File does not exist!
        dest = input("Enter your CSGO install dir : ")
        cfg = open('csdir.cfg', 'w')
        cfg.write(dest)
        if platform.system()=='Windows':
            path = os.path.join(os.getcwd(),'voice_input.wav')
            shutil.copy(path, f"{dest}\\")
        elif platform.system()=="Linux":
            shutil.copy(f'{os.getcwd()}/voice_input.wav', f"{dest}/")
        if os.path.exists(os.path.join(dest,'csgo','cfg','csdj.cfg'))==False:
           shutil.copy(f'{os.path.join(os.getcwd(),"csdj.cfg")}', f"{os.path.join(dest,'csgo','cfg')}")
        print("Copied!")
        cfg.close()


download(input("Enter song you want! : "))
movetodir()

