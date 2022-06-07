import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from math import floor
matplotlib.rcParams['mathtext.default'] = 'regular'
plt.rc('font', size=10)
plt.rc('axes', labelsize=10)
matplotlib.rcParams["axes.formatter.limits"] = [-3, 6]

def m1(t, a, b, c, d):
    #a = 9.432*0.75
    #b = 2.392
    #c = 0.1246
    #d = -0.4996
    left = a / np.sqrt(t)
    upper = -b*((d - c*t)**2)
    right = np.exp(upper / t)
    return left * right

def m2(t, a, b, c, d):
    #a = 55.54*0.75
    #b = 23.81
    #c = 0.000256
    #d = -0.3712
    left = a / np.sqrt(t**3)
    upper = -b*((c*t - d)**2)
    right = np.exp(upper / t)
    return left * right

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

inputs = []
to_trunc_s = [109, 129, 77, 127, 86, 87, 80, 85, 111, 85, 87, 92]
to_trunc_e = [171, 168, 164, 172, 168, 163, 166, 164, 171, 172, 164, 166]
for i in range(12):
    t, y = np.loadtxt(f'input/trials/t{i+1}.txt', delimiter=',', unpack=True, skiprows=1)
    to_sub = np.average(y[:to_trunc_s[i]])
    inputs.append([t[:to_trunc_e[i]],y[to_trunc_s[i]:to_trunc_e[i] + to_trunc_s[i]] - to_sub])

#vals1, covs1 = curve_fit(m1, t, y)
#vals2, covs2 = curve_fit(m2, t, y)

#m1_out = m1(t, *vals1)
#inputs.append([t,m1_out])
#m2_out = m2(t, *vals2)
#inputs.append([t,m2_out])

#fig, ax = plt.subplots(figsize=(10, 4.5), dpi=600)
fig1, axs1 = plt.subplots(3, 4, figsize=(11.69,8.27))
fig2, axs2 = plt.subplots(2, 4, figsize=(11.69,8.27))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#17becf', '#bcbd22']

m1s = []
m2s = []
vars1 = []
vars2 = []

for i in range(12):
    t, y = inputs[i]
    row = floor(i / 4)
    col = i % 4
    ax = axs1[row][col]
    #t = moving_average(t, 3)
    vals1, covs1 = curve_fit(m1, t, y)
    m1s.append(vals1)
    vars1.append(np.diag(covs1))
    m1_out = m1(t, *vals1)
    vals2, covs2 = curve_fit(m2, t, y)
    m2_out = m2(t, *vals2)
    m2s.append(vals2)
    vars2.append(np.diag(covs2))
    ax.plot(t, y, '-', color='b', label='exp')
    ax.plot(t, m1_out, '--', color='red', label='model 1')
    ax.plot(t, m2_out, '--', color='green', label='model 2')
    ax.set_title(f"trial {i + 1}")
    #if col == 0:
    #    ax.set_ylabel(ylabel='sensor output (V)')
    #ax.set_xlabel(xlabel='time (s)')
    ax.set_ylim(bottom=-0.25, top=3.5)
    ax.set_xlim(left=0, right=7)
    ax.set_xticks(np.arange(0, 7 + 1, step=0.5))
    ax.set_yticks(np.arange(0, 3.5, step=0.5))
    ax.grid(color='gray', linestyle=':', linewidth=1)
    ax.legend(prop={'size': 8})

titles = ['a', 'b', 'c', 'd']
# convert 4 arrays (1 for each letter) of len 12
# instead of 12 arrays of len 4
m1s = list(zip(*m1s))
m2s = list(zip(*m2s))
covs1 = list(zip(*covs1))
covs2 = list(zip(*covs2))

for i in range(8):
    row = floor(i / 4)
    col = i % 4
    ax = axs2[row][col]
    x = np.arange(1, 12 + 1)
    mean = 0
    var = 0
    if row == 0:
        y1 = m1s[col]
        mean1 = np.full(12, np.average(y1))
        mean = np.average(y1)
        var = np.var(y1)
        ax.plot(x, y1, color='b')
        ax.plot(x, mean1, '--', color='r')
    elif row == 1:
        y2 = m2s[col]
        mean2 = np.full(12, np.average(y2))
        mean = np.average(y2)
        var = np.var(y2)
        ax.plot(x, y2, color='g')
        ax.plot(x, mean2, '--', color='r')
    ax.grid(color='gray', linestyle=':', linewidth=1)
    ax.set_title(titles[col % len(titles)])
    ax.set_ylabel(ylabel='coefficient value')
    ax.set_xlabel(xlabel='trial')
    ax.set_xticks(np.arange(0, 12 + 3, step=3))
    props = dict(boxstyle='round', facecolor='grey', alpha=0.5)
    ax.text(0.95, 0.05, f'$\mu$ = {mean:.2f}\nRMSE = {2}\n$\sigma^2$ = {var:.2f}\nVMR = {var/mean:.2f}', transform=ax.transAxes, bbox=props, verticalalignment='bottom', horizontalalignment='right', fontsize=8)

fig2.tight_layout()
fig1.tight_layout()
#plt.savefig(f"output/model.png")
plt.show()
