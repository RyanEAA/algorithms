import numpy as np
import matplotlib.pyplot as plt

# Generate a signal with two frequencies
fs = 1000  # Sampling frequency
t = np.arange(0, 1, 1/fs)  # Time vector
f1, f2 = 50, 120  # Frequencies of the signal
signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# Perform FFT
fft_result = np.fft.fft(signal)
freq = np.fft.fftfreq(len(fft_result), 1/fs)

# Plot the original signal and its frequency spectrum
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Original Signal')

plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(fft_result))
plt.title('Frequency Spectrum')
plt.xlabel('Frequency (Hz)')

plt.tight_layout()
plt.show()
