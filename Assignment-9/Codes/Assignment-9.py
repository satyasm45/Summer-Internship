# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RhG96scPc5fH1CrEui0knYsk5wiWqJP8
"""

#Code by Satya Sangram
#For Inequality 2.67
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#vertices
A = np.array([-15, 0])
B = np.array([15, 0])
C = np.array([-5, 0])
D = np.array([0,0])

plt.figure(0)
#Generating and plotting points on number line
X_coord = np.array(np.linspace(-14, 14, num=29))
Y_coord = np.zeros(29)
plt.plot(X_coord, Y_coord, '|',color='k')

#Generating all lines
x_AB = line_gen(A,B)
x_CB = line_gen(C,B)

#Plotting all lines
plt.plot(x_AB[0,:], x_AB[1,:], color='k')
plt.plot(x_CB[0,:], x_CB[1,:], color='r',linewidth=2.5, label='x>-5')

#Plotting and labelling points
plt.plot(A[0], A[1], '<',color='k')
plt.text(A[0]-1, 0.005, '$-∞$')
plt.plot(B[0], B[1], '>',color='r')
plt.text(B[0], 0.005, '$∞$')
plt.plot(C[0], C[1], 'o',color='b')
plt.text(C[0]-0.5, 0.005 , '$-5$')
plt.text(D[0]-0.2, 0.005 , '$0$')

plt.axis('off')
plt.legend(loc='best')
plt.show()

plt.figure(1)
C = np.array([5, 0])
x_CB = line_gen(C,B)

#Generating and plotting points on number line
X_coord = np.array(np.linspace(-14, 14, num=29))
Y_coord = np.zeros(29)
plt.plot(X_coord, Y_coord, '|',color='k')

#Plotting all lines
plt.plot(x_AB[0,:], x_AB[1,:], color='k')
plt.plot(x_CB[0,:], x_CB[1,:], color='r',linewidth=2.5, label='x>5')

#Plotting and labelling points
plt.plot(A[0], A[1], '<',color='k')
plt.text(A[0]-1, 0.005, '$-∞$')
plt.plot(B[0], B[1], '>',color='r')
plt.text(B[0], 0.005, '$∞$')
plt.plot(C[0], C[1], 'o',color='b')
plt.text(C[0]-0.5, 0.005 , '$5$')
plt.text(D[0]-0.2, 0.005 , '$0$')

plt.axis('off')
plt.legend(loc='best')
plt.show()