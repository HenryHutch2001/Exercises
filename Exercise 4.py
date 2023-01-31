#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 13:20:35 2023

@author: henryhutchings
"""
import numpy as np
import matplotlib.pyplot as plt
import random

r = np.array([])

for i in range(20):
    num = np.random.normal(1,9)
    r = np.append(r,num)
    
print(r)



