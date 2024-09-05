from tkinter import *
from pytube import YouTube

def download_video():
    url = entry.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        status_label.config(text=f"Video '{yt.title}' downloaded successfully!")
    except Exception as e:
        status_label.config(text=f"Error downloading video: {e}")

root = Tk()
root.title("YouTube Video Downloader")

entry = Entry(root, width=40)
entry.pack(pady=10)

download_button = Button(root, text="Download", command=download_video)
download_button.pack()

status_label = Label(root, text="")
status_label.pack()

root.mainloop()
