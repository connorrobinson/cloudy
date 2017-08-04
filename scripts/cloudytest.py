import matplotlib.pyplot as plt
import numpy as np
import pyCloudy as pc
import os

#pc.config.cloudy_exe = '/Users/Connor/Desktop/Research/cloudy/c17.00/.cloudy_bin/cloudy'
pc.config.cloudy_exe = '/Users/Connor/Desktop/Research/cloudy/c17.00/source/cloudy.exe'

radius = np.arange(12,14,1.0)

def make_model(name,rad):
    model = pc.CloudyInput('../models/{}_{}'.format(name, rad))
    model.set_BB(Teff = 4400, lumi_unit='Q(H)', lumi_value = 33.20)
    model.set_cste_density(10.5)
    model.set_radius(rad)
    #model.set_abund(predef='ism function sublimation', nograins=False, )
    model.set_grains(grains = 'ism function sublimation')
    model.set_other(('Cosmic Rays Background'))
    model.set_iterate(to_convergence = True)
    model.set_stop('zone 1')
    model.set_other('set dr 0')
    #model.set_stop('optical depth 0 at 5 microns')
    model.print_input()
    #model.set_other('save grain abundance ".grn" no hash')


name = 'pytest'

os.system('rm ../models/'+name+'.*')
pc.print_make_file('../models')



for rad in radius:
    make_model(name, rad)

#model.run_cloudy()
#pc.run_cloudy(dir_='../models', n_proc=3, use_make=True)

M = pc.CloudyModel('../models/'+name+'_12.0', read_emis = False, read_grains = True)

Ms = pc.load_models('../models/'+name+'_', read_emis=False, read_grains = True)
#M = pc.CloudyModel('/Users/Connor/Desktop/Research/cloudy/Project/models/pytest', read_emis=False)



