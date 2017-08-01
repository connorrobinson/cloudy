import numpy as np
import matplotlib.pyplot as plt
import pdb

'''

make_phot.py

make: Converts nextgen photosphere spectra into something cloudy can use

'''

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