import numpy as np
import matplotlib.pyplot as plt



x = np.arange(-np.pi ,np.pi , 0.001)

u =  np.sin(np.pi / 4*x)
v =  np.cos(np.pi / 4*x)

plt.plot(x,u,label='u=sin(pi/4*x)')
plt.plot(x,v,label='v=cos(pi/4*x)')
plt.xlabel('x')
plt.ylabel('u and v')
plt.title('Two signals: sine and cosine')

plt.figure()
plt.show()