from pytube import YouTube
from pytube.exceptions import RegexMatchError
import os


def solo_video_loader():
    path = str(input("Path :"))
    if os.path.exists(path):
        try:
            url = str(input("Youtube video url :"))
            video = YouTube(url)
            print(video.title)
            stream = video.streams.filter(progressive=True).get_highest_resolution()
            stream.download(output_path=path)
            print("The video is downloaded in MP4")
        except RegexMatchError:
            print("Unable to fetch video information. Please check the video URL, provide the correct URL or your "
                  "network connection.")
    else:
        print("The path is wrong or doesn't exist. Please enter the correct path.")
