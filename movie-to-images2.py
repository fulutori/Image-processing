# -*- coding: utf-8 -*-
import cv2
import os

#動画ファイルを読み込む
file_name = u"/home/aokakes/works/python/smakoma/gochiusa.mp4"
video = cv2.VideoCapture(file_name)
print (file_name)

#スクリーンキャプチャを保存するディレクトリ
dir_name = "img"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

#フレーム数を取得
frame_count = int(video.get(7))
print (frame_count)
for i in range(frame_count):
    frame = video.read()
    cv2.imwrite(dir_name+ "/" + str(i) + ".png", frame)
