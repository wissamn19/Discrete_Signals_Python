import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-4, 4)
t = np.arange(-5, 5.1, 0.1)

dirac_pulse = (n == 0).astype(int)
step_signal = (n >= 0).astype(int)
window_signal = ((n >= 0) & (n < 4)).astype(int)
sigma = 1
gaussian_signal = np.exp(-t**2 / (2*sigma**2))


plt.subplot(2, 2, 1)
plt.stem(n, dirac_pulse)
plt.title('Dirac Pulse δ[n]')
plt.xlabel('n'); 
plt.ylabel('Amplitude'); 
plt.grid(True)

plt.subplot(2, 2, 2)
plt.stem(n, step_signal)
plt.title('Step Signal u[n]')
plt.xlabel('n'); 
plt.ylabel('Amplitude'); 
plt.grid(True)

plt.subplot(2, 2, 3)
plt.stem(n, window_signal)
plt.title('Rectangular Window w[n]')
plt.xlabel('n'); 
plt.ylabel('Amplitude'); 
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(t, gaussian_signal, 'r')
plt.title('Gaussian Function g(t)')
plt.xlabel('t'); 
plt.ylabel('Amplitude'); 
plt.grid(True)


plt.show()
