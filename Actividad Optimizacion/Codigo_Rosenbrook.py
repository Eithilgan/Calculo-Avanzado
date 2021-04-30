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
import matplotlib.patches as mpatches

t = np.linspace(0.1, 3, 30)
a = 2.0


def Weibull(t,a):
    func = 1-np.exp(-(a*t))
    return func
def Higuchi(t,a):
    func2= a*t**(0.5)
    return func2

orange_patch = mpatches.Patch(color='orange', label='Higuchi')
blue_patch = mpatches.Patch(color='dodgerblue', label='Weibull')

plt.legend(handles=[orange_patch,blue_patch])
plt.plot(Weibull(t,a))
plt.plot(Higuchi(t,a))



f = lambda x,y: (x-1)**2 + 100*(y-x**2)**2;

figRos = plt.figure(figsize=(12, 7))
axRos = figRos.gca(projection='3d')

# Evaluar la funcion
X = np.arange(-2, 2, 0.15)
Y = np.arange(-1, 3, 0.15)
X, Y = np.meshgrid(X, Y)
Z = f(X,Y)

# Plot the surface
surf = axRos.plot_surface(X, Y, Z, cmap=cm.gist_heat_r,
                       linewidth=0, antialiased=False)
axRos.set_zlim(0, 100)
figRos.colorbar(surf, shrink=0.5, aspect=10)
plt.show() 
