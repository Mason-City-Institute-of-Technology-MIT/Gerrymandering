# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 14:27:32 2020

@author: Mason

this program is simply a test of the saving methods Ive been reading about to see
if they will be viable methods for saving the gerrymandered district images and labels 
"""

import numpy as np
import cv2
from numpy import asarray
from numpy import savez_compressed
from numpy import load
from PIL import Image


#initiates an empty array so that later it can be filled with images to be stacked
arraylist = []

#loops for the number of images there are
for i in range(1,47):
    
    #reads in image 
    img = cv2.imread('P:\Python Projects\MIT\SheetPicData\EdgesGerryResized\%s.png' %str(i))
    
    #filters out just one chanel of the 3, the others are not used
    Chosen, garbagelevel, garbagelevel2 = cv2.split(img)
    
    #converts the single channel image into a numpy array
    CurrentImage = asarray(Chosen)
    
    #appends the array to the list initated before loop
    arraylist.append(CurrentImage)
    
    #prints shape of array to ensure that all images are the same size as program is running
    print(CurrentImage.shape)
  
    
#once loop is complete this function stacks all of the images within the list
DataSet = np.stack(arraylist,axis = 2)
#this prints the shape of the entire dataset to be saved
print(DataSet.shape)
#saves as a compressed .npz file 
savez_compressed('P:/Python Projects/MIT/MasonIsAnImageSavingGenius.npz', DataSet)

'''
#this was a test to ensure that the saved images can be opened and all look good

#loads data from file that was just saved
loaddata =load('P:/Python Projects/MIT/MasonIsAnImageSavingGenius.npz')

#Because noname was given in the savez_compressed line this is the auto one to ensure propper data load
DataArray = loaddata['arr_0']


#takes 2D slices from the 3D array and displays them as images
for i in range(1,47):
    CurrentSlice= DataArray[:,:,i]
    LoadedImage = Image.fromarray(CurrentSlice)
    LoadedImage.show()
'''

#Work Log
'''
3:00pm Friday August 7th:
    works to open image, save image as compressed numpy array and then open and convert back
    to photo,
    
    now need to work on opening many images to be saved within one 3d array to determin if 
    this is a reasonable way to feed data into the network
    
4:22pm Friday August 7th:
    Can save Images as compressed numpy arrays, and then open them for use.
    
    Now need to redo where the images come from (edges not color), transform them
    to black and white and retry to ensure that no edge detail is lost

5:17 Thursday August 13th
    Wrote a second code that makes all of the inputed images squares of the same size
    by adding black borders on the edges of the smaller ones, also cut out the color chanels so that 
    the image is only saving a 3D array instead of a 4D array.
    
    Need to make sure that the labels can be translated in the same order, as well as upload this to
    gethub
'''

















































