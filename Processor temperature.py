# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:33:10 2019

@author: diego
"""
# import
import matplotlib.pyplot as plt
#matplotlib inline
import numpy as np
# axis x, axis y
y = [33,66,65,0,59,60,62,64,70,76,80,81,80,83,90,79,61,53,50,49,53,48,45,39]
x = list(range(len(y)))

# plot
plt.plot(x, y)
plt.axhline(y=70, linewidth=1, color='r')
plt.xlabel('hours')
plt.ylabel('Temperature ºC')
plt.title('Temperatures of our server throughout the day')

# assign a variable to the list of temperatures
temperatures_C = [33,66,65,0,59,60,62,64,70,76,80,81,80,83,90,79,61,53,50,49,53,48,45,39]

# 1. Calculate the minimum of the list and print the value using print()
print(min(temperatures_C))

# 2. Calculate the maximum of the list and print the value using print()
print(max(temperatures_C))

# 3. Items in the list that are greater than 70ºC and print the result
f=[]
for i in range(0, len(temperatures_C)):
    if temperatures_C[i]>70:
        f.append(temperatures_C[i])
print(f)
# 4. Calculate the mean temperature throughout the day and print the result
prome=sum(temperatures_C)/len(temperatures_C)

# 5.1 Solve the fault in the sensor by estimating a value
temperatures_C[3]=(temperatures_C[4]+temperatures_C[2])/2

# 5.2 Update of the estimated value at 03:00 on the list
print(temperatures_C)

temperatures_F=[0]*24

for i in range(0,len(temperatures_C)):
    temperatures_F[i]= 1.8*temperatures_C[i]+32
print(temperatures_F)

peligro=0
for i in range(0,len(temperatures_C)):
    if temperatures_C[i]>=70:
        peligro=peligro+1
    elif temperatures_C[i]>80:
        peligro=4
    elif sum(temperatures_C[:])/len(temperatures_C)>65:
        peligro=4
if peligro>=4:
    print("True")
    
# 1. We want the hours (not the temperatures) whose temperature exceeds 70ºC
j=[]
for i in range(0,len(temperatures_C)):
    if temperatures_C[i]>70:
        j.append(i)

proC=sum(temperatures_C[:])/len(temperatures_C)
proF=sum(temperatures_F[:])/len(temperatures_F)
print(proC)
print(proF)

devc=0
devf=0

for i in range(0, len(temperatures_C)):
    devc=devc+(temperatures_C[i]-proC)*(temperatures_C[i]-proC)
    devf=devf+(temperatures_F[i]-proF)*(temperatures_F[i]-proF)
devc=np.sqrt(devc/(len(temperatures_C)))
devf=np.sqrt(devf/(len(temperatures_F)))
print(devc)
print(devf)
print("1.8*proC+32")
print("1.8*devc")
print(1.8*proC+32)
print(1.8*devc)








