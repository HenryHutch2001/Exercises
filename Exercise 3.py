#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:39:40 2023

@author: henryhutchings
"""

import numpy as np 

a = np.array([5, 4, 9, 2, 0, 4, 7, 2])
print(a[-1])

print(a[1:6])
"Printing indexes 1-6 selects the second element in the array and prints each element up until the 7th, python indexing starts at 0"

print(a[:-2])
"Prints the every array element before the second to last element"

print(a[::2])
"Prints every other element in the array"

b = np.array([5, 4, 9, 2, 0, 4, 7, -9])

print(b)

b[0:3] = 1

print(b)
"Changes every element in the array from index 0-3 to a '1' "