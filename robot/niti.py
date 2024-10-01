import numpy as np
import cv2
import matplotlib.pyplot as plt
# from statistics import variance
import statistics as st
plt.gray()


def otsuBinarization(img):
  # 画像コピー
  dst = img.copy()
  # グレースケール化
  gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

  w,h = gray.shape
  Max = 0

  # 画像全体の画素値平均
  M = np.mean(gray)

  # 閾値256値全てに適用
  for th in range(256):
    # クラス分け
    g0,g1 = gray[gray<th],gray[gray>=th]

    # 画素数
    w0,w1 = len(g0),len(g1)
    # 画素値分散
    s0_2,s1_2 = g0.var(),g1.var()
    # 画素値平均
    m0,m1 = g0.mean(),g1.mean()
    # 画素値合計
    p0,p1 = g0.sum(),g1.sum()

    # クラス内分散
    sw_2 = w0*s0_2 + w1*s1_2
    # クラス間分散
    sb_2 = ((w0*w1) / ((w0+w1)*(w0+w1))) * ((m0-m1)*(m0-m1))
    # 分離度
    if (sb_2 != 0):
      X = sb_2 / sw_2
    else:
      X = 0

    if (Max < X):
      Max = X
      t = th

  # 二値化
  idx = np.where(gray < t)
  gray[idx] = 0
  idx = np.where(gray >= t)
  gray[idx] = 255

  return gray


# 画像読込
img = cv2.imread('/Users/nishimurayuuhajime/Desktop/スクリーンショット 2022-10-28 23.05.43.png')

# 大津の二値化
mono = otsuBinarization(img)

# 画像保存
cv2.imwrite('result.jpg', mono)
# 画像表示
plt.imshow(mono)
plt.show()