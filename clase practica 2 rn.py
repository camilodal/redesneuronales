#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:31:31 2023

@author: clinux01
"""

import numpy as np
from matplotlib import pyplot as mpl


p=1
n=10
m=15
N=0.01


x=np.random.uniform(-5, 5, (p, n+1))
a=np.random.uniform(-2, 2, (n+1, m))
z=np.random.uniform(-3, 3, (p, m))

w=np.random.normal(0, 0.1, (n+1, m))
y= np.dot(x, w)
d=z-y
delta_w=np.dot(x.T, d)
w=w + N * delta_w

i=1
e=[]
while np.sum(np.square(d))>0.0000000000000000000001 and i<99:
        y= np.dot(x, w)
        d=z-y
        delta_w=np.dot(x.T, d)
        w=w + N * delta_w
        i=i+1
        e.append(np.sum(np.square(d)))
        print(np.sum(np.square(d)))
        
graf=np.arange(1,i)
mpl.plot(graf, e)


## EJ 1 de la práctica 

xp = np.array( [ [ -1, -1 ],
[ -1, +1 ],
[ +1, -1 ],
[ +1, +1 ] ] )
    
z = np.array( [ [ -1, -1 ],
[ -1, +1 ],
[ -1, +1 ],
[ +1, +1 ] ] )

x = np.concatenate((xp, np.ones((4,1))), axis=1)    

    
w=np.random.binomial(1, 0.5, (3, 2))
y= np.sign(np.dot(x, w))
d=z-y
delta_w=np.dot(x.T, d)
w=w + N * delta_w

i=1
e=[]
while np.sum(np.square(d))>0.001 and i<99:
        y= np.sign(np.dot(x, w))
        d=z-y
        delta_w=np.dot(x.T, d)
        w=w + N * delta_w
        i=i+1
        e.append(np.sum(np.square(d)))
        print(np.sum(np.square(d)))
        
        
graf=np.arange(1,i)
mpl.plot(graf, e)


