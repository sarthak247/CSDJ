from youtube_search import YoutubeSearch
import json
import pafy
import os, subprocess

def search(name):
    results = YoutubeSearch(name, max_results=5).to_json() # To get all the video links
    best = json.loads(results)   #The top video
    download_link = f'https://youtube.com{best["videos"][0]["url_suffix"]}' #Complete Download Link
    print(download_link)    #Printing for debuggind
    return download_link    #Returning it to the download functon

def download(name):
    link = search(name)     #Searching the song on YT
    song = pafy.new(link)   #Finding the song using PAFY
    dl = song.getbestaudio() #Getting the best song and audio quality
    title = song.title
    path = f"{os.getcwd()}/{name}.webm"
    dl.download(quiet=False, filepath = path)    #Downloading it with output to console
    #os.rename(title, name)
    ffmpeg_cmd = "ffmpeg -i "+ "'" + name + '.webm' + "'" + " -acodec pcm_s16le -ar 22050 -ac 1 -flags +bitexact voice_input.wav -y"


    subprocess.call(ffmpeg_cmd,shell=True) #Call to ffmpeg to run the conversion
    print("Here!")

download("EZ4ENCE")