# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 13:28:34 2019

@author: diego
"""
# Variables

dbs = [0, 1, 0, 0, 0, 0, 1, 0, 1, 23, 1, 0, 1, 1, 0, 0, 0, 
       1, 1, 0, 20, 1, 1, 15, 1, 0, 0, 0, 40, 15, 0, 0]

# Show volumes that exceed 10 dBs
f=[]
fmo=[]
j=0
for i in range(0, len(dbs)):
    if dbs[i]>10:
        f.append(dbs[i])
        fmo.append(i)
obj1 = enumerate(f) 
obj2 = enumerate(fmo)

a=list(obj1)
b=list(obj2)
c = a + b
print(c)    
#[(0, 23), (1, 20), (2, 15), (3, 40), (4, 15),
# (0, 9), (1, 20), (2, 23), (3, 28), (4, 29)]
# [(9, 23), (20, 20), (23, 15), (28, 40), (29, 15)]
print(dbs)
for i in range(0, len(dbs)):
    if dbs[i]>20 and dbs[i]<30:
        dbs[i]=dbs[i]-12
    elif  dbs[i]>30:
        dbs[i]=dbs[i]-18
    else:
        dbs[i]=dbs[i]
print(dbs)
        
        
        
        
        
        
        
        
