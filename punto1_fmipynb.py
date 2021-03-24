# -*- coding: utf-8 -*-
"""punto1_fmipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19I3GkiaaJnh3A0snW1HcMLebS8FaYuHK
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as fourier

#inciso a
fig, ax = plt.subplots(2, 1, figsize=(9, 6),tight_layout = True)
Fs = 80e3
t = np.arange(-0.01, 0.01, 1/Fs)
Ac = 1
fc = 1000

Am = 1
fm = 100
bheta = 5

m_t = Am*np.cos(2*np.pi*fm*t)
modulada = Ac*np.cos(2*np.pi*fc*t + bheta*np.sin(2*np.pi*fm*t))

ax[0].plot(t, m_t, 'navy')
ax[1].plot(t, modulada, 'red')
ax[0].title.set_text("Señal moduladora")
ax[1].title.set_text("Señal modulada")

#inciso c
trans_fourier = np.fft.fft(modulada)
trans_fourier_2 = np.fft.fftshift(trans_fourier)
espectro = abs(trans_fourier_2)

portadora = np.cos(2*np.pi*fc*t)
trans_fourier_por = np.fft.fft(portadora)
trans_fourier_por_2 = np.fft.fftshift(trans_fourier_por)
espectro_2 = abs(trans_fourier_por_2)
frq = np.arange(-Fs/2, Fs/2, Fs/len(modulada))

fig, ax = plt.subplots(4,figsize=(10,10),tight_layout = True)
ax[0].plot(frq, espectro, 'red')
ax[1].phase_spectrum(modulada, Fs = Fs, c = 'limegreen')
ax[2].plot(frq, espectro_2, 'red')
ax[3].phase_spectrum(portadora, Fs = Fs, c = 'limegreen')

ax[0].title.set_text("Espectro en magnitud modulada")
ax[1].title.set_text("Espectro en fase señal modulada")
ax[2].title.set_text("Espectro en magnitud portadora")
ax[2].title.set_text("Espectro en fase señal portadora")