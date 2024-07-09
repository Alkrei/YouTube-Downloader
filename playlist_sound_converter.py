from pathlib import Path
import os


def playlist_sound_converter():
    playlist = Path("playlist/").glob('*.mp4')
    for video in playlist:
        file_name = os.path.splitext(os.path.basename(video))[0]
        if not os.path.exists(f"sound_playlist/{file_name}.mp3"):
            command = f"ffmpeg -i 'playlist/{file_name}.mp4' 'sound_playlist/{file_name}.mp3'"
            os.system(command)
        else:
            print("pass")
            print(" ")
    print("The playlist is converted in MP3")
