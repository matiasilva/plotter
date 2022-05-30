import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rcParams['mathtext.default'] = 'regular'
plt.rc('font', size=12)
plt.rc('axes', labelsize=14)

inputs = []
#keep = [2, 1, 1, 1, 1, 2]
xs = [0, 30, 60, 90, 120, 150, 180]
for i in range(7):
    trials = []
    for j in range(1, 4):
        try:
            t, y = np.loadtxt(f'input/rotation/rotation_h_{xs[i]}_{j}.txt', delimiter=',', unpack=True, skiprows=1)
            trials.append([t,y])
        except:
            pass
    inputs.append(trials)

#fig, ax = plt.subplots(figsize=(10, 4.5), dpi=600)
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#17becf', '#bcbd22']

for i in range(7):
    for j in range(3):
        if j < len(inputs[i]):
            t, y = inputs[i][j]
            if j == 1:
                ax.plot(t, y, '--', color=colors[i], label=f'{xs[i]}deg trial {j + 1}')
            else:
                ax.plot(t, y, colors[i], label=f'{xs[i]}deg trial {j + 1}')
            
ax.set_xlabel(xlabel='time (s)',labelpad=8)
ax.set_ylabel(ylabel='sensor output (V)', labelpad=8)
ax.set_ylim(bottom=0)
ax.set_xlim(left=0)
ax.legend()

plt.tight_layout()
#plt.savefig(f"output/out1.png")
plt.show()
