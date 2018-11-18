
import cv2
import os

def changeto160(window_name):
    #cv2.namedWindow(window_name)
    classfier = cv2.CascadeClassifier("D:/cv/ASI-cv/opencv-classifier/haarcascades/haarcascade_frontalface_alt2.xml")
    for i in range(500):
        if i<10 :
            url="D:/cv/ASI-cv/CASIA-FaceV5/00"
            url=url+str(i)    
        elif i<100:
            url="D:/cv/ASI-cv/CASIA-FaceV5/0"
            url=url+str(i)  
        else :
            url="D:/cv/ASI-cv/CASIA-FaceV5/"
            url=url+str(i)
        color = (0, 0, 255)        
        pics=os.listdir(url)
        num=0
        for pic in pics:
            road=url+"/"+pic
            imgs = cv2.imread(road)
            #cv2.imshow(window_name, imgs)
            #cv2.waitKey(100)
            grey = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY)
            faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (128, 128))
            sp_x=imgs.shape[0]
            sp_y=imgs.shape[1]
            
            if len(faceRects) > 0:
                for faceRect in faceRects:
                    x, y, w, h = faceRect
                    y1=0
                    x1=0
                    yh=0
                    xw=0
                    if y-50>=0:
                        y1=y-50
                    else:
                        y1=0
                    if y+h+50<sp_y:
                        yh=y+h+50
                    else:
                        yh=sp_y
                    if x-50>=0:
                        x1=x-50
                    else:
                        x1=0
                    if x+w+50<sp_x:
                        xw=x+w+50
                    else:
                        xw=sp_x
                    imgs_crop = imgs[y1:yh, x1:xw]
                    imgs_crop = cv2.resize(imgs_crop, (160,160),interpolation=cv2.INTER_LINEAR)
                    #cv2.imshow(window_name, imgs_crop)
                    #cv2.waitKey(0)  
                    saveroad=url[:25]+"-160-all"   
                    if not os.path.exists(saveroad):
                        os.makedirs(saveroad)
                    save_num=pic[:4]
                    saveroad=saveroad+"/"+save_num+str(num)+".bmp"
                    num=num+1
                    cv2.imwrite(saveroad, imgs_crop)
            else:
                print(road)
                    

'''
    color = (0, 0, 255)
    imgs = cv2.imread("D:/cv/ASI-cv/001_1.bmp")  
    grey = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY)   
    cv2.imwrite("D:/cv/ASI-cv/grey.bmp", grey)   
    #人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
    faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (128, 128))
    if len(faceRects) > 0:            #大于0则检测到人脸                                   
        for faceRect in faceRects:  #单独框出每一张人脸
            x, y, w, h = faceRect        
            cv2.rectangle(imgs, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
            print(x,y,w,h)
            imgs_crop = imgs[y-30:y+h+30, x-30:x+w+30]
            imgs_crop = cv2.resize(imgs_crop, (160,160),interpolation=cv2.INTER_LINEAR)

    #cv2.imshow(window_name, imgs)   
    cv2.imwrite("D:/cv/ASI-cv/001_1_rec.bmp", imgs)   
    cv2.imshow(window_name, imgs_crop)   
    cv2.waitKey(0)  
    #cv2.destroyAllWindows() 
'''
if __name__ == '__main__':

    changeto160("cv160")

