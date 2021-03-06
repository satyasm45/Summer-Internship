# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eTxr3-TsHdUxv7htprJt_UBr1ohT_Qt8
"""

#code by Satya Sangram
#18/05/2021
#Triangle PQR for Q.NO 2.25

import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

QR = 4
PR = 6

#Calculating third side 
PQ=((PR*PR)-(QR*QR))**(0.5)

#Triangle vertices
P = np.array([0,PQ]) 
Q = np.array([0,0]) 
R = np.array([QR,0]) 


#Generating all lines
x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_RP = line_gen(R,P)

#Plotting all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_RP[0,:],x_RP[1,:],label='$RP$')

plt.plot(P[0], P[1], 'o')
plt.text(0.1, P[1] * (1 - 0.1) , 'P')
plt.plot(Q[0], Q[1], 'o')
plt.text(0.1, 0.1 , 'Q')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.02), R[1] * (1 - 0.1) , 'R')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()