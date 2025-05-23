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
    print("This is Youtoob audio file downloader by your little brother")
    print("All audio files will be downloaded to your desktop")
    linkloop = True
    while linkloop:
        # Specify the YouTube video URL
        video_url = input("Youtube Link Here: ")

        # Create a YouTube object
        yt = YouTube(video_url, "WEB", on_progress_callback=on_progress)

        # Display video title
        print(f"Video Title: {yt.title}")

        # Select the best audio stream
        audio_stream = yt.streams.get_audio_only()

        # Specify the download location (or leave blank for the current directory)
        userPath = os.environ['USERPROFILE']
        download_location = userPath + r"\Desktop\downloadedSongs"
        os.makedirs(download_location, exist_ok=True)

        # Download the audio
        print("Downloading audio...")
        audio_stream.download(output_path=download_location)
        print("Download completed!")

        # This part of code is for if the downloaded file is an mp4
        # videoPath = download_location + rf"\{yt.title}.mp4"
        # videoToAudio(videoPath)
        # print("MP3 File downloaded, Preparing for temp mp4 file deletion")
        # time.sleep(10)
        # os.remove(videoPath)

        if input("Download another file? (y/n): ").lower() == "n":
            linkloop = False

