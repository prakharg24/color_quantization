import numpy as np
import cv2 as cv

def cal_dist(p1,p2):
	val = 0
	for i in range(3):
		val += (p1[i] - p2[i])**2
	return val	

def find_close(point,lis):
	min_pt = lis[0]
	min_val = cal_dist(point,lis[0])
	for i in range(len(lis)):
		val = cal_dist(point,lis[i])
		if(val<min_val):
			min_val = val
			min_pt = lis[i]
	return min_pt

img = cv.imread('messi5.jpg')
zoom = 2
img = np.array(img)
a = np.zeros((256,256,256),dtype = int)
#new_img = np.zeros((zoom*len(img), zoom*len(img[0]), 3))
dic = {} 
for i in range(len(img)):
	for j in range(len(img[0])):
		if((img[i][j][0],img[i][j][1],img[i][j][2]) in dic):
			dic[(img[i][j][0],img[i][j][1],img[i][j][2])] += 1
		else:
			dic[(img[i][j][0],img[i][j][1],img[i][j][2])] = 1


lis = sorted(dic, key=lambda k: dic[k],reverse = True)

# for k in lis:
# 	print(k,dic[k])

new_img = np.zeros((len(img),len(img[0]),3))

for i in range(len(img)):
	for j in range(len(img[0])):
		print(i,j)
		point = (img[i][j][0],img[i][j][1],img[i][j][2])
		cl_pt = find_close(point,lis[0:500])
		new_img[i][j][0] = cl_pt[0]/255.0
		new_img[i][j][1] = cl_pt[1]/255.0
		new_img[i][j][2] = cl_pt[2]/255.0
# for key in sorted(dic.iterkeys()):
#     print("%s: %s" % (key, dic[key]))


# res = cv.resize(new_img,None,fx=1, fy=1, interpolation = cv.INTER_CUBIC)
cv.imshow('det',new_img)
cv.waitKey(0)
cv.destroyAllWindows()
