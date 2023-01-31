#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 13:59:45 2023

@author: henryhutchings
"""

import numpy as np
import matplotlib.pyplot as plt
import math 

A = np.array([[1,-1],[2,4],[1,1],[3,8]])




def psuedoinverse(A):
    Aplus = np.linalg.pinv(A)
    print(Aplus)
    return Aplus



I = np.matmul(psuedoinverse(A),A)
print(I)