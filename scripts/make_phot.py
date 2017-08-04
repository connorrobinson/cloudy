import numpy as np
import matplotlib.pyplot as plt
import pdb

'''

make_phot.py

make: Converts nextgen photosphere spectra into something cloudy can use

'''

def bbstar_to_Q(T, R):
    '''
    Calculate Q(H), the ionizing luminosity for a blackbody based on temperature and radius
    
    INPUTS:
        T: temperature in kelvin
        R: Radius in solar radii
    
    '''
    #Define constants
    h = 6.6261e-27 #cgs
    c = 3e10 #cm/s
    k = 1.38e-16 #cgs
    Rsun = 6.96e10
    
    R_cm = R * Rsun
    
    #Set up wl array
    wl = 10**np.arange(0,14,0.01) * 1e-8 #cm
    
    #Planck's law
    B = (2*h*c**2/wl**5) * 1/(np.exp(h*c/(wl*k*T)) - 1) * wl
    B_flux = B * np.pi
    
    #Convert to rydbergs
    ergstoryd = 4.587425e10
    flux = B_flux*ergstoryd
    
    #Convert wl to energy
    energy = h*c/wl * ergstoryd
    
    #Find the ionizing flux and calculate Q
    H_ionize = energy > 1
    Q_H = 4*np.pi*R_cm**2 * np.sum(flux[H_ionize]/(energy[H_ionize]))
    
    return Q_H
    
    
    
def make(photfile, SEDpath, SEDfile):
    '''
    
    INPUTS:
        photfile: raw phot file from nextgen
        SEDpath: path to cloudy's /data/SED/ directory
        
    
    '''
    c = 3e18
    h = 6.626e-34
    rydberg = 13.6 * 1.6e-19
    
    data = np.genfromtxt(photfile, skip_header = 8)
    

    freq = c/data[:,0] 
    energy = h*freq/rydberg
    flux = data[:,1] * data[:,0]

    newfile = open(SEDpath+SEDfile, 'w')
    newfile.writelines("{:.5e}".format(energy[0]) + '\t' + "{:.5e}".format(flux[0]) + ' lambdaFlambda extrapolate\n' )
    
    for i in np.arange(len(energy)-1):
        newfile.writelines("{:.5e}".format(energy[i+1]) + '\t' + "{:.5e}".format(flux[i+1]) + '\n')
        
    newfile.close()
    return