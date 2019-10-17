# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 12:24:06 2019

@author: diego
"""
import numpy as np
# variables
stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1),
         (1, 5), (5, 8), (4, 6), (2, 3)]

# 1. Calculate the number of stops.
ma=len(stops)

# 2. Assign a variable a list whose elements 
#are the number of passengers in each stop: 
# Each item depends on the previous item in the list + in - out.
lis=[0,0,0,0,0,0,0,0,0]
x=0
prevx=0
for i in range(0, len(stops)):
    prevx=stops[i][0]-stops[i][1]
    x=prevx+x
    lis[i]=x
maxi=max(lis)
promedio=sum(lis)/len(lis)
dev=0
for i in range(0, len(lis)):
    dev=dev+(lis[i]-promedio)*(lis[i]-promedio)
dev=np.sqrt(dev/(len(lis)))
print(promedio)
print(dev)