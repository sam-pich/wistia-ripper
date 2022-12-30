# Imports necessary libraries
from __future__ import unicode_literals
from urllib.parse import unquote
import youtube_dl
import os
import ffmpeg

# Sets the file path to whatever directory this file is located in
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# If this directory/videos does not exist, create it
if os.path.exists(dname+'/videos') == False:
    os.mkdir(os.path.join(dname, "videos"))

# Change directory name to include /videos
dname = dname + '/videos'
os.chdir(dname)

# Youtube downloader format for downloading the wistia videos
ydl_opts = {}

ydl_opts = {
    'outtmpl': './%(title)s-%(id)s.%(ext)s',
}

# Input the link
templink = input('Enter: ')
print("\n")
print(templink)

# Parses the line for src= and the first &, of which you only need the link inbetween
sourceIndex = templink.index("src=")
andIndex = templink.index("&")
templink = templink[sourceIndex+4:andIndex]
templink = unquote(templink)

# Downloading the video as a .bin file
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([templink])

# For every .bin file in the directory, convert it to .mp4 using FFMPEG, then delete the bin file
for filename in os.listdir(dname):
    f = os.path.join(dname,filename)
    if f.endswith(".bin"):
        print(filename)
        inputbin = filename
        outputvid = filename[0:-5] + ".mp4"

        (
            ffmpeg
            .input(f)
            .output(dname + '/' + outputvid)
            .run()
        )
        os.remove(f)

print("Finished")