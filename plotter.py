import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
matplotlib.rcParams['mathtext.default'] = 'regular'
plt.rc('font', size=12)
plt.rc('axes', labelsize=14)

def m1(t, a, b, c, d):
    #a = 9.432*0.75
    #b = 2.392
    #c = 0.1246
    #d = -0.4996
    left = a / np.sqrt(t)
    upper = -b*((d - c*t)**2)
    right = np.exp(upper / t)
    return left * right + 0.18

def m2(t, a, b, c, d):
    #a = 55.54*0.75
    #b = 23.81
    #c = 0.000256
    #d = -0.3712
    left = a / np.sqrt(t**3)
    upper = -b*((c*t - d)**2)
    right = np.exp(upper / t)
    return left * right + 0.18

inputs = []
t, y = np.loadtxt(f'input/rotation/rotation_v_120_2.txt', delimiter=',', unpack=True, skiprows=1)
inputs.append([t,y])

vals1, covs1 = curve_fit(m1, t, y)
vals2, covs2 = curve_fit(m2, t, y)

m1_out = m1(t, *vals1)
inputs.append([t,m1_out])
m2_out = m2(t, *vals2)
inputs.append([t,m2_out])

#fig, ax = plt.subplots(figsize=(10, 4.5), dpi=600)
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#17becf', '#bcbd22']

labels = ['experimental', 'model 1', 'model 2']
for i in range(3):
    t, y = inputs[i]
    ax.plot(t, y, colors[i], label=labels[i])
            
ax.set_xlabel(xlabel='time (s)',labelpad=8)
ax.set_ylabel(ylabel='sensor output (V)', labelpad=8)
ax.set_ylim(bottom=0)
ax.set_xlim(left=0)
ax.legend()

plt.tight_layout()
#plt.savefig(f"output/model.png")
plt.show()
