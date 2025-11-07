import numpy as np
from scipy.io import wavfile

Fs1, y1 = wavfile.read("C:\\Users\\Hp\\OneDrive\\Documents\\sounds\\guitar.wav")
Fs2, y2 = wavfile.read("C:\\Users\\Hp\\OneDrive\\Documents\\sounds\\bass.wav")
Fs3, y3 = wavfile.read("C:\\Users\\Hp\\OneDrive\\Documents\\sounds\\drums.wav")


if len(y1.shape) > 1:
    y1 = np.mean(y1, axis=1)

if len(y2.shape) > 1:
    y2 = np.mean(y2, axis=1)

if len(y3.shape) > 1:
    y3 = np.mean(y3, axis=1)


d = 10  
f = 20  


sound1_seg = y1[int(Fs1*d) : int(Fs1*f)]
sound2_seg = y2[int(Fs2*d) : int(Fs2*f)]
sound3_seg = y3[int(Fs3*d) : int(Fs3*f)]


print("Length of sound1_seg =", len(sound1_seg))
print("Length of sound2_seg =", len(sound2_seg))
print("Length of sound3_seg =", len(sound3_seg))


if len(sound1_seg) == len(sound2_seg) == len(sound3_seg):
    print("The 3 segments have identical sizes.")
else:
    print("Segments do NOT have the same size.")
