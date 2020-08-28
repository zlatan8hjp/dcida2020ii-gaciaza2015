import matplotlib.pyplot as plt
import math

'''
Ecuación para el péndulo simple usando el método de Euler
y{i+1} = y{i} + hf(x,y)
'''
h = 0.01
t = [0]
yo = [math.pi/4]
n = 1000
g = 9.81
l = 1
wo = math.sqrt(g/l)
wi = wo

def euler(y,w):
    wn = w - h*wo*wo*math.sin(y)
    yn = y + h*wn
    return yn, wn

for i in range(n):
    s, wi = euler(yo[i],wi)
    yo.append(s)
    t.append(t[i]+h)

fig, ax = plt.subplots()
ax.plot(t, yo)
ax.grid
ax.set_xlabel('Tiempo')
ax.set_ylabel('Angulo')
plt.show()
