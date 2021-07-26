from __future__ import unicode_literals
import youtube_dl


ydl = youtube_dl.YoutubeDL({'format': 'mp4'})


def download(url):
    ydl.download([url])
