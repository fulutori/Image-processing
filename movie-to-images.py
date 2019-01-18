# coding: utf-8
import os
import shutil
import cv2


def video_2_frames(video_file='./movie/sample.mp4', image_dir='./img/', image_file='img_%s.png'):
	# 指定したディレクトリが既にあれば削除
	if os.path.exists(image_dir):
		shutil.rmtree(image_dir)

	# ディレクトリを作成
	if not os.path.exists(image_dir):
		os.makedirs(image_dir)

	# 動画をフレームで切り出して保存
	i = 0
	cap = cv2.VideoCapture(video_file)
	while(cap.isOpened()):
		flag, frame = cap.read() # フレームを読み込む
		if flag == False: # 読み込めないとき
			break
		cv2.imwrite(image_dir+image_file % str(i).zfill(6), frame) # 画像を保存
		print('Save', image_dir+image_file % str(i).zfill(6))
		i += 1

	cap.release()

if __name__ == '__main__':
	video_2_frames()
