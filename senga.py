# -*- coding: utf-8
import sys
import cv2
import numpy as np

def mksenga(path):
	neiborhood24 = np.array([[1, 1, 1, 1, 1],
							 [1, 1, 1, 1, 1],
							 [1, 1, 1, 1, 1],
							 [1, 1, 1, 1, 1],
							 [1, 1, 1, 1, 1]],
							 np.uint8)
	#グレースケールで画像を読み込む
	gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

	#白い部分を膨張させる
	dilated = cv2.dilate(gray, neiborhood24, iterations=1)

	#差をとる
	diff = cv2.absdiff(dilated, gray)

	#白黒反転
	contour = 255 - diff
	out_name = "./"+path.replace(".png","").replace(".jpg","").replace(".gif","")+"_sen.png"
	cv2.imwrite(out_name, contour)
	return contour

if __name__ == '__main__':
	path = sys.argv[1]
	#path = "kancolle_4097.jpg"
	mksenga(path)
