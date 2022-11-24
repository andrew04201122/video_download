import os
from os import listdir
from os.path import isfile, isdir, join
import random
import shutil

dist = 'D:/video/watch'
video_position= 'E://Pvideo//'


file_list = ['EU//','japan//','long_video//','sensed//']
file_choice = random.randint(0,3)
video_position = video_position + file_list[file_choice]

os.chdir(video_position)
print("Current working directory: {0}".format(os.getcwd()))
files = listdir(os.getcwd())
video = []

for i in range(len(files)):
    if 'mp4' in files[i]:
        files[i] =  video_position  + files[i]
        video.append(files[i])

video_choice = random.randint(0,len(video)-1)


shutil.copy2(video[video_choice], dist)