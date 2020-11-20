import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
import pandas as pd

amplitude = 1
begin_time=0					                                                 
end_time=1       							               
signalFrequency= 1
                                                
time =np.linspace(begin_time, end_time, 101)
print(len(time))
sampling_interval=time[1]-time[0]

sine_wave = amplitude*np.sin(2*np.pi* signalFrequency *time)

params = {'legend.fontsize': '20',
          'font.family': 'Times New Roman Bold',
          'font.size': '15',
          'axes.labelsize': 'x-large',
          'axes.labelweight': 'bold',
          'axes.titlesize':'x-large',
          'xtick.labelsize':'x-large',
          'ytick.labelsize':'x-large',
          'font.weight':'bold'}

plt.rcParams.update(params)
plt.figure(1)
plt.xlabel('Time[s]')
plt.ylabel('Amplitude')
print(time)
plt.plot(time, sine_wave, color='red',linewidth=4.0,label='Time vs Amplitude')
plt.xticks(np.arange(0, max(time)+0.25, 0.25))
ymax = 1.0
xmax = 0.25
plt.annotate('Peak', xy=(xmax, ymax), xytext=(xmax, ymax + 0.25),arrowprops=dict(arrowstyle = '-', connectionstyle = 'arc3',facecolor='red'))
plt.legend()

z1= 2*np.pi*signalFrequency*time
z2= z1*180/np.pi
df = pd.DataFrame({"Time[s]" : time, "Sine Function" : sine_wave,"Radians":z1,"Degrees":z2})
df.to_csv("SineWave.csv", index=False)

fft_amplitude=2.0*np.abs(fftpack.fft(sine_wave)/len(time))
fft_freqs=fftpack.fftfreq(len(time),sampling_interval)


print(fft_freqs)
mask = fft_freqs > 0
plt.figure(2)
plt.tick_params
plt.xlabel('Frequency[Hz]')
print(len(fft_freqs[mask]))
plt.ylabel('Amplitude')
plt.stem(fft_freqs[mask], fft_amplitude[mask],label="Frequency vs Amplitude",use_line_collection=True)
plt.legend()

df = pd.DataFrame({"Frequency[Hz]" : fft_freqs[mask],"FFT Amplitude":fft_amplitude[mask]})
df.to_csv("FFTSineWave.csv", index=False)
