from __future__ import print_function
from __future__ import division

import os
from string import Template
import cantera as ct
import numpy as np

import soln2ck_uq

sens_index = [1, 2, 5]

gas = ct.Solution('gri30.cti')
thermo_data = 'mech/thermo30.dat'
transport_data = "mech/transport.dat"
factor = np.ones(gas.n_reactions)
fname = 'output/hashemi2016_methane_'
output_file_name = soln2ck_uq.write(gas, factor=None, fname=fname)

for i in sens_index:
    i_reac = i - 1
    factor = np.ones(gas.n_reactions)
    factor[i_reac] = 1.5
    soln2ck_uq.write(gas, factor, fname=fname + str(i_reac))
    os.system("ck2cti --input=" + fname+str(i_reac) +
              " --thermo="+thermo_data+" --transport="+transport_data+" --output="+fname+str(i_reac))
