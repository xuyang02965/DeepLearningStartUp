# coding=utf-8

import numpy as np

def setZeroIfLittle(a):
    if a < 0:
        return 0
    else:
        return a

sampleNum = 100
mu = 0
sigma = 1

np.random.seed(0)
s = np.random.normal(mu, sigma, sampleNum)
print (s)

vfunc = np.vectorize(setZeroIfLittle)
s1 = vfunc(s)
print (s1)
