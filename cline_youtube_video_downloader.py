from pytube import YouTube

def download_youtube_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        print(f"Video '{yt.title}' downloaded successfully!")
    except Exception as e:
        print(f"Error downloading video: {e}")

if __name__ == "__main__":
    video_url = input("Enter a YouTube video URL: ")
    download_youtube_video(video_url)
