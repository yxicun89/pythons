import cv2

WIDTH = 130
HEIGHT = 41

img = cv2.imread('gundam.png')
print(img[15, 30])

for x in range(HEIGHT):
    for y in range(WIDTH):
        b, g, r = img[x, y]
        if (b, g, r) == (255, 255, 255):
            continue
        img[x, y] = 0, g, r

cv2.imwrite('edit.png', img)