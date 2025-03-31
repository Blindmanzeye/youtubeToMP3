import os
from moviepy.editor import VideoFileClip


def videoToAudio(videoPath: str):
    video = VideoFileClip(videoPath)
    mp3Path = videoPath.removesuffix("mp4") + "mp3"
    video.audio.write_audiofile(mp3Path)
    print("done")
userPath = os.environ['USERPROFILE']
download_location = userPath + r"\Desktop\downloadedSongs"
os.makedirs(download_location, exist_ok=True)

filePath = input("Please enter the filepath of your video file: ")
videoToAudio(filePath)