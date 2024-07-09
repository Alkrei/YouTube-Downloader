from pytube import Playlist
from rich.progress import Progress
import pytube
import os


def playlist_video_loader():
    url = str(input("Youtube playlist url :"))
    with Progress() as progress:
        pl = Playlist(url)
        num = 0
        try:
            task = progress.add_task("[cyan]Downloading...", total=len(pl))
        except KeyError:
            print(
                "Unable to fetch playlist information. Please check the playlist URL, provide the correct URL or your "
                "network connection.")
        while not progress.finished:
            for video in pl.videos:
                try:
                    stream = video.streams.filter(progressive=True).get_highest_resolution()
                    if not os.path.exists(f"playlist/{stream.default_filename}"):
                        stream.download(output_path="playlist/")
                        print("Successfully")
                        print(video.title)
                        print(" ")
                        num += 1
                    elif os.path.exists(f"playlist/{stream.default_filename}"):
                        print("Pass")
                        print(video.title)
                        print(" ")
                except pytube.exceptions.AgeRestrictedError:
                    print("Error")
                    print(video.title)
                    print(" ")
                progress.update(task, advance=1)
            print(f"+{num} videos!")
            print("The video playlist is downloaded in MP4")
