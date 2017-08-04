import numpy as np
import matplotlib.pyplot as plt

'''
plot_grains.py

PURPOSE:
    Script that plots grain abundance as a function of radius from the star


'''

path = '/Users/Connor/Desktop/Research/cloudy/Project/scripts/'
grainfile = 'test.grn'
gridfile = 'test.grd'

rawdata = np.genfromtxt(path+grainfile, skip_header =1)

data = []

#dist = np.arange(10,14.4,0.1)
dist = np.genfromtxt(path+gridfile, usecols = [3,6], delimiter = '\t')[:,1]
err = np.genfromtxt(path+gridfile, usecols = [3,6], delimiter = '\t', dtype = 'str')[:,0]


good = np.where(err != '        cloudy abort')
dist = dist[good]


#for x in np.arange(len(rawdata)/3):
#   data.append(rawdata[int(x)*3,:])
 
#data = np.array(data)

AU = 1.5e13

#plt.loglog(10**dist/AU, data[:,-1])
plt.xscale('log')
plt.yscale('log')
plt.scatter(rawdata[:,0]/AU, rawdata[:,-1], s = 20)

plt.xlabel(r'Radius $[AU]$')
plt.ylabel(r'Grain abundance')
plt.show()