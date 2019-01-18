# -*- coding:utf-8 -*-
import cv2
import sys
import os
import shutil

print("ディレクトリ名を入力してください")
dir_name = input()
image_dir = "./image/" + dir_name
cascade_path = "./lbpcascade_animeface.xml"
pic = os.listdir(r'./image/'+dir_name)

dir_path = './face/'+dir_name
if os.path.isdir(dir_path) == False:
	os.mkdir(dir_path)

i=0
number=0
for f in range(len(pic)):
	#ファイル読み込み
	img = image_dir + '/' + str(pic[f])
	image = cv2.imread(img)
	if(image is None):
		print ('画像を開けません。')
		quit()

	#グレースケール変換
	image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	#カスケード分類器の特徴量を取得する
	cascade = cv2.CascadeClassifier(cascade_path)

	#物体認識（顔認識）の実行
	facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.2, minNeighbors=2, minSize=(10, 10))
	if len(facerect) == 0:
		continue
	for rect in facerect:
		#顔だけ切り出して保存
		x = rect[0]
		y = rect[1]
		width = rect[2]
		height = rect[3]
		dst = image[y:y+height, x:x+width]
		new_image_path = dir_path + '/' + str(i) + '.jpg';
		cv2.imwrite(new_image_path, dst)
		print(str(f) + ":" + pic[f])
		i += 1
	number += 1

print("処理した画像：" + str(f+1))
print("抽出した画像：" + str(number))
