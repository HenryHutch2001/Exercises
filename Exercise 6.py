#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 13:27:48 2023

@author: henryhutchings
"""
import numpy as np
import math
import matplotlib.pyplot as plt

t = np.linspace(0,5,50)

y = []

print(len(t))
"print(t)"

for i in t:
    output = (i**2)*math.exp(-2*i)
    y.append(output)
    if output == max(y):
        maxt = i
    else:
        continue

print(max(y))
print(maxt)


plt.plot(t,y, color = 'red')
plt.xlabel('t')
plt.ylabel('y')
plt.title('A graph of the relationship between t and y(t)')
plt.show()



