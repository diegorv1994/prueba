# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 00:51:01 2019

@author: diego
"""
armas = ['pistola','escopeta']
cargadores = {'pistola': [10, 10], 'escopeta': [2, 2, 2, 2, 2]}

# your code
total=0
for i in range(0,len(armas)):
    r=armas[i]
    numerocar=cargadores[r]
    total=total+sum(numerocar)
print(total)

armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']###

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17], 
    'ametralladora': [33, 40], 
    'escopeta': [2, 2, 2, 1], 
    'fusil de francotirador': [1, 2, 4]
}

# your code
total=0
for i in range(0,len(armas)):
    r=armas[i]
    numerocar=cargadores[r]
    total=total+sum(numerocar)
print(total)
    
armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17], 
    'ametralladora': [33, 40], 
    'escopeta': [2, 2, 2, 1], 
    'fusil de francotirador': [1, 2, 4], 
    'bazoka': [1, 1]
}

# your code
total=0
for i in range(0,len(armas)):
    r=armas[i]
    numerocar=cargadores[r]
    total=total+sum(numerocar)
print(total)
    
armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17], 
    'ametralladora': [33, 40], 
    'escopeta': [2, 2, 2, 1] 
}

# your code
total=0
for i in range(0,len(cargadores)):
    r=armas[i]
    numerocar=cargadores[r]
    total=total+sum(numerocar)
print(total)
a=sum([12, 13, 4, 5, 20, 17])
b=sum([33,40])
c=sum([2,2,2,1])
d=a+b+c





