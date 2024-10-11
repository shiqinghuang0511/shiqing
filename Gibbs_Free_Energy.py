import os
import glob
import pandas as pd


energy_last_list = []
name_list = []

for filenames in glob.glob('*.log'):
    with open(filenames) as f:
        lines = f.readlines()
    name_list.append(filenames[:-4])
    energy_all = []
    for line in lines:
        if 'Sum of electronic and thermal Free Energies=' in line:
            energy_line = line
            words = energy_line.split('=')
            energy = float(words[-1])
            energy_all.append(energy)
    energy_last_list.append(energy_all[-1])

data = {'Filename':name_list,'G(a.u.)':energy_last_list}
df = pd.DataFrame(data=data)
df.to_csv('-G.csv',index = False)