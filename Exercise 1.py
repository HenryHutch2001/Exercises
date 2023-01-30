# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from math import pi

N = 2000
PiSum = 0


def function(n):
    a = ((4*n)+1)
    b = ((4*n)+3)
    ab = a*b
    PiSum = 8/ab
    return PiSum



for i in range(N):
    PiSum += function(i)
    error = abs(pi - PiSum)
    if error > 10^-7:
        N = N+1
    else:
        pass

print(error)
print(N)
print(PiSum)







