import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [16,12]
plt.rcParams.update({'font.size': 18})

#Create a simple signal with two frequencies

dt = 0.001
t = np.arange(0,1,dt)
f = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t) # sum of two frequencies
f_clean = f
f = f + 2.5*np.random.randn(len(t))

# plt.plot(t, f, color='c', linewidth=1.5,label='Noisy')
# plt.plot(t, f_clean,color='k' , linewidth=2,label='Clean' ) 
# plt.xlim(t[0],t[-1])
# plt.legend()

##computing FFT
n = len(t)
fhat = np.fft.fft(f,n)
PSD = fhat * np.conj(fhat) / n
freq = (1/(dt*n)) * np.arange(n)
L = np.arange(1, np.floor(n/2), dtype = 'int')





#using PSD to filter out noise
indices = PSD > 100 # finds all frequencies larger than 100
PSDClean = PSD*indices # zeroes out the rest
fhat = indices * fhat

#FFT gives the original signal back without the noise
ffilt = np.fft.ifft(fhat)


fig,axs = plt.subplots(3, 1)


plt.sca(axs[0])
plt.plot(t, f,color='c', linewidth=1.5,label='Noisy') 
plt.plot (t,f_clean, color='k', linewidth=2,label='Clean') 
plt.xlim(t[0],t[-1]) 
plt.legend()

plt.sca(axs[1])
plt.plot(t, ffilt,color='k', linewidth=2,label='Filtered')
plt.xlim(t[0],t[-1])
plt.legend()

plt.sca(axs[2])
plt.plot(freq[L],PSD[L], color='c', linewidth=2,label='Noisy')
plt.plot(freq[L],PSDClean[L],color='k',linewidth=1.5,label='Filtered')
plt.xlim(freq[L[0]],freq[L[-1]])
plt.legend()


plt.show()