# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 23:02:31 2018

@author: Lenovo
"""

import cv2 as cv
# Load an color image in color
img = cv.imread('messi.jpg',cv.IMREAD_COLOR)

import numpy as np
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()