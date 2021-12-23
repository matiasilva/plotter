import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from uuid import uuid4
matplotlib.rcParams['mathtext.default'] = 'regular'

x = np.loadtxt(f"input/x.txt", delimiter='\t', unpack=True)
y = np.loadtxt("input/y.txt",delimiter='\t', unpack=True)

plt.plot(x, y[0], f"D", markerfacecolor='r', markeredgecolor='k', label="SBD")
plt.plot(x[1], y[1], f"D", markerfacecolor='g', markeredgecolor='k', label="p-n")
ln_a1 = np.log(y[0])
ln_a2 = np.log(y[1])
z1 = np.polyfit(x[0], ln_a1, 1)
z2 = np.polyfit(x[1], ln_a2, 1)
A1 = np.exp(z1[1])
A2 = np.exp(z2[1])
B1 = z1[0]
B2 = z2[0]
def expo(A, B, x):
    return A*np.exp(B*x)
#z2 = np.polyfit(x[1], y[1], 1)
#p2 = np.poly1d(z2)
trend_x1 = np.arange(0, 1, 0.025)
trend_x2 = np.arange(0, 1.2, 0.025)
plt.plot(trend_x1, expo(A1, B1, trend_x1), "b-")
plt.plot(trend_x2, expo(A2, B2, trend_x2), "b-")
print(expo(A2, B2, 0.8))
print(expo(A1, B1, 0.6))
plt.xlabel('$V_{F}$   [V]')
plt.ylabel('$I_{F}$   [mA]')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.legend()
plt.tight_layout()
#plt.savefig(f"output/test-{str(uuid4())[:4]}.png")
plt.show()
