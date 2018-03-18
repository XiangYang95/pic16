# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 21:10:25 2018

@author: Xiang Yang Ng
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('frame.png',0)
img2 = img.copy()
template = cv.imread('hip.png',0)
w, h = template.shape[::-1]



#first part of the assignment
# =============================================================================
# method = eval("cv.TM_CCOEFF_NORMED")
# res = cv.matchTemplate(img,template,method)
# min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# 
# top_left = max_loc
# bottom_right = (top_left[0] + w, top_left[1] + h)
# 
# cv.rectangle(img,top_left, bottom_right, 255, 2)
# 
# plt.imshow(img)
# =============================================================================

#%%
img = cv.imread('frame.png',0)
template = cv.imread('hip.png',0)
w, h = template.shape[::-1]
method = eval("cv.TM_CCOEFF_NORMED")

cap = cv.VideoCapture("RyanRun.MP4")

global nthFrame
global coor

nthFrame = 0
coor = []


while(True):
    # Capture frame-by-frame
    frame = cap.grab()
    

    
    nthFrame += 1
    if nthFrame > 874 and nthFrame < 1083:

        ret, frame = cap.retrieve(frame)
        
       # w_img, h_img = frame.shape[:2][::-1]
        w_img= frame.shape[1]
        h_img  = frame.shape[0]
            
        # Our operations on the frame come here
        grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
 
        
        if nthFrame < 876:
            res = cv.matchTemplate(grayframe,template,method)  
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
            coor.append(max_loc)
            
        
        else:
            xbound = (np.max([0,x-h]), np.min([x+2*h, w_img]))
            ybound = (np.max([0,y-w]), np.min([y+2*w, h_img]))

            img_small = grayframe[ybound[0]: ybound[1], xbound[0]: xbound[1]]
            res = cv.matchTemplate(img_small, template, method)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
            max_loc = (max_loc[0]+ xbound[0],max_loc[1]+ ybound[0])
            
        top_left = max_loc
        x = top_left[0]
        y = top_left[1]
        bottom_right = (top_left[0] + w, top_left[1] + h)
            


        cv.rectangle(grayframe, top_left, bottom_right, 255, 2)
        
        # Display the resulting frame
        cv.imshow('frame', grayframe)
        
        coor.append(top_left)
        
        if cv.waitKey(10) & 0xFF == ord('q') or nthFrame >= 1082:
            break


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

frameListX = [coordinate[0] for coordinate in coor]
frameListY = [-coordinate[1] for coordinate in coor]
plt.plot(np.array(frameListX), np.array(frameListY))






