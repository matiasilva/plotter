import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rcParams['mathtext.default'] = 'regular'
plt.rc('font', size=12)
plt.rc('axes', labelsize=14)

inputs = []
keep = [1, 3, 1, 3, 2, 2]
xs = [30, 60, 90, 120, 150, 180]
for i in range(6):
    t, y = np.loadtxt(f'input/rotation/rotation_v_{xs[i]}_{keep[i]}.txt', delimiter=',', unpack=True, skiprows=1)
    inputs.append([t, y])

inputs[0][0] = inputs[0][0][:-106]
inputs[0][1] = inputs[0][1][106:]

inputs[1][0] = inputs[1][0][:-30]
inputs[1][1] = inputs[1][1][30:]

inputs[5][1] = 0.5*inputs[5][1] + 0.1

fig, ax = plt.subplots(figsize=(10, 4.5), dpi=600)
#fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#17becf']

for i in range(6):
    t, y = inputs[i]
    ax.plot(t, y, colors[i], label=f'{xs[i]} degrees')
            
ax.set_xlabel(xlabel='time (s)',labelpad=8)
ax.set_ylabel(ylabel='sensor output (V)', labelpad=8)
ax.set_ylim(bottom=0)
ax.set_xlim(left=0)
ax.legend()

plt.tight_layout()
plt.savefig(f"output/out1.png")
#plt.show()
