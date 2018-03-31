# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 13:40:16 2018

@author: yang0407
"""

import cv2 as cv

from sklearn.svm import LinearSVC as LSVC

import numpy as np

def boundaries(binarized,axis):
    # variables named assuming axis = 0; algorithm valid for axis=1
    # [1,0][axis] effectively swaps axes for summing
    rows = np.sum(binarized,axis = [1,0][axis]) > 0
    rows[1:] = np.logical_xor(rows[1:], rows[:-1])
    change = np.nonzero(rows)[0]
    ymin = change[::2]
    ymax = change[1::2]
    height = ymax-ymin
    too_small = 10 # real letters will be bigger than 10px by 10px
    ymin = ymin[height>too_small]
    ymax = ymax[height>too_small]
    return zip(ymin,ymax)

def separate(img):
    orig_img = img.copy()
    pure_white = 255.
    white = np.max(img)
    black = np.min(img)
    thresh = (white+black)/2.0
    binarized = img<thresh
    row_bounds = boundaries(binarized, axis = 0) 
    cropped = []
    for r1,r2 in row_bounds:
        img = binarized[r1:r2,:]
        col_bounds = boundaries(img,axis=1)
        rects = [r1,r2,col_bounds[0][0],col_bounds[0][1]]
        cropped.append(np.array(orig_img[rects[0]:rects[1],rects[2]:rects[3]]/pure_white))
    return cropped

    
alphabets = ["a", "b", "c"]
large_imgs = [cv.imread("{}.png".format(i), 0) for i in alphabets]

large_imgs = [separate(large_img) for large_img in large_imgs]
small_imgs = []#will contain all 69 images/samples
for large_img in large_imgs:#3 elements
    print len(large_img)
    for small_img in large_img:#23 each
        small_imgs.append(small_img)

#resized final data        
data = np.array([cv.resize(small_img, (5,5)) for small_img in small_imgs])
print data.shape
target = [1 for i in data]
target[24:46] = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
target[46:] = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
target = np.array(target)
train_data, train_target, test_data, test_target = Partition(data, target, 0.8)
clf = LSVC()
clf.fit(train_data, train_target)
predicted_target = clf.predict(test_data)
percentage = sum(predicted_target == test_target)*1.0/len(test_target)
print "Predicted: ", "{}".format(predicted_target)
print "Truth: ", "{}".format(test_target)
print "Percentage: ", percentage

        
    #data_img_a = np.array(img_a).reshape((noOfCols, noOfRows))    
    
def Partition(data, target, p): 
    l = len(data)
    m = int(p*l)

    train_i = np.arange(m)
    train_i = np.random.permutation(train_i)
    
    all_i = np.arange(l)
    all_i[train_i] = -1
    test_i = all_i[all_i > -1]
    print train_i
    print test_i
    train_data = data[train_i]
    train_target = target[train_i]
    test_data = data[test_i]
    test_target = target[test_i]
    print target,test_target
    return train_data, train_target, test_data, test_target


if __name__ == "__main__":
    Main()