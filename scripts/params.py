import numpy as np
import matplotlib.pyplot as plt

'''
params.py

PURPOSE:
    Calculate some basic parameters to use as inputs into cloudy

'''
#Define constants (all in SI units)
AU = 1.5e11
G = 6.67e-11
mh = 1.67e-27
k = 1.38e-23 

#Set up stellar/disk parameter
r = np.linspace(0,1,100)*AU 
M = 1.1 * 2e30
R = 1.7 * 6.96e8

#These can be solved for later, but assume reasonable things 
Rwall = .3 * AU
Twall = 1400

#Define the surface density of the disk (m^-2)
Sigma = 2e3 / 1e4

omega = np.sqrt(G*M/Rwall**3)
mh = 1.67e-27

#Calculate mean molecular mass, assuming that all the heavier stuff is in the grains. 
mu = (3/4 * .1 + 2 * .9)**-1 

cs = np.sqrt(k*Twall/(mu*mh))

h = cs/omega

rho0 = 1/np.sqrt(2*np.pi)*Sigma/h

n0 = rho0/(mu * mh)/1e6

#Load in the spectrum and scale it to the size of the star
path = '/Users/Connor/Desktop/Research/cloudy/Project/data/'
photfile = 'teff4400_logg4.0_meta0_cloudy.dat'

data = np.genfromtxt(path+photfile, usecols = [0,1])
energy = data[:,0]

ergstoryd = 4.587425e10

flux = data[:,1]  * ergstoryd

H_ionize = energy > 1

Q_H = 4*np.pi*R**2 * np.sum(flux[H_ionize]/(energy[H_ionize]))

#flux[H_ionize]



