# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 15:33:37 2021

@author: Ezxiio
"""
import scipy.optimize as optimize
def higuchi(t):

    return t**(1/2)
res=optimize.minimize(higuchi,0,method='TNC',tol=1e-6)
print(res)