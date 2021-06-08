import numpy as np
import cv2

img = cv2.imread('dog.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(300,500),(150,150)    ,(255,255,255),15)

cv2.rectangle(img,(115,225),(200,150),(255,0,255),5)

cv2.circle(img,(450,63),55,(0,255,255),-1)

pts=np.array([[200,350],[20,40],[50,295],[55,150],[80,100]],np.int32)
#pts=pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,0),6)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV!!',(300,130),font,1,(255,255,100),5,cv2.LINE_AA)




img[200:450,250:400]=[255,255,255]

watch_face=img[112:250,190:400]
img[0:138,0:210]=watch_face





cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows
