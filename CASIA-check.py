import cv2
import os
import sys 
import compare
import random

random_pair=[]
path="D:/cv/ASI-cv/CASIA-FaceV5-160-all"
model="20170512-110547"

def get_imgs_pair(pics):
	img1_num=random.randint(1,len(pics)-1)
	img2_num=random.randint(1,len(pics)-1)
	pair=[img1_num,img2_num]
	pair.sort()
	while (img1_num==img2_num and pair in random_pair):
		img2_num=random.randint(1,len(pics)-1)
		pair=[img1_num,img2_num]
		pair.sort()
	random_pair.append(pair)
	return pair

def evaluate():
	ta=0
	fa=0
	p_same=0
	p_diff=0
	eva_num=100
	eva_round=50 #做40,000次对比  
	pics=os.listdir(path)
	argv=[model]
	img_num=[]
	for j in range(eva_round):
		for i in range(eva_num):
			img1_num,img2_num=get_imgs_pair(pics)
			img1=path+"/"+pics[img1_num]
			img2=path+"/"+pics[img2_num]
			argv.append(img1)
			argv.append(img2)
			img_num.append([img1_num,img2_num])
		dist=compare.get_dist(argv)
		for i in range(eva_num):
			if pics[img_num[i][0]][:3]==pics[img_num[i][1]][:3]:
				p_same=p_same+1
			else:
				p_diff=p_diff+1
			if dist[i]<=1.0 and pics[img_num[i][0]][:3]==pics[img_num[i][1]][:3]:
				ta=ta+1
			if dist[i]<=1.0 and pics[img_num[i][0]][:3]!=pics[img_num[i][1]][:3]:
				fa=fa+1
		print("TA=",ta,"    p_same=",p_same)
		print("FA=",fa,"    p_diff=",p_diff)
		if p_same!=0:
			print("VAL=",ta/p_same)
		else:
			print("p_same=0")
		if p_diff!=0:
			print("FAR=",fa/p_diff)
		else:
			print("p_diff=0")

if __name__ == '__main__':
	evaluate()




'''	
model="20170512-110547"
img1="D:/cv/ASI-cv/CASIA-FaceV5-160-all/0_0.bmp"
img2="D:/cv/ASI-cv/CASIA-FaceV5-160-all/0_2.bmp"
argv=[model,img1,img2]
print(compare.get_dist(argv))
#["20170512-110547","D:/cv/ASI-cv/CASIA-FaceV5-160-all/0_0.bmp","D:/cv/ASI-cv/CASIA-FaceV5-160-all/0_2.bmp"]
'''