# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 01:03:39 2021

@author: Ezxiio
"""
import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0.1, 1.0, 10)
valorEnt = [-2.232,-1.8,-2.0,-2.0,-1.85,-2.01,-2.0,-2.012,-1.8,-1.65]


def modelo(t,a):
    e=2.718281828459#045235360
    func = 1-e**(a*t)
    return func

plt.plot(t,modelo(t,valorEnt))
print(modelo(t,valorEnt))