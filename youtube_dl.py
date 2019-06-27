#!/usr/bin/python
# coding: utf-8

from pytube import YouTube
import os

DL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')

if __name__ == '__main__':
    try:
        yt = YouTube(raw_input('URL : '))
        yt.streams.first().download(DL_PATH)
        print 'Download complete'
    except:
        print 'Download failed'
