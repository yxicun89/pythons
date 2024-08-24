import cv2
import numpy as np

image = cv2.imread('/Users/nishimurayuuhajime/Documents/写真/dark1.jpeg')
# 画像の黒い部分を白に置き換える
black = [0, 0, 0]
white = [255, 255, 255]
image[np.where((image == black).all(axis=2))] = white