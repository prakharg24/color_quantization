import numpy as np
import cv2 as cv
import sys

if(len(sys.argv)!=4):
	print("Required -> python Zin_replicate.py <input_image> <zoom> <output_image>")
	exit()

img = cv.imread(sys.argv[1])
zoom = int(sys.argv[2])

img = np.array(img)

new_img = np.zeros((int(len(img)/zoom), int(len(img[0])/zoom), 3))

for i in range(len(new_img)):
	if(i%100==0):
		print(i, "out of", len(new_img), "done")
	for j in range(len(new_img[0])):
		new_img[i][j][0] = img[i*zoom][j*zoom][0]
		new_img[i][j][1] = img[i*zoom][j*zoom][1]
		new_img[i][j][2] = img[i*zoom][j*zoom][2]


cv.imwrite(sys.argv[3], new_img)