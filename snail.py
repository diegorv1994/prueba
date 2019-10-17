# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:24:06 2019

@author: diego
"""
#"A snail falls at the bottom of a 125 cm well. Each day the snail rises 30 cm."
# "But at night, while sleeping, slides 20 cm because the walls are wet."
 #"How many days does it take to escape from the well?"
# Assign problem data to variables with representative names
# well height, daily advance, night retreat, accumulated distance
w=30
s=20
x=0

# Assign 0 to the variable that represents the solution
days=0

# Write the code that solves the problem
while x<125: 
    x=x+w
    days=days+1
    if x<125:
        x=x-s
    else:
        # Print the result with print('Days =', days)
        print('Days =', days)
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
# Assign problem data to variables with representative names
# well height, daily advance, night retreat, accumulated distance
s=20
x=0

# Assign 0 to the variable that represents the solution
days=0

# Write the code that solves the problem
while x<125: 
    x=x+advance_cm[days]
    print(x)
    days=days+1
    if x<125:
        x=x-s
        print(x)
    else:
        # Print the result with print('Days =', days)
        print('Days =', days)

