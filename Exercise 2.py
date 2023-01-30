#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 11:38:39 2023

@author: henryhutchings
"""
a = [1, 2, 3]
b = [4, 5, 6]


def dotproduct(a,b):
    N = len(a)
    Ncheck = len(b)
    dot = 0
    for i in range(N):
        dot += a[i]*b[i]
    return dot   
print(dotproduct(a, b))   

A = [[1,2,3],[4,5,6]]

m1 = A[0]
m2 = A[1]
print(m1,m2)


