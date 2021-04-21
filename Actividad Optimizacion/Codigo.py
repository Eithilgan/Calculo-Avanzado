# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 15:33:37 2021

@author: Ezxiio
"""
import numpy as np
import scipy.optimize as optimize

def modelo(a):
    e=2.718281828459#045235360
    t = np.linspace(0.1, 1.0, 10)
    func = 1-e**(a*t)
    return func
res=optimize.minimize(modelo,0.1,method='TNC',tol=1e-6)
print(res)