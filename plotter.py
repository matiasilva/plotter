import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from uuid import uuid4
matplotlib.rcParams['mathtext.default'] = 'regular'

x = np.loadtxt(f"input/x.txt", delimiter='\t', unpack=True)
y = np.loadtxt("input/y.txt",delimiter='\t', unpack=True)

fig, ax = plt.subplots(1)

ax.plot(x, y, f"x", markerfacecolor='r', markeredgecolor='r')
ax.set(xlabel='peak-to-peak input (mV)', ylabel='demodulator output (mV)')

plt.tight_layout()
plt.savefig(f"output/test-{str(uuid4())[:4]}.png")
plt.show()
