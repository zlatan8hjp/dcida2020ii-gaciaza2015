# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

'''
Ecuación para el péndulo simple usando el método de Euler con numpy
y{i+1} = y{i} + hf(x,y)
'''
h = 0.01
t = np.array([0])               #Arreglo del tiempo
yo = np.array([np.pi/4])        #Arreglo para el ángulo cambiante
n = 1000                        #Iteraciones
g = 9.80665                     
l = 1                           #longitud del péndulo
wo = np.sqrt(g/l)               
wi = wo

def euler(y,w):                     #Función del algoritmo
    wn = w - h*wo*wo*np.sin(y)      #Primera derivada
    yn = y + h*wn                   #Segunda serivada
    return yn, wn

for i in range(n):
    s, wi = euler(yo[i],wi)
    yo = np.append(yo,s)
    t = np.append(t,t[i]+h)

fig, ax = plt.subplots()
ax.plot(t, yo)
ax.grid
ax.set_xlabel('Tiempo')
ax.set_ylabel('Angulo')
plt.show()

