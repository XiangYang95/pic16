# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:42:19 2018

@author: harsh
"""
from sklearn import svm
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imread,imresize
import cv2

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

Key = ["A","B","C","D","E","G","H","J","K","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Example usage
a_big_img = imread("A.png", flatten = True)
b_big_img = imread("B.png", flatten = True)
c_big_img = imread("C.png", flatten = True)
d_big_img = imread("D.png", flatten = True)
e_big_img = imread("E.png", flatten = True)
f_big_img = imread("F.png", flatten = True)
g_big_img = imread("G.png", flatten = True)
h_big_img = imread("H.png", flatten = True)
#i_big_img = imread("I.png", flatten = True)
j_big_img = imread("J.png", flatten = True)
k_big_img = imread("K.png", flatten = True)
l_big_img = imread("L.png", flatten = True)
m_big_img = imread("M.png", flatten = True)
n_big_img = imread("N.png", flatten = True)
o_big_img = imread("O.png", flatten = True)
p_big_img = imread("P.png", flatten = True)
q_big_img = imread("Q.png", flatten = True)
r_big_img = imread("R.png", flatten = True)
s_big_img = imread("S.png", flatten = True)
t_big_img = imread("T.png", flatten = True)
u_big_img = imread("U.png", flatten = True)
v_big_img = imread("V.png", flatten = True)
w_big_img = imread("W.png", flatten = True)
x_big_img = imread("X.png", flatten = True)
y_big_img = imread("Y.png", flatten = True)
z_big_img = imread("Z.png", flatten = True)


 # flatten = True converts to grayscale
#cv2.imshow("a",b_big_img/255)
#cv2.waitKey(1000)
#cv2.destroyAllWindows()

a_imgs = separate(a_big_img)
b_imgs = separate(b_big_img)
c_imgs = separate(c_big_img)
d_imgs = separate(d_big_img)
e_imgs = separate(e_big_img)
#f_imgs = separate(f_big_img)
g_imgs = separate(g_big_img)
h_imgs = separate(h_big_img)
#i_imgs = separate(i_big_img)
j_imgs = separate(j_big_img)
k_imgs = separate(k_big_img)
#l_imgs = separate(l_big_img)
m_imgs = separate(m_big_img)
n_imgs = separate(n_big_img)
o_imgs = separate(o_big_img)
p_imgs = separate(p_big_img)
q_imgs = separate(q_big_img)
r_imgs = separate(r_big_img)
s_imgs = separate(s_big_img)
t_imgs = separate(t_big_img)
u_imgs = separate(u_big_img)
v_imgs = separate(v_big_img)
w_imgs = separate(w_big_img)
x_imgs = separate(x_big_img)
y_imgs = separate(y_big_img)
z_imgs = separate(z_big_img)



ALL_IMG = a_imgs+b_imgs+c_imgs+d_imgs+e_imgs  +g_imgs +h_imgs  +j_imgs +k_imgs +m_imgs +n_imgs+o_imgs+p_imgs+q_imgs+r_imgs+s_imgs+t_imgs+u_imgs+v_imgs+w_imgs+x_imgs+y_imgs+z_imgs

ALL_IMG2 = []

for img in ALL_IMG:
    img2 = imresize(img,(5,5))
    ALL_IMG2.append(img2)

ALL_IMG = ALL_IMG2[:]
del ALL_IMG2


## # separates big_img (pure white = 255) into array of little images (pure white = 1.0)
for img in ALL_IMG:
    cv2.imshow("a",img) 
    cv2.waitKey(250)
cv2.destroyAllWindows()



#Define a = 0
#b = 1,....

#Import Data
a_imgs = ALL_IMG


Data = []

for img in a_imgs:
    Data.append(np.reshape(img,(1,25)))

Data = np.array(Data)
Data = np.reshape(Data,(len(ALL_IMG),25))

Target = range(23)*10
Target  = np.array(Target)
Target = np.sort(Target)



def partition(Data,Target,p):
    l = int(Data.shape[0])
    m = int(p*l)
    train_i = np.random.choice(l,m, False)

    all_i = np.arange(l)
    all_i[train_i] = -1
    test_i = all_i[all_i > -1]

    train_data = Data[train_i,:]
    train_target = Target[train_i]
    test_data = Data[test_i]
    test_target = Target[test_i]
    
    
    return l,m,train_data,train_target,test_data,test_target


l,m,train_data,train_target,test_data,test_target = partition(Data,Target,0.9)


###USING LINEAR LEARNING
clf1 = LinearSVC(random_state=0)
clf1.fit(train_data,train_target)
clf1.predict(test_data)

print "Predicted:",clf1.predict(test_data)
print "Truth : ",test_target
accuracy = sum(clf1.predict(test_data)==test_target)*100/(l-m)
print "Accuracy: ",accuracy
#WORKS IN MOST CASES



##USING REGULAR SVM

##WORKS FOR VERY SMALL GAMMA
clf = svm.SVC(gamma = 0.00001)#WORKS
#clf = svm.SVC(gamma = 0.1)#DOESNT WORK
clf.fit(train_data,train_target)
clf.predict(test_data)



print "Predicted:",clf.predict(test_data)
print "Truth : ",test_target
accuracy = sum(clf.predict(test_data)==test_target)*100/(l-m)
print "Accuracy: ",accuracy


##############TEST ACTUAL HANDWRITING
test_img = imread("test.png",flatten = True)
test_img = separate(test_img)

Test_Data = []
for img in test_img:
    cv2.imshow("a",img) 
    cv2.waitKey(250)

    img = imresize(img,(5,5))
    img = np.reshape(img,(1,25))
    Test_Data.append(img)

cv2.destroyAllWindows()   

Test_Data = np.reshape(Test_Data,(len(Test_Data),25))


clf3 = LinearSVC(random_state=0)
clf3.fit(Data,Target)
ans  = clf3.predict(Test_Data)

for i in ans:
    print Key[i]
