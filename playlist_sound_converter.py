from moviepy.editor import VideoFileClip
from pathlib import Path
import os

playlist = Path("playlist/").glob('*.mp4')
for video in playlist:
    if not os.path.exists(f"music/{video.name[:-4]}.mp3"):
        clip = VideoFileClip(f"{video}")
        audio = clip.audio
        audio.write_audiofile(f"music/{video.name[:-4]}.mp3")
    else:
        print("pass")
        print(" ")
