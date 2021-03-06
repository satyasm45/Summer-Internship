# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RPVbpaNzYXWn4GR9olDSduX41HHvYORK
"""

import numpy as np
import matplotlib.pyplot as plt

#Module for Bayes Theorem
def bayes_theorem(p_e1,p_e2,p_xgiven_e1,p_xgiven_e2):
	p_x= p_e1*p_xgiven_e1 + p_e2*p_xgiven_e2
	numerator1 = p_e1*p_xgiven_e1
	p_e1given_x=numerator1/p_x
	return p_e1given_x

#Probability that ball transferred from bag I is Black
p_1= 4/7
#Probability that ball transferred from bag I is Red
p_2= 1-p_1
#Probability that ball drawn from Bag II is Red given that ball transfered from Bag I was Black
p_red_1=2/5
#Probability that ball drawn from Bag II is Red given that ball transfered from Bag I was Red
p_red_2= 1/2

#Probability that person has disease provided his test result is positive
prob= bayes_theorem(p_1,p_2,p_red_1, p_red_2)

print(prob)