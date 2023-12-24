import numpy as np
import matplotlib.pylab as plt

N = 50

x = np.random.randn(N)

y = 3*np.sin(x)

w = np.sum(y)/np.sum(x)

print("solution:", w)

pred = w * x

plt.plot(y)
plt.plot(pred)
plt.legend(["truth", "prediction"])

plt.show()