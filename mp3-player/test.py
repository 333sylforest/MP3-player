import os

os.chdir("/Users/kimberleyellars/github/MP3-player/mp3-player/music")
print(os.getcwd())

songtracks = os.listdir(os.getcwd())

print(songtracks)
