import numpy as np
import matplotlib.pyplot as plt

#Plot up the spectrum of our object
data = np.genfromtxt('test.econ', usecols = [0,2])

#Convert units to wavelength
h = 6.62e-32
q = 1.6e-19
c = 3e8
ryd = 13.6

wl = h*c/(data[:,0]*ryd*q) *1e6

plt.loglog(wl, data[:,1])
