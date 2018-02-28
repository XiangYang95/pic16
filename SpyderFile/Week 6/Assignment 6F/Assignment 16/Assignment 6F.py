# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 00:45:11 2018

@author: Xiang Yang Ng
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

import numpy as np

imgA = mpimg.imread("a.jpg")

imgB = mpimg.imread("b.jpg")

print imgA.shape, imgB.shape

img3 = np.concatenate((imgA[250:650,0:100,:],imgB, imgA[250:650,500:,:]), axis = 1)

img4 = np.concatenate((imgA[:250,:,:],img3,imgA[650:,:,:]), axis = 0)

plt.imshow(img4)
plt.imsave("c.jpg", img4)

#%%
imgG = mpimg.imread('g.jpg')
imgGC = imgG.copy()
imgGC = imgGC.astype("float32")

imgH = mpimg.imread('h.jpg')
imgHC = imgH.copy()
imgHC = imgHC.astype("float32")

imgHC2 = imgH.copy()

for i in range(430):
    for j in range(400):
        if abs(imgHC[i,j,0] - imgGC[i,j,0]) < 20 and abs(imgHC[i,j,1] - imgGC[i,j,1]) < 20 and abs(imgHC[i,j,2] - imgGC[i,j,2]) < 20:
            imgHC2[i,j,0] = 0
            imgHC2[i,j,1] = 0
            imgHC2[i,j,2] = 0

plt.imshow(imgHC2)
plt.imsave("i.jpg", imgHC2)

#%%
imgE = mpimg.imread("e.jpg")

imgEC = imgE.copy()
imgEC[np.logical_and(imgEC[:,:,0] < 50, imgEC[:,:,1] > 225, imgEC[:,:,2] < 40)] = 0

imgD = mpimg.imread("d.jpg")
imgDC = imgD.copy()

#589:,300:465
for i in range(591, 751):
    for j in range(301,466):
        if imgEC[i-591, j-301, 0] != 0 and imgEC[i-591, j-301, 1] != 0 and imgEC[i-591, j-301, 2] != 0:
            imgDC[i,j,:] = imgEC[i-591, j-301,:]
            

plt.imshow(imgDC)
plt.imsave("f.jpg", imgDC)


