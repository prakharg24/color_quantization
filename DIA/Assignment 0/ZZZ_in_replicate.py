import numpy as np
import cv2 as cv

img = cv.imread('messi5.jpg')
zoom = 5
img = np.array(img)

new_img = np.zeros((zoom*len(img), zoom*len(img[0]), 3))

for i in range(len(new_img)):
	for j in range(len(new_img[0])):
		new_img[i][j][0] = img[int(i/zoom)][int(j/zoom)][0]/255.0
		new_img[i][j][1] = img[int(i/zoom)][int(j/zoom)][1]/255.0
		new_img[i][j][2] = img[int(i/zoom)][int(j/zoom)][2]/255.0


# res = cv.resize(new_img,None,fx=1, fy=1, interpolation = cv.INTER_CUBIC)
cv.imshow('det',new_img)
cv.waitKey(0)
cv.destroyAllWindows()