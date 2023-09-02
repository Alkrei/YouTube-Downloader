from moviepy.editor import VideoFileClip
from pytube import YouTube

url = str(input("Youtube video url :"))
video = YouTube(url)
print(video.title)
video.streams.filter(progressive=True).desc().first().download("playlist/")

clip = VideoFileClip(f"{video.title}.mp4")
audio = clip.audio
audio.write_audiofile("music/.mp3")
