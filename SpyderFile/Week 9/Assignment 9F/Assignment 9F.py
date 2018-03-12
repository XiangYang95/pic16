# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 21:10:25 2018

@author: Lenovo
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('frame.png',0)
img2 = img.copy()
template = cv.imread('hip.png',0)
w, h = template.shape[::-1]

method = eval("cv.TM_CCORR_NORMED")

res = cv.matchTemplate(img,template,method)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv.rectangle(img,top_left, bottom_right, 255, 2)

#plt.imshow(img)

cap = cv.VideoCapture("RyanRun.MP4")

global nthFrame
global coor

nthFrame = 0
coor = []
while(True):
    # Capture frame-by-frame
    frame = cap.grab()
    nthFrame += 1
    if nthFrame > 870 and nthFrame < 1083:

        ret, frame = cap.retrieve(frame)

        # Our operations on the frame come here
        grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
        res = cv.matchTemplate(grayframe,template,method)
        if nthFrame == 871:
            res = cv.matchTemplate(grayframe,template,method)
        
        else:
            res = cv.matchTemplate(grayframe[top_left[0]-w: top_left[0]+2*w, top_left[1]-h, top_left[1]+2*h]
            ,template,method)
        
        
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        
        top_left = max_loc
        
        bottom_right = (top_left[0] + w, top_left[1] + h)
        print grayframe
        print top_left
        print bottom_right
        cv.rectangle(grayframe,top_left, bottom_right, 255, 2)
        
        # Display the resulting frame
        cv.imshow('frame', grayframe)
        
        coor.append(top_left)
        
        if cv.waitKey(1) & 0xFF == ord('q') or nthFrame >= 1082:
            break
        
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

frameListX = [coordinate[0] for coordinate in coor]
frameListY = [-coordinate[1] for coordinate in coor]
plt.plot(np.array(frameListX), np.array(frameListY))





# =============================================================================
#         if nthFrame == 871:
#             previousFrame = grayframe
#             res = cv.matchTemplate(grayframe,template,method)
#         
#         else:
#             res = cv.matchTemplate(grayframe,template,method, previousFrame)
#             previousFrame = grayframe
#         
#         min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# =============================================================================
