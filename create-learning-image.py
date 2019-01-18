# -*- coding: utf-8 -*-
import cv2
import sys
import shutil
from PIL import Image
import os

def extraction(pic):
	i = 0
	number = 0
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

def readImg(imgName):
	try:
		img_src = Image.open(dir_path + "/" + imgName)
	except:
		img_src = 1
	return img_src


def spinImg(imgNames):
	for imgName in imgNames:
		img_src = readImg(imgName)
		if img_src == 1:continue
		else:
			rotation = [90,180,270]
			rotation15 = [15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345]
			for rad in rotation:
				#45
				tmp = img_src.rotate(rad)
				tmp.save(dir_path + "/spin" + str(rad) + "_" + imgName)
			#上下反転
			tmp = img_src.transpose(Image.FLIP_TOP_BOTTOM)
			tmp.save(dir_path + "/flipTB_" + imgName)
			#左右反転
			tmp = img_src.transpose(Image.FLIP_LEFT_RIGHT)
			tmp.save(dir_path + "/flipLR_" + imgName)

if __name__ == '__main__':
	#アニメ顔の分類器を読み込み
	cascade_path = "./lbpcascade_animeface.xml"

	#処理する画像があるディレクトリを入力
	print("ディレクトリ名を入力してください")
	dir_name = input()
	image_dir = "./image/" + dir_name	#処理前の画像path
	dir_path = "./face/" + dir_name		#処理後の画像path
	face = "./face"

	#保存先のディレクトリが存在するか確認、無ければ作成
	if os.path.isdir(face) == False:
		os.mkdir(face)
	if os.path.isdir(dir_path) == False:
		os.mkdir(dir_path)

	#処理前の画像のファイル名をリスト化
	pic = os.listdir(image_dir)
	#入力したディレクトリにある画像から顔部分を抽出
	print("「" + dir_name + "」の画像処理を開始します")
	extraction(pic)
	#処理後の画像を上下左右反転、90度270度回転させたものを保存
	dir_path = "./face/" + dir_name
	imgNames = os.listdir(dir_path)
	spinImg(imgNames)
	print("「" + dir_name + "」の画像処理が完了しました")
