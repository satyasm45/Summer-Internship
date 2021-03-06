# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hK-dr2CTCBX-YjGmbJ7vEOXA96fy9_0l
"""

#Code by Satya_Sangram
#For vectors 2.22
import numpy as np
import matplotlib.pyplot as plt

m=0.1
g=np.array([0,-9.8])
a=np.array([1,0])
F1=m*g
F2=m*a
F3=-F2
V=np.array([F1,F2,F3])
origin = [0], [0] # origin point
plt.quiver(*origin, F1[0],F1[1] ,color='r',scale=2,label="$F_a,F_b,F_c$")
plt.quiver(*origin, F2[0],F2[1] ,color='b',scale=2,label="$F_d(Case1)$")
plt.quiver(*origin, F3[0],F3[1] ,color='g',scale=2,label="$F_d(Case2)$")

plt.ylim(-50,5)
plt.legend(loc='upper left')

plt.grid()
plt.show()