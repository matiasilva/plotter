# sinusoidal PWM visualizer
# made by matias <3 in 2021
# for the switch-mode power supply course (3B3)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.widgets import Slider, Button
import math


class Switcher():

    def __init__(self, cr_f, m_f, cr_fq, m_fq, m_amp, cr_amp, t):
        self.cr_f = cr_f
        self.m_f = m_f
        self.cr_fq = cr_fq
        self.m_amp = m_amp
        self.cr_amp = cr_amp
        self.m_fq = m_fq
        self.t = t

        # iniial values
        self.ini_cr_fq = cr_fq
        self.ini_m_amp = m_amp

    def get_cr(self):
        n = len(t)
        cr_out = np.zeros(n)
        for i in range(n):
            t_val = self.t[i]
            cr_out[i] = self.cr_f(t_val, self.cr_fq, self.cr_amp)
        return cr_out

    def get_m(self):
        return self.m_f(self.t, self.m_fq, self.cr_amp*self.m_amp)

    def set_m_amp(self, val):
        self.m_amp = val/100

    def set_cr_fq(self, val):
        self.cr_fq = val

    @staticmethod
    def bipolar(cr, m, v_d):
        v_an = v_d*(m > cr)
        v_bn = v_d*(cr > m)
        return v_an - v_bn

    @staticmethod
    def unipolar(cr, m, v_d):
        v_an = v_d*(m > cr)
        v_bn = v_d*(-m > cr)
        return v_an - v_bn


def cr(t, f, h):
    # the carrier signal
    T = 1 / f
    m = 4 * h / T
    norm_t = t - math.floor(t / T)*T
    if norm_t < T / 4:
        return m*norm_t
    elif norm_t < 3 * T / 4:
        return -m*norm_t + 2*h
    elif norm_t < T:
        return m*norm_t - 4*h
    else:
        print(t, T, m, norm_t)


def m(t, f, a):
    # the "reference" control signal
    return a * np.sin(2 * np.pi * f * t)


total_time = 10
v_d = 3
t = np.linspace(0, total_time, 2000)
sw = Switcher(cr, m, 2, 1/total_time, 0.65, 1, t)

fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(14, 9), sharex=True)
line_carrier, = ax1.plot(t, sw.get_cr())
line_control, = ax1.plot(t, sw.get_m())
line_unipolar, = ax2.plot(t, Switcher.unipolar(
    sw.get_cr(), sw.get_m(), v_d), "k", lw=0.75)
line_bipolar, = ax3.plot(t, Switcher.bipolar(
    sw.get_cr(), sw.get_m(), v_d), "k", lw=0.75)
fig.suptitle('Sinusoidal Pulse Width Modulation (SPWM)')
ax1.set_title('carrier and control signals')
ax2.set_title('unipolar switching output')
ax3.set_title('bipolar switching output')
ax3.set_xlabel('time [s]')
ax3.set_xlim(0, total_time)
ax3.axhline(0, color='red', lw=0.5)

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)

axfreq = Axes(fig, [0.2, 0.06, 0.65, 0.03])
fig.add_axes(axfreq)
carrier_freq_slider = Slider(
    ax=axfreq,
    label=r'$f$ $v_{cr}$ [Hz]',
    valmin=0.25,
    valmax=5,
    valinit=sw.ini_cr_fq,
    valstep=0.2,
)

axamp = Axes(fig, [0.2, 0.02, 0.65, 0.03])
fig.add_axes(axamp)
control_amp_slider = Slider(
    ax=axamp,
    label=r'$|v_{m}|$ [%]',
    valmin=1,
    valmax=100,
    valinit=sw.ini_m_amp*100,
    valstep=1,
)


def update_control(val):
    sw.set_m_amp(val)
    line_control.set_ydata(sw.get_m())
    update_both()


def update_carrier(val):
    sw.set_cr_fq(val)
    line_carrier.set_ydata(sw.get_cr())
    update_both()


def update_both():
    line_unipolar.set_ydata(Switcher.unipolar(sw.get_cr(), sw.get_m(), v_d))
    line_bipolar.set_ydata(Switcher.bipolar(sw.get_cr(), sw.get_m(), v_d))


# register the update function with each slider
carrier_freq_slider.on_changed(update_carrier)
control_amp_slider.on_changed(update_control)


plt.show()
