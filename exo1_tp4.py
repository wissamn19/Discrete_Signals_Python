import numpy as np
from scipy.io import wavfile
import sounddevice as sd


x = np.random.randint(-5, 6, 10)   

Y1 = np.zeros(len(x))
Y2 = np.zeros(len(x))

for n in range(1, len(x)):  
    Y1[n] = 0.5 * (x[n] + x[n-1])  
    Y2[n] = max(x[n], x[n-1])       

print("Input vector x =", x)
print("Y1 (average)   =", Y1)
print("Y2 (max)       =", Y2)



Fs, y = wavfile.read(r"C:\Users\Hp\OneDrive\Documents\sounds\compte.wav")


if len(y.shape) > 1:
    y = y[:, 0]

y = y.astype(float)

Y1_audio = np.zeros(len(y))
Y2_audio = np.zeros(len(y))

for n in range(1, len(y)):
    Y1_audio[n] = 0.5 * (y[n] + y[n-1])   
    Y2_audio[n] = max(y[n], y[n-1])      

print("\nPlaying Y1 (moving average)")
sd.play(Y1_audio, Fs)
sd.wait()

print("Playing Y2 (max nonlinear effect)")
sd.play(Y2_audio, Fs)
sd.wait()
