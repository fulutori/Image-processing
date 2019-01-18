# -*- coding:utf-8 -*-
import cv2
import os
from PIL import Image

print("ディレクトリ名を入力してください")
dir_name = input()
image_dir = "./face/" + dir_name
cascade_path = "./lbpcascade_animeface.xml"
pic = os.listdir(r'./face/'+dir_name)

dir_path = './face_r/'+dir_name
if os.path.isdir(dir_path) == False:
	os.mkdir(dir_path)

i=0
for f in range(len(pic)):
    img = image_dir + '/' + str(pic[f])
    image = cv2.imread(img)
    if(image is None):
        print('画像を開けません。')
        quit()

    re_image = image.resize((100,100))
    re_image.save("re"+pic[f])

    #上下反転
    tmp = re_image.transpose(Image.FLIP_TOP_BOTTOM)
    tmp.save("flipTB_" + f)
    #90度回転
    tmp = image.transpose(Image.ROTATE_90)
    tmp.save("spin90_" + f)
    #270度回転
    tmp = image.transpose(Image.ROTATE_270)
    tmp.save("spin270_" + f)
    #左右反転
    tmp = image.transpose(Image.FLIP_LEFT_RIGHT)
    tmp.save("flipLR_" + f)
    print("{} is done!".format(f))
    i += 1
