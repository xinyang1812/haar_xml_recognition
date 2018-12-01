#为了检验生成的.xml的分类效率
# -- coding: UTF-8 --
import cv2
import numpy as np

z_sum = 0
c_sum = 0
face_xml = cv2.CascadeClassifier('C:/Users/7invensun/Downloads/opencv/sources/data/haarcascades/haarcascade_eye.xml')
# eye_xml = cv2.CascadeClassifier('C://Users//7invensun//Downloads//opencv//sources//data//haarcascades//haarcascade_eye.xml')
# 加载文件
# 文件来源：https://juejin.im/post/5afd25b66fb9a07aa34a775f
list = 'C:/Users/7invensun/PycharmProjects/PictureTailoring/bg.txt'
fp = open(list,'r')
lines = fp.readlines()
fp.close()
for line in lines:
    path = line.split('\n')
    img = cv2.imread(path[0])
    z_sum = z_sum + 1
#cv2.imshow('src', img)
# 打印图片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 进行灰色处理
    faces = face_xml.detectMultiScale(gray, 1.3, 5)
# 检测出图片的待检测物
    print('eye=', len(faces))
# 打印检测出了多少个待检测物
    for (x, y, w, h) in faces:
         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
         roi_face = gray[y:y + h, x:x + w]
         roi_color = img[y:y + h, x:x + w]
         c_sum =c_sum + 1
         cv2.imshow('dst', img)
         cv2.waitKey(100)

cv2.destroyAllWindows()
print ('测试总数：'+ str(z_sum))
print ('识别数：'+ str(c_sum))
print('percent: {:.2%}'.format(float(c_sum)/float(z_sum)))