import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-np.pi ,np.pi , 0.001)

u =  np.sin(np.pi / 4*x)
v =  np.cos(np.pi / 4*x)

Y_add = u + v 

plt.plot(x,Y_add,label='Y_add = u + v')
plt.xlabel('x')
plt.ylabel('Y_add')
plt.title('Addition of two signals')
plt.show()

alpha = 0.5
beta  = 0.3

Y_mul = alpha * u + beta * v

plt.plot(x,Y_mul,'r--',label='Y_mul = 0.5*u + 0.3*v')
plt.xlabel('x')
plt.ylabel('Y_mul')
plt.title('Multiply of two signals')
plt.show()

gate = (x >= np.pi/2) & (x <= 3*np.pi/2)

Y_gate = u * gate

plt.plot(x,Y_gate,label='Y_gate = u * gate')    
plt.xlabel('x')
plt.ylabel('Y_gate')
plt.title('Gating of signal u')
plt.show()

Y_inv = -u
plt.plot(x,Y_inv,label='Y_inv = -u')
plt.xlabel('x')
plt.ylabel('Y_inv')
plt.title('Inversion of signal u')
plt.show()

