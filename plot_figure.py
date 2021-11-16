# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 22:29:57 2021

@author: Superhhu
"""
import matplotlib.pyplot as plt

x=[50,500,1500,3000,6000,12000]
y=[7.9,17.3,20.3,18.7,14.4,13.7]
plt.rcParams.update({'font.size': 26})

plt.scatter(x,y)

plt.plot(x,y)
plt.xlabel('Number of Merges')
plt.ylabel('BLEU')


x=[0.01,0.05,0.10,0.20]
y=[15.3,19.9,24.0,5.3]

plt.rcParams.update({'font.size': 26})

plt.scatter(x,y)

plt.plot(x,y)
plt.xlabel('BPE Dropout Probability')
plt.ylabel('BLEU')
