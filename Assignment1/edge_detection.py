import numpy as np
import cv2 as cv
from scipy.ndimage.filters import gaussian_filter


def x_dog(image,ep,k,gamma):
	p = 20

	dif_fil = dog(image, k, gamma)/255
	#diff = dif_fil*image
	edge_fil = np.zeros((len(dif_fil), len(dif_fil[0])))

	for i in range(0, len(dif_fil)):
		for j in range(0, len(dif_fil[0])):
			if dif_fil[i][j].all() < ep:
				edge_fil[i][j] = 1
			else:
				ht = np.tanh(np.sum(dif_fil[i][j])*p)
				edge_fil[i][j] = 1 + ht
			for k in range(0, 3):
				dif_fil[i][j][k] = int(edge_fil[i][j]*124)

	return dif_fil*255

def dog(image,k,gamma):
	fir_fil = 0.5
	sec_fil = fir_fil*k
	filter1 = gaussian_filter(image,fir_fil)
	filter2 = gamma*gaussian_filter(image,sec_fil)
	diff_filter = filter2 - filter1
	return diff_filter

img = cv.imread('gary.jpg')
result = x_dog(img, 0.05, 10, 0.98)

cv.imshow('det',result)
cv.waitKey(0)
cv.destroyAllWindows()