# pytube is a libary use for downloading Youtube videos  
from pytube import YouTube

#tqdm is a libary use for showing progress bar 
from tqdm import tqdm
import time



def down_youtube(link):
    yt = YouTube(link)

    videos = yt.streams.all()
    list_q = []

    i = 1
    for stream in videos:
        str_stream = str(stream)
        print(str(i) + ' ' + str_stream[41:53])
        i += 1


    stream_number = int(input('enter stream number'))

    video_download = videos[stream_number - 1]

    for x in tqdm(range(1000)):
        video_download.download("./dowload_item")
        time.sleep(0.01)

    print('dowloaded')
