import numpy as np
import cv2 as cv
import sys

class medianBox:

	def __init__(self):
		self.bounds = [255., 0., 255., 0., 255., 0.]
		self.points = []

	def get_median(self,dim):
		med_array = []
		for ele in self.points:
			med_array.append(ele[dim])

		print("Start sort")
		lis = sorted(med_array)
		return lis[int(len(lis)/2)]
	
	def get_max_bound(self):
		maxv = 0
		maxd = -1
		for i in range(0, 6, 2):
			if(self.bounds[i+1] - self.bounds[i] > maxv):
				maxv = self.bounds[i+1] - self.bounds[i]
				maxd = i/2

		return int(maxd)

	def add_element(self,pnt):
		self.points.append(pnt)
		for i in range(0, 6, 2):
			if(pnt[int(i/2)]<self.bounds[i]):
				self.bounds[i] = pnt[int(i/2)]
			if(pnt[int(i/2)]>self.bounds[i+1]):
				self.bounds[i+1] = pnt[int(i/2)]

def medianCut(mdBox):
	maxBound = mdBox.get_max_bound()
	med = mdBox.get_median(maxBound)

	print("Median :", med)

	child1 = medianBox()
	child2 = medianBox()

	print(len(mdBox.points))
	for ele in mdBox.points:
		if(ele[maxBound]<=med):
			child1.add_element(ele)
		else:
			child2.add_element(ele)

	print("Cut done")

	return child1, child2

def completeMedianCut(dic_keys,k):
	print(len(dic_keys))
	initialBox = medianBox()

	for ele in dic_keys:
		initialBox.add_element(ele)

	lis_box  = []
	lis_box.append(initialBox)
	it = 0
	while(it+1<k):
		print("Cut :", it)
		box1,box2 = medianCut(lis_box[it])
		lis_box.append(box1)
		lis_box.append(box2)
		it += 1

	return lis_box[it:]

def cal_avg(lis_box):
	lis_avg = []
	for ele in lis_box:
		new_avg = [0,0,0]
		for k in range(len(ele.points)):
			new_avg[0] += ele.points[k][0]
			new_avg[1] += ele.points[k][1]
			new_avg[2] += ele.points[k][2]
		new_avg[0] = int(new_avg[0]/len(ele.points))
		new_avg[1] = int(new_avg[1]/len(ele.points))
		new_avg[2] = int(new_avg[2]/len(ele.points))
		lis_avg.append(new_avg)
	return lis_avg

def cal_dist(p1,p2):
	val = 0
	for i in range(3):
		val += (int(p1[i]) - int(p2[i]))*(int(p1[i]) - int(p2[i]))
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

def make_dic(img):
	dic = {} 
	for i in range(len(img)):
		for j in range(len(img[0])):
			if((img[i][j][0], img[i][j][1], img[i][j][2]) in dic):
				dic[(img[i][j][0], img[i][j][1], img[i][j][2])] += 1
			else:
				dic[(img[i][j][0], img[i][j][1], img[i][j][2])] = 1

	return dic

def pop_sort(dic,ki):
	lis = sorted(dic, key=lambda k: dic[k], reverse = True)

	return lis[0:ki]

def normalize(x):
	return x/255.0

def add_error(x,y,z):
	return tuple(map(lambda x : x[0]+z*x[1], zip(x,y)))

if(len(sys.argv)!=6):
	print("Required -> python quantization.py <input_image> <algo_code> <algo_parameter> <include_dithering> <output_image>")
	print("Popularity Algorithm -> 1")
	print("Median Cut Algorithm -> 2")
	exit()

img = cv.imread(sys.argv[1])

img = np.array(img)

dic = make_dic(img)

if(int(sys.argv[2])==1):
	lis = pop_sort(dic, int(sys.argv[3]))
else:
	lis1 = completeMedianCut(dic.keys(), int(sys.argv[3]))
	lis = cal_avg(lis1)

bool_dither = int(sys.argv[4])

new_img = np.zeros((len(img),len(img[0]),3))
for i in range(len(img)):
	print("Conversion :", i, "out of", len(img))
	for j in range(len(img[0])):
		point = (img[i][j][0],img[i][j][1],img[i][j][2])
		#print(point)
		cl_pt = find_close(point,lis)
		#print(cl_pt)
		new_img[i][j] = tuple(cl_pt)
		if(bool_dither!=0):
			err = tuple(map(lambda x : int(x[0])-int(x[1]), zip(point,cl_pt)))
			#print(err)
			if (j+1)<len(img[0]):
				img[i][j+1] = add_error(img[i][j+1],err,3/8)
			if (i+1)<len(img):
				img[i+1][j] = add_error(img[i+1][j],err,3/8)
			if (i+1)<len(img) and (j+1)<len(img[0]):
				img[i+1][j+1] = add_error(img[i+1][j+1],err,1/4)

cv.imwrite(sys.argv[5], new_img)
