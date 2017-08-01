import numpy as np
import matplotlib.pyplot as plt
import pdb

'''

make_phot.py

Converts nextgen photosphere spectra into something cloudy can use


'''

#This is a comment

path = '/Users/Connor/Desktop/Research/cloudy/Project/data/'
photfile = 'teff4400_logg4.0_meta0.dat'
SEDpath = '/Users/Connor/Desktop/Research/cloudy/c17.00/data/SED/'
data = np.genfromtxt(path+photfile, skip_header = 8)

c = 3e18
h = 6.626e-34
rydberg = 13.6 * 1.6e-19

freq = c/data[:,0] 
energy = h*freq/rydberg
flux = data[:,1] * data[:,0]

newfile = open(SEDpath+'teff4400_logg4.0_meta0_cloudy.dat', 'w')
newfile.writelines("{:.5e}".format(energy[0]) + '\t' + "{:.5e}".format(flux[0]) + ' lambdaFlambda extrapolate\n' )

for i in np.arange(len(energy)-1):
    newfile.writelines("{:.5e}".format(energy[i+1]) + '\t' + "{:.5e}".format(flux[i+1]) + '\n')

newfile.close()



#np.savetxt(np.dstack(wl, flux))



