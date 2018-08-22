import numpy as np
import cv2 as cv

img = cv.imread('messi5.jpg')
zoom = 2
img = np.array(img)

new_img = np.zeros((zoom*len(img), zoom*len(img[0]), 3))

for i in range(len(new_img)-zoom):
	for j in range(len(new_img[0])-zoom):
		a = i%zoom
		c = j%zoom
		mat0 = np.array([[img[int(i/zoom)][int(j/zoom)][0],img[int(i/zoom)][int(j/zoom)+1][0]],[img[int(i/zoom+1)][int(j/zoom)][0],img[int(i/zoom)+1][int(j/zoom)+1][0]]])
		mat1 = np.array([[img[int(i/zoom)][int(j/zoom)][1],img[int(i/zoom)][int(j/zoom)+1][1]],[img[int(i/zoom+1)][int(j/zoom)][1],img[int(i/zoom)+1][int(j/zoom)+1][1]]])
		mat2 = np.array([[img[int(i/zoom)][int(j/zoom)][2],img[int(i/zoom)][int(j/zoom)+1][2]],[img[int(i/zoom+1)][int(j/zoom)][2],img[int(i/zoom)+1][int(j/zoom)+1][2]]])
		y_arr = np.array([zoom-c,c])
		x_arr = np.array([zoom-a,a])
		new_img[i][j][0] = np.matmul(x_arr,(np.matmul(mat0,np.transpose(y_arr))))/(zoom*zoom*255.0)
		new_img[i][j][1] = np.matmul(x_arr,(np.matmul(mat1,np.transpose(y_arr))))/(zoom*zoom*255.0)
		new_img[i][j][2] = np.matmul(x_arr,(np.matmul(mat2,np.transpose(y_arr))))/(zoom*zoom*255.0)

# res = cv.resize(new_img,None,fx=1, fy=1, interpolation = cv.INTER_CUBIC)
cv.imshow('det',new_img)
cv.waitKey(0)
cv.destroyAllWindows()