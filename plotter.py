import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from uuid import uuid4

inputs = []
inputs.append({
	"name": "al",
	"label": "Al alloy",
	"lcolor": "b",
	"textloc": (1.8, 1.5),
	"textoff": (90, -25),
})
inputs.append({
	"name": "pmma",
	"label": "PMMA",
	"lcolor": "g",
	"textloc": (2.2, 2.6),
	"textoff": (-15, 25),
})

fig, ax = plt.subplots()

for input in inputs:
	name, label, lcolor, textloc, textoff = input.values()
	load, disp, force = np.loadtxt(f"input/{name}.txt", delimiter='	', unpack=True)
	ax.plot(load, disp, f"-D{lcolor}", label=label, markerfacecolor='r', markeredgecolor='k')
	p, cov = np.polyfit(disp, load, 1, cov=True)
	print(f"{label}: {np.sqrt(np.diag(cov))}")
	ax.annotate(fr"k = {p[0]:.3f} kg $\mathregular{{mm^{-1}}}$",
            xy=textloc, xycoords='data',
            horizontalalignment='right', arrowprops={"arrowstyle":  "-|>"},
			verticalalignment='center', xytext=textoff, textcoords='offset points', bbox=dict(facecolor='none', edgecolor='black', pad=5.0))
	ax.errorbar(load, disp, yerr=50*0.002, xerr=8*0.01, ecolor='black', capsize=3, fmt="none")

ax.legend()

ax.set(xlabel='deflection (mm)', ylabel='mass on load hanger (kg)')
fig.savefig(f"output/test-{str(uuid4())[:4]}.png")
plt.show()
