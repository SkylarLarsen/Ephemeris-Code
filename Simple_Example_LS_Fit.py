import astropy
import astropy.timeseries
import astropy.units as u
import numpy as np
import matplotlib.pyplot as plt
import math as m
from astropy.timeseries import LombScargle

### Creation of Data ##############################################################################################
rand = np.random.RandomState(42)
t = 100 * rand.rand(100)
#print(t)
y = np.sin(2 * np.pi * t) + 0.1 * rand.randn(100)

frequency, power = LombScargle(t, y).autopower()
#plt.plot(frequency, power)  


### Preparation of Data############################################################################################
### Uncertainties
dy = 0.1 * (1 + rand.rand(100))
y = np.sin(2 * np.pi * t) + dy * rand.randn(100)
frequency, power = LombScargle(t, y, dy).autopower()


### Frequency (ask about this later!)
frequency, power = LombScargle(t, y, dy).autopower(nyquist_factor=10)
#print(len(frequency), frequency.min(), frequency.max())  
#plt.plot(frequency, power) 

### Units
t_days = t * u.day
y_mags = y * u.mag
dy_mags = y * u.mag
frequency, power = LombScargle(t_days, y_mags, dy_mags).autopower()
#print(frequency.unit)
#print(power.unit)
#plt.plot(frequency, power)  


### Grid Spacing
frequency, power = LombScargle(t, y, dy).autopower(minimum_frequency=0.1,maximum_frequency=1.9,samples_per_peak=10)
#print(len(frequency))
#plt.plot(frequency, power) 


### Creation of Phase Data ########################################################################################
best_frequency = frequency[np.argmax(power)]
print(best_frequency)
t_1 = 0
phase_data = []
period = 1 / best_frequency
for i in t: 
    #print(i)
    new_point = (i - t_1) % period
    phase_data.append(new_point)
#print(phase_data)
plt.scatter(phase_data,y)


### Lomb-Scargle Model ############################################################################################

t_fit = np.linspace(0, 1)
ls = LombScargle(t, y, dy)
y_fit = ls.model(t_fit, best_frequency)
plt.plot(t_fit, y_fit)
#print(y_fit)
#plt.xlim(0, 1)


### Plan B??? #####################################################################################################
#x = np.arange(0,1,0.01)
#y = np.sin(-((2*np.pi)/period) * x)
#plt.plot(x,y)

