# ydl1.py
from __future__ import unicode_literals
import youtube_dl
link = input("Enter your link:")

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
    
 