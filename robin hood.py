# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 16:34:11 2019

@author: diego
"""
import numpy as np
points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]
# 1. Robin Hood is famous for hitting an arrow with another arrow. Did you get it?
points_test = points[:]
unique_values = set(points_test)
if len(unique_values) < len(points_test):
    print(True)
else:
    print("Robin Hood didn't make it this time.")
x1=0
x2=0
x3=0
x4=0
c=0
dv=np.zeros((22, 1))
for i in range(0, len(points)):
    if points[i][0]>0 and points[i][1]>0:
        x1=x1+1
    elif points[i][0]<0 and points[i][1]>0:
        x2=x2+1
    elif points[i][0]>0 and points[i][1]<0:
        x3=x3+1
    elif points[i][0]<0 and points[i][1]<0:
        x4=x4+1
    d=np.sqrt(points[i][0]*points[i][0]+points[i][1]*points[i][1])
    dv[i]=d
    if d>9:
        c=c+1
        print(points[i])
print(c)
mini=min(dv)
x=[x1,x2,x3,x4]
print(x)