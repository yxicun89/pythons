import cv2  # OpenCVのインポート
import numpy as np  # numpyのインポート

img = cv2.imread('/Users/nishimurayuuhajime/python/santa_girl.jpg') # 画像の読み出し
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # BGR->HSV変換
hsv_2 = np.copy(hsv)
hsv_3 = np.copy(hsv)

# h>173の画素のhを-90
hsv_2[:, :, 0] = np.where(hsv[:, :, 0]>173,hsv[:, :, 0]-90,hsv[:, :, 0])
# h<5の画素のhを+90
hsv_3[:, :, 0] = np.where(hsv_2[:, :, 0]<5,hsv_2[:, :, 0]+90,hsv_2[:, :, 0])

bgr = cv2.cvtColor(hsv_3, cv2.COLOR_HSV2BGR) # HSV->BGR変換

cv2.imwrite('/Users/nishimurayuuhajime/python/santa_girl.jpg',bgr) # 画像の保存 
#cv2.imshow()
#cv2.waitKey()