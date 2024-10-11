import os
import glob
import pandas as pd


energy_last_list = []
name_list = []

for filenames in glob.glob('*.out'):
    with open(filenames, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    name_list.append(filenames[:-4])
    energy_all = []
    for line in lines:
        if 'FINAL SINGLE' in line:
            energy_line = line
            words = energy_line.split(' ')
            energy = (words[-1])
            energy_all.append(energy)
    energy_last_list.append(energy_all[-1])

data = {'Filename':name_list,'SP(a.u.)':energy_last_list}
df = pd.DataFrame(data=data)
df.to_csv('-SP.csv',index = False)