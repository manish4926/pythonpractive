import pytube
import numpy as np
from pytube import Playlist
link = "https://www.youtube.com/watch?v=9YSbflKeOZQ"
yt = pytube.YouTube(link)
# print(yt.streams)
# print(yt)
# print(yt.title)
# print(yt.thumbnail_url)
# print(yt.captions)
#print(yt.streaming_data['formats'])
# print(yt.streams.get_highest_resolution)

formats = yt.streaming_data['formats']

for list in formats:
    print(list)
    print(float(list['qualityLabel']))
    for key, value in list.items():

        pass


# stream = yt.streams.filter(only_audio=True).first()
# print(stream)
# stream.download()
