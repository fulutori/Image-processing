import os
import shutil
import cv2

def video_change():
	movie_file = './mkmovie.mov'
	count = 0
	cap = cv2.VideoCapture(movie_file)
	while True:
		ret, frame = cap.read()
		if ret == True:
			count += 1
			cv2.imwrite('./img/img_' + str("{0:05d}".format(count)) +'.jpg', frame)
		else:
			break

if __name__ == '__main__':
	video_change()