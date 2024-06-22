import sys
import os
import numpy as np
import matplotlib.pyplot as pt
from scipy.fft import rfft, rfftfreq, irfft
import funcs

script_location = os.path.dirname(os.path.realpath(__file__))
if (len(sys.argv)) < 2:
    file_path = f"{script_location}/signal_12.npy"
else:
    file_path = sys.argv[1]
params = {'axes.labelsize': 'x-large',
          'axes.titlesize': 'x-large',
          'xtick.labelsize': 'large',
          'ytick.labelsize': 'large',
          "figure.autolayout": True,
          "figure.figsize": [35.0, 15.0],
          'text.usetex': True,
          }
pt.rcParams.update(params)
pt.ioff()
data = np.load(file_path)
sampling_period = 0.1e-3
N = len(data)
t_data = np.linspace(0, N * sampling_period, N)
spectrum = rfft(data)
amplitudes = [2 / N * np.abs(y) for y in spectrum]
freqs = rfftfreq(N, sampling_period)
fig, axes = pt.subplots(5, 1)
funcs.add_graph(t_data, data, "Noised signal", '$t$, $s$', 'Value', axes[0])
funcs.add_graph(freqs, amplitudes, "Fourier transform result in frequency field",
                'Frequency, $Hz$',
                'Amplitude', axes[1])

max_spectrum_power = max(np.abs(y) for y in spectrum)
signal_indices = set(np.where(np.abs(spectrum) * 2 > max_spectrum_power)[0])
signal_spectrum = np.copy(spectrum)

for i in range(len(signal_spectrum)):
    if i not in signal_indices:
        signal_spectrum[i] = 0
signal_data = irfft(signal_spectrum)

funcs.add_graph(freqs, [2 / N * np.abs(y) for y in signal_spectrum], "Signal spectrum without noise",
                'Frequency, $Hz$',
                'Amplitude', axes[2])
funcs.add_graph(t_data, signal_data, "Signal", '$t$, $s$', 'Value', axes[3])
funcs.add_graph(t_data[:1000], signal_data[:1000], "Signal (first 1000 samples)", '$t$, $s$', 'Value', axes[4])

fig.savefig(f"{script_location}/result.jpg")
pt.cla()
pt.close(fig)
