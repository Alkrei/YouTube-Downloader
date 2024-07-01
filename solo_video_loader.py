from pytube import YouTube


def solo_video_loader():
    try:
        url = str(input("Youtube video url :"))
        video = YouTube(url)
        print(video.title)
        stream = video.streams.filter(progressive=True).get_highest_resolution()
        stream.download(output_path="video/")
        print("The video is downloaded in MP4")
    except Exception:
        print("Unable to fetch video information. Please check the video URL, provide the correct URL or your network "
              "connection.")


solo_video_loader()
