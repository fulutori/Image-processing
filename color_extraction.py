from PIL import Image
import numpy as np
import time

current_dir = '/home/' #作業用ディレクトリのpath
save_dir = 'store/' #変換後の保存用path
i_path = 'town_img/hoge.png' #テスト用画像のpath
img = np.array(Image.open(current_dir+i_path)) #画像を読み込んで配列に変換

#RGBの閾値(これより赤い部分だけ抽出)
target_color = [234, 86, 73]

#生成する画像のサイズ
width = 1920
height = 1080

#イメージ生成
new_img = Image.new('RGB', (width, height), (0, 0, 0))

cnt = 0
for y,i in enumerate(img):
	#赤線が無いと思われる部分は飛ばす
	if y < height*0.1:
		continue
	elif y > height*0.9:
		break

	for x,t in enumerate(i):
		#赤線が無いと思われる部分は飛ばす
		if x < width*0.2:
			continue
		elif x > width*0.9:
			break

		#閾値を超えている部分を特定
		if t[0]>=target_color[0] and t[1]<=target_color[1] and t[2]<=target_color[2]:
			new_img.putpixel((x, y), (255, 0, 0))

#タイムスタンプで画像保存用のファイル名を作成
name = current_dir+save_dir+str(time.strftime('%Y%m%d%H%M%S', time.strptime(time.ctime())))+'.png'
new_img.save(name)
