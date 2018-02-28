# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 01:54:24 2018

@author: Xiang Yang Ng
"""

import matplotlib.pyplot as plp
import numpy as np
import scipy.fftpack as scifft
from scipy.io import wavfile as wf 

rate,data = wf.read("wooguy.wav")

data1 = data[:,0]

data2 = scifft.fft(data1)

data3 = abs(data2)

d = 1.0/rate

n = len(data)

freq = scifft.fftfreq(n,d)

plp.plot(freq, data3)

#%%

data4 = data2.copy()
mask1 = np.logical_and(500 <= freq, freq<= 600)
mask2 = np.logical_and(-500 >= freq, freq>= -600)
#freqmask = np.logical_and(500 <= freq, freq<= 600 or np.logical_and(-500 >= freq, freq>= -600))
freqmask = np.logical_or(mask1, mask2)

data5 = data3.copy()

data5[freqmask] = 0

plp.plot(freq, data5)

data4[freqmask] = 0

data6 = scifft.ifft(data4).astype("int16")

wf.write("wooguymine.wav", rate, data6)
