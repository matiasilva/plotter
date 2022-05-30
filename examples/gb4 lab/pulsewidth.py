import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rcParams['mathtext.default'] = 'regular'
plt.rc('font', size=12)
plt.rc('axes', labelsize=14)

inputs = []
keep = [2, 1, 1, 1, 1, 2]
for i in range(1, 7):
    t, y = np.loadtxt(f'input/pulsewidth/0{i}_{keep[i-1]}.txt', delimiter=',', unpack=True, skiprows=1)
    inputs.append((t,y))

fig, ax = plt.subplots(figsize=(10, 4.5), dpi=600)
#fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#17becf']

for i in range(6):
    t, y = inputs[i]
    ax.plot(t, y, colors[i], label=f'0.{i+1}s pulse')

ax.set_xlabel(xlabel='time (s)',labelpad=8)
ax.set_ylabel(ylabel='sensor output (V)', labelpad=8)
ax.set_ylim(bottom=0)
ax.set_xlim(left=0)
ax.legend()

plt.tight_layout()
plt.savefig(f"output/pw.png")
#plt.show()
