# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 14:52:51 2020

@author: Mason
"""
'''the objective of this code is to add black space around the existing images
that we created in earlier sessions to normalize the size and shape of the images
so that they can be stacked and fed into the nueral net easily and efficiently'''

import numpy as np
import cv2


#loops for the number of images
for i in range(1,47):
    #reads image into Open CV
    img = cv2.imread('P:\Python Projects\MIT\SheetPicData\EdgesGerry/%s.PNG' %str(i))
    #Splits image into color Channels (2 are discarded)
    b,g,r = cv2.split(img)
    #takes one color chanel and reads the width and height
    w, h = b.shape
    #determines the difference between the larges image and the current image
    topadd = 1194 - w
    sideadd = 1194 - h
    #adds the difference in image size to ensure congruent images
    border = cv2.copyMakeBorder(b, top = topadd, bottom = 0, left = sideadd, right = 0, borderType=cv2.BORDER_CONSTANT)
    #prints the shape of the image to ensure it has been normalized
    print(border.shape)
    #prints the current counter so that if there is an issue on one image the image can be determined
    print(i)
    #saves ajusted image
    cv2.imwrite('P:\Python Projects\MIT\SheetPicData\EdgesGerryResized\%s.png' %str(i), border)


#this is the same code jsut for a different folder
for i in range(1,85):
    img = cv2.imread('P:\Python Projects\MIT\SheetPicData\EdgesNotGerry/%s.PNG' %str(i))
    b,g,r = cv2.split(img)
    w, h, = b.shape
    topadd = 1194 - w
    sideadd = 1194 - h
    border = cv2.copyMakeBorder(b, top = topadd, bottom = 0, left = sideadd, right = 0, borderType=cv2.BORDER_CONSTANT)
    print(border.shape)
    print(i)
    cv2.imwrite('P:\Python Projects\MIT\SheetPicData\EdgesNotGerryResized\%s.png' %str(i), border)


'''
Nice, all images are the same size now!!!
'''