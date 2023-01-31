#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 13:14:29 2023

@author: henryhutchings
"""
import numpy as np

A = np.array([[1,0,0,0],[1,-2,1,0],[0,1,-2,1],[0,0,0,1]])
b = np.array([[0],[1],[1],[2]])

x = np.linalg.solve(A, b)

print(x)

output = np.matmul(A,x) - b
print(output)
"The system of equations is satisfied as Ax-b = 0 which is consistent"