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
        if 'SCF Done' in line:
            energy_line = line
            words = energy_line.split()
            energy = words[4]
            energy_all.append(energy)
    energy_last_list.append(energy_all[-1])
   

data = {'Filename':name_list,'Energy':energy_last_list}
df = pd.DataFrame(data=data)
df.to_csv('data.csv',index = False)