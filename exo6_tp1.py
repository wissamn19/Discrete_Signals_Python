import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


Fs = 44100       
d = 0.5          
F = [440]        

for n in range(1, 12):
    F.append(F[n-1] * 2**(1/12))


t = np.arange(0, d, 1/Fs)


melody = np.array([])

for freq in F:
    note = np.sin(2 * np.pi * freq * t)
    melody = np.concatenate((melody, note))

sd.play(melody, Fs)
sd.wait()

plt.figure()
markerline, stemlines, baseline = plt.stem(F)   

plt.title("Frequencies of Musical Notes (A4 to next G#)")
plt.xlabel("Note number")
plt.ylabel("Frequency (Hz)")
plt.grid(True)

plt.show()
