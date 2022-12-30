# Wistia Video Ripper

Wistia Ripper is a file designed to be able to download wistia-hosted videos with a copy-pasted link from the thumbnail

## Installation

Drag the wistia_ripper.py file into any folder you'd like

## Usage

1. Right click on the thumbnail on a wistia video.
2. Click 'Copy link from thumbnail'
3. Run the .py file
4. Paste the link
5. The file will be downloaded to a folder called 'videos' in the same directory as wistia_ripper.py

## How this works

Since wistia videos can also be downloaded by YoutubeDL, it utilizes that library. However, this leaves it in a state of .bin. Using ffmpeg it converts it into .mp4
