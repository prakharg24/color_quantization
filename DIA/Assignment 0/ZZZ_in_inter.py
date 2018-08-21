import numpy as np
import cv2 as cv

img = cv.imread('messi5.jpg')
zoom = 2
img = np.array(img)

new_img = np.zeros((zoom*len(img), zoom*len(img[0]), 3))

# for i in range(len(img)):
# 	for j in range(len(img[0])):
# 		new_img[i*zoom][j*zoom][0] = img[i][j][0]/255.0
# 		new_img[i*zoom][j*zoom][1] = img[i][j][1]/255.0
# 		new_img[i*zoom][j*zoom][2] = img[i][j][2]/255.0

# for i in range(len(img)):
# 	for j in range(len(new_img[0])-zoom):
# 		new_img[i*zoom][j][0] = (((zoom - j%zoom)/zoom)*img[i][int(j/zoom)][0] + ((j%zoom)/zoom)*img[i][int(j/zoom)+1][0])/255.0
# 		new_img[i*zoom][j][1] = (((zoom - j%zoom)/zoom)*img[i][int(j/zoom)][1] + ((j%zoom)/zoom)*img[i][int(j/zoom)+1][1])/255.0
# 		new_img[i*zoom][j][2] = (((zoom - j%zoom)/zoom)*img[i][int(j/zoom)][2] + ((j%zoom)/zoom)*img[i][int(j/zoom)+1][2])/255.0

# for i in range(len(new_img)-zoom):
# 	for j in range(len(img[0])):
# 		new_img[i][j*zoom][0] = (((zoom - i%zoom)/zoom)*img[int(iz)][j][0] + ((i%zoom)/zoom)*img[int(iz)+1][j][0])/255.0
# 		new_img[i][j*zoom][1] = (((zoom - i%zoom)/zoom)*img[int(iz)][j][1] + ((i%zoom)/zoom)*img[int(iz)+1][j][1])/255.0
# 		new_img[i][j*zoom][2] = (((zoom - i%zoom)/zoom)*img[int(iz)][j][2] + ((i%zoom)/zoom)*img[int(iz)+1][j][2])/255.0

for i in range(len(new_img)-zoom):
	for j in range(len(new_img[0])-zoom):
		a = i%zoom
		c = j%zoom
		iz = i/zoom
		jz = j/zoom
		mat0 = np.array([[img[iz][jz][0],img[iz][jz+1][0]],[img[iz+1][jz][0],img[iz+1][jz+1][0]]])
		mat1 = np.array([[img[iz][jz][1],img[iz][jz+1][1]],[img[iz+1][jz][1],img[iz+1][jz+1][1]]])
		mat2 = np.array([[img[iz][jz][2],img[iz][jz+1][2]],[img[iz+1][jz][2],img[iz+1][jz+1][2]]])
		y_arr = np.array([zoom-c,c])
		x_arr = np.array([zoom-a,a])
		new_img[i][j][0] = np.matmul(x_arr,(np.matmul(mat0,np.transpose(y_arr))))/(zoom*zoom*255.0)
		new_img[i][j][1] = np.matmul(x_arr,(np.matmul(mat1,np.transpose(y_arr))))/(zoom*zoom*255.0)
		new_img[i][j][2] = np.matmul(x_arr,(np.matmul(mat2,np.transpose(y_arr))))/(zoom*zoom*255.0)

# res = cv.resize(new_img,None,fx=1, fy=1, interpolation = cv.INTER_CUBIC)
cv.imshow('det',new_img)
cv.waitKey(0)
cv.destroyAllWindows()