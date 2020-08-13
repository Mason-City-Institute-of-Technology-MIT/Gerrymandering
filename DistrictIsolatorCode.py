# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:09:44 2020

@author: Mason
"""
'''
the objective of this code is to take an inputed image from the wikipedia page of a state congresional district
and eliminate all of  background map and color so that it can be fed into a nueral net
'''
### need to find a way to eliminate second map

#imports required librarys
import cv2
import numpy as np


for i in range(19,23):
    
    #opens desired image (would need loop in final version to run through all files)
    '''
    need to look at data names to ensure matching with TB's Code
    '''
    
    img = cv2.imread('P:\Python Projects\MIT\SheetPicData\PicNotGerry\%s.png' %str(i), cv2.IMREAD_COLOR)
    #cv2.rectangle(img, (1030,0), (1920,911),(), -1 )
    cropped_img = img[0:, 0:800]

    #converts format of image to HSV from RGB (supposedly faster and higher quality *taken at facevalue, not factchecked*)
    hsv = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2HSV)

    #ajusts color screens to filter out desired color
    lower_green= np.array([70,85,85])
    upper_green= np.array([100,250,200])

    #filters out all color that is not within the specified range above
    mask = cv2.inRange(hsv, lower_green, upper_green)

    #runs an edge identifyer that attempts to remove everything thats not an edge (the numbers affect the scale it affects)
    edges = cv2.Canny(mask, 600,600)


    #prints images to screen (original image, the mask, the edges)
    #because the edges are all that is needed, it is printed
    cv2.imshow('img', img)
    cv2.imshow('mask', mask)
    cv2.imshow('edges', edges)
    #cv2.imshow('cropped', cropped_img)


    #waits until any key is pressed
    cv2.waitKey(0)
    #removes all opened images
    cv2.destroyAllWindows()
    dimensions = img.shape
    print(dimensions)
    print(edges.shape)
    print(i)
    cv2.imwrite('P:\Python Projects\MIT\SheetPicData\EdgesNotGerry\%s.png' %str(i), edges)

'''
#these are other filtering functions that I messed around with, interesting but unnecisary
erode = cv2.erode(mask, None, iterations = 20)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
edges = cv2.Canny(mask, 900,500)

cv2.imshow("test", erode)
cv2.imshow('deepfry', laplacian)
cv2.imshow('edges', edges)
'''
'''
#LINEDRAWINGTEST REGION 
cv2.rectangle(img, (1030,0), (1920,911),(), -1 )

cv2.imshow('imagewithline', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
need to loop through downloaded images, crop, edge detect, save as black and white
then upload to drive
'''


























































