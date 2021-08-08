# ydl1.py
from __future__ import unicode_literals
import youtube_dl


print('This is for downloading spotify songs')
print('Author:G.A.Roshan Melvin')
print('Contact: datatech644@gmail.com')
print('a - video to audio')
print('v - video')
print('s - For downloading spotify songs')
action=input('Ender your option a/v/s:')

if action=='v':
 link = input("Enter your link:")

 ydl_opts = {}
 with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
elif action=='a':
 
 links = input('Enter link:')
 class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


 def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


 ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],

    'logger': MyLogger(),
    'progress_hooks': [my_hook],
 }
 with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([links])
#thats all
elif action==s :
   action2=input('Enter your option:')
   elif action2== 'l':
     spotify=input('Enter your spotify link:')
     print(os.system('spotifydl -o '+str(Path.home() / "Downloads ") + spotify))
else :
 print("Enter correct option")
    
 
