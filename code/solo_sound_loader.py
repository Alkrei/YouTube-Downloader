from pytubefix import YouTube
from pytubefix.exceptions import RegexMatchError
from pytubefix.innertube import _default_clients
import os

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

def solo_sound_loader():
    path = str(input("Path :"))
    if os.path.exists(path):
        try:
            url = str(input("Youtube video url :"))
            video = YouTube(url)
            print(f"{video.title}")
            print(" ")

            stream = video.streams.filter(progressive=True).get_highest_resolution()
            file = stream.download(output_path="../sound")
            file_name = os.path.splitext(os.path.basename(file))[0]

            command = f"ffmpeg -i '../sound/{file_name}.mp4' '{path}/{file_name}.mp3'"
            os.system(command)
            os.remove(f"../sound/{file_name}.mp4")

            print(" ")
            print("The video is downloaded in MP3")
        except RegexMatchError:
            print("Unable to fetch video information. Please check the video URL, provide the correct URL or your "
                  "network connection.")
    else:
        print("The path is wrong or doesn't exist. Please enter the correct path.")
