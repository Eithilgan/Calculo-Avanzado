# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 19:21:58 2021

@author: Ezxiio

"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(0.1, 1, 10)
a = 2.0


def Weibull(t,a):
    func = 1-np.exp(-(a*t))
    return func

plt.plot(Weibull(t,a))



f = lambda x,y: (x-1)**2 + 100*(y-x**2)**2;

figRos = plt.figure(figsize=(12, 7))
axRos = figRos.gca(projection='3d')

# Evaluar la funcion
X = np.arange(0, 1, 0.1)
Y = np.array(Weibull(t,a))
X, Y = np.meshgrid(X, Y)
Z = f(X,Y)

# Plot the surface
surf = axRos.plot_surface(X, Y, Z, cmap=cm.gist_heat_r,
                       linewidth=0, antialiased=False)
axRos.set_zlim(0, 100)
figRos.colorbar(surf, shrink=0.5, aspect=10)
plt.show() 