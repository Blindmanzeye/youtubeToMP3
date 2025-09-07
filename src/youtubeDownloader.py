from pytubefix import YouTube
from moviepy.editor import VideoFileClip
from pytubefix.cli import on_progress
import os
import time
# C:\Users\infer\Documents\programming\pythonStuff\pythonWorks\Projects\theUltimateFileConverter



def videoToAudio(videoPath: str):
    video = VideoFileClip(videoPath)
    mp3Path = videoPath.removesuffix("mp4") + "mp3"
    video.audio.write_audiofile(mp3Path)
    print("done")
    

if __name__ == "__main__":
    print("This is Youtoob audio file downloader")
    print("All audio files will be downloaded to your desktop")
    linkloop = True
    while linkloop:
        # Specify the YouTube video URL
        video_url = input("Youtube Link Here: ")

        # Create a YouTube object
        yt = YouTube(video_url, on_progress_callback=on_progress)
        print(yt.title)

        ys = yt.streams.get_highest_resolution()
        userPath = os.environ['USERPROFILE']
        download_location = userPath + r"\Desktop\downloadedYT"
        os.makedirs(download_location, exist_ok=True)
        ys.download(output_path=download_location)

        if input("Download another file? (y/n): ").lower() == "n":
            linkloop = False

