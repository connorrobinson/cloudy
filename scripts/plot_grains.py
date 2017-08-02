import numpy as np
import matplotlib.pyplot as plt

'''
plot_grains.py

PURPOSE:
    Script that plots grain abundance as a function of radius from the star


'''

path = '/Users/Connor/Desktop/Research/cloudy/Project/scripts/'
grainfile = 'test.grn'

rawdata = np.genfromtxt(path+grainfile, skip_header =1)

data = []

dist = np.arange(10,14.4,0.4)

for x in np.arange(len(rawdata)/3-1):
   data.append(rawdata[int(x)*3,:])
 
data = np.array(data)

AU = 1.5e13

plt.semilogx(10**dist/AU, data[:,-1])
plt.xlabel(r'Radius $[AU]$')
plt.ylabel(r'Grain abundance')
plt.show()