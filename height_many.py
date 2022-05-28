import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rcParams['mathtext.default'] = 'regular'
plt.rc('font', size=12)
plt.rc('axes', labelsize=14)

inputs = []
#keep = [2, 1, 1, 1, 1, 2]
xs = [1, 5, 11, 24]
for i in range(4):
    trials = []
    for j in range(1, 3):
        t, y = np.loadtxt(f'input/height/height_{xs[i]}cm_{j}.txt', delimiter=',', unpack=True, skiprows=1)
        trials.append((t,y))
    inputs.append(trials)

fig, ax = plt.subplots(figsize=(10, 4.5), dpi=600)
#fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#17becf']

for i in range(4):
    for j in range(2):
        t, y = inputs[i][j]
        if j == 1:
            ax.plot(t, y, '--', color=colors[i], label=f'{xs[i]}cm trial {j + 1}')
        else:
            ax.plot(t, y, colors[i], label=f'{xs[i]}cm trial {j + 1}')
            
ax.set_xlabel(xlabel='time (s)',labelpad=8)
ax.set_ylabel(ylabel='sensor output (V)', labelpad=8)
ax.set_ylim(bottom=0)
ax.set_xlim(left=0)
ax.legend()

plt.tight_layout()
plt.savefig(f"output/hm.png")
#plt.show()
