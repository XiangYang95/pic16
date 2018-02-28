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

data1 = scifft.fft2(data)

data2 = abs(data1)

d = 1.0/rate

n = len(data)

freq = scifft.fftfreq(n,d)


plp.plot(freq, data2)

#%%

data4 = data2.copy()
mask1 = np.logical_and(500 <= freq, freq<= 600)
mask2 = np.logical_and(-500 >= freq, freq>= -600)
#freqmask = np.logical_and(500 <= freq, freq<= 600 or np.logical_and(-500 >= freq, freq>= -600))
freqmask = np.logical_not(np.logical_or(mask1, mask2))

plp.plot(freq[freqmask], data2[:,freqmask])

data5 = scifft.ifft(data4[freqmask]).astype("int16")

wf.write("wooguymine3.wav", rate, data5)