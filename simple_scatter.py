import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rcParams['mathtext.default'] = 'regular'

traces = []
inputs = ['long', 'short']

for i in range(2):
    t, y = np.loadtxt(f'input/{inputs[i]}.txt', delimiter=',', unpack=True, skiprows=1)
    traces.append([t,y])

fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#17becf', '#bcbd22']
labels = ['short 0s', 'long 1s']

for i in range(2):
    t, y = traces[i]
    ax.plot(t, y, colors[i], label=labels[i])

ax.set_xlabel(xlabel='time (s)',labelpad=8)
ax.set_ylabel(ylabel='sensor output (V)', labelpad=8)
ax.set_ylim(bottom=0)
ax.set_xlim(left=0)
ax.legend()

plt.tight_layout()
#plt.savefig(f"output/out1.png")
plt.show()