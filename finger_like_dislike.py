# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 00:20:20 2021

@author: Veka
"""

# kütüphaneler tanımlanır
import cv2
import HandTrackingModule as htm
 
wCam, hCam = 640, 480

# iconlarımızı tanımlıyoruz
dislikeIcon = cv2.imread('dislike.png')
likeIcon = cv2.imread('like.png')

# cameranın nereden alınacağı ve boyutlarının ne olacağı belirlenir
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
 
detector = htm.handDetector()

 
tipIds = [4, 8, 12, 16, 20] # parmakların en uç kısımları belirlenir
 
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img) # algıladı videoda el olup olmadığını algılar
    # print(lmList)
    # parmakların kordinatları işaretlere göre uyarlanır
    if len(lmList) != 0:
        if lmList[tipIds[0]][2] > lmList[tipIds[4] - 1][2]:
            if lmList[tipIds[1]][1] < lmList[tipIds[1] - 2][1]:
                if lmList[tipIds[2]][1] < lmList[tipIds[2] - 2][1]:
                    if lmList[tipIds[3]][1] < lmList[tipIds[3] - 2][1]:
                        if lmList[tipIds[4]][1] < lmList[tipIds[4] - 2][1]:
                            img[0:190, 0:150] = dislikeIcon
        
        elif lmList[tipIds[0]][2] < lmList[tipIds[4] - 1][2]:
            if lmList[tipIds[1]][1] < lmList[tipIds[1] - 2][1]:
                if lmList[tipIds[2]][1] < lmList[tipIds[2] - 2][1]:
                    if lmList[tipIds[3]][1] < lmList[tipIds[3] - 2][1]:
                        if lmList[tipIds[4]][1] < lmList[tipIds[4] - 2][1]:
                            img[0:190, 0:150] = likeIcon
                            
        else:
            print('detection failed')
 
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()