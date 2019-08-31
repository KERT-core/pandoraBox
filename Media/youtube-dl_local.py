#!/usr/bin/python3
# -*- coding: utf-8 -*-
import youtube_dl
from tqdm import tqdm

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


if __name__ == "__main__":
    print("Please Enter URL of video that you want to download")
    link = input()
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
        'nocheckcertificate': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
