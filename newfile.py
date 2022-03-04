# ydl1.py
from __future__ import unicode_literals
import youtube_dl
import os
from pathlib import Path
text = 'YouSpot'
os.system("cfonts "+text+" -f block -c bright_red ")

print('Author:G.A.Roshan Melvin')
print('Contact: datatech644@gmail.com')
print("")
print("")
print('1 - Youtube video to audio.')
print('2 - Youtube video.')
print('3 - Spotify song downloader.')
action=input('Enter your option :')

if action=='2':
 link = input("Enter your link:")

 ydl_opts = {}
 with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

elif action=='1':
 
 links = input('Enter your audio link:')
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
elif action=='3':
   print('1-For android.')
   print('2-For linux.')

   action2=input('Enter your option:') 
   if action2== '1':
     spotify=input('Enter your spotify link:')
     print(os.system('spotifydl -o /sdcard/Download/ '+ spotify))
   elif action2== '2':
     spotify=input('Enter your spotify link:')
     print(os.system('spotifydl -o '+str(Path.home() / "Downloads ") + spotify))
   else :
     print('Enter your correct os')
else :
 print("Enter correct option")
 print("""try again by using "bash termux.sh" in termux and "python newfile.py or python3 newfile.py".""")

