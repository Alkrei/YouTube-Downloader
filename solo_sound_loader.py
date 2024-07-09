from pytube import YouTube
import os


def solo_sound_loader():
    try:
        url = str(input("Youtube video url :"))
        video = YouTube(url)
        print(f"{video.title}")
        print(" ")
        stream = video.streams.filter(progressive=True).get_highest_resolution()
        file = stream.download(output_path="./")
        file_name = os.path.splitext(os.path.basename(file))[0]

        command = f"ffmpeg -i '{file_name}.mp4' 'sound/{file_name}.mp3'"
        os.system(command)
        os.remove(f"{file_name}.mp4")
        print("The video is downloaded in MP3")
    except Exception:
        print("Unable to fetch video information. Please check the video URL, provide the correct URL or your network "
              "connection.")
