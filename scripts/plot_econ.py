import numpy as np
import matplotlib.pyplot as plt

#Plot up the spectrum of our object
data = np.genfromtxt('test.econ', usecols = [0,2])

AU = 1e13

#Get the information about the grid
height = 10**(np.genfromtxt('test.grd', usecols = 7))/AU

#Convert units to wavelength
h = 6.62e-34
q = 1.6e-19
c = 3e8
ryd = 13.6

conv = h*c/(ryd*q)

wl = conv/(data[:,0])*1e6
#wl = (h*c/(np.reshape(data[:,0], [len(radius), len(data)//len(radius)])*ryd*q))[0] * 1e6
#wl = (h*c/(np.reshape(data[:,0], [len(radius), len(data)//len(radius)])*ryd*q))[0]


#flux = np.reshape(data[:,1], [len(radius), len(data)//len(radius)])
flux = data[:,1]


#wl = h*c/(data[:,0]*ryd*q) *1e6
#plt.loglog(wl, flux)


for i in np.arange(12):
    plt.loglog(wl[int(i*len(wl)/12):int((i+1)*len(wl)/12)], flux[int(i*len(wl)/12):int((i+1)*len(wl)/12)]*5**i)

plt.show()

