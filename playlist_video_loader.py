from pytube import Playlist
from rich.progress import Progress
import pytube
import os


with Progress() as progress:
    pl = Playlist("https://www.youtube.com/playlist?list=PLrRPjcGNN3MeVnD7NrGTaKrhpNVaft2uK")
    num = 0
    task = progress.add_task("[cyan]Downloading...", total=len(pl))

    while not progress.finished:
        for video in pl.videos:
            try:
                if not os.path.exists(f"playlist/{video.title}.mp4"):
                    video.streams.filter(progressive=True).desc().first().download("playlist")
                    print("Successfully")
                    print(video.title)
                    print(" ")
                    num += 1
                elif os.path.exists(f"playlist/{video.title}.mp4"):
                    print("Pass")
                    print(video.title)
                    print(" ")
            except pytube.exceptions.AgeRestrictedError:
                print("Error")
                print(video.title)
                print(" ")
            progress.update(task, advance=1)
            print(f"+{0} soundtracks!")
