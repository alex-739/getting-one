# name- praveen kumar roll-39/cse/16028,0000184
import numpy as np
import matplotlib.pyplot as plt

fm = 5.0    # frequency of modulating signal
fc = 50.0 # frequency of carrier signal

wc = 2.0 * np.pi * fc
wm = 2.0 * np.pi * fm

time = np.arange(44100.0) / 44100.0
baseband_signal = np.cos(wm * time)     # m(t) = cos(wm t)
carrier = np.cos(wc * time)                   # c(t) = cos(wc t)  
AMW = np.zeros_like(baseband_signal)

for i, t in enumerate(time):
    AMW[i] = (1 + np.cos(wm * t)) * np.cos(wc * t)
    
plt.subplot(3, 1, 1)
plt.title('Amplitude Modulation')
plt.plot(baseband_signal)
plt.ylabel('Baseband Signal')

plt.subplot(3, 1, 2)
plt.plot(carrier)
plt.ylabel('Carrier Signal')

plt.subplot(3, 1, 3)
plt.plot(AMW)
plt.ylabel('Modulated Signal')

plt.show()



