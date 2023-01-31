#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 13:20:35 2023

@author: henryhutchings
"""
import numpy as np
import matplotlib.pyplot as plt
import random



r = np.random.normal(5,3,20)

    


idx = r < 5
print(idx)
"Displays a boolean output for each entry in the array explaining whether the entry is less than 5, if true we print 'true', else print 'false'"

r[idx] = 0



