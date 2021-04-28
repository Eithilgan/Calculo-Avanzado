# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 01:03:39 2021

@author: Ezxiio
"""
import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0.1, 1, 10)
a = 2.0


def modelo_1(t,a):
    func = 1-np.exp(-(a*t))
    return func

plt.plot(t,modelo_1(t,a))
sum()
