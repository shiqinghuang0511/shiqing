# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:36:29 2024

@author: Shiqing
"""

import os

# 读取几何坐标输出文件
def read_geometry(file_path):
    atoms = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() and not line.startswith('#'):
                parts = line.split()
                atom = {
                    'element': parts[0],
                    'x': float(parts[1]),
                    'y': float(parts[2]),
                    'z': float(parts[3])
                }
                atoms.append(atom)
    return atoms

# 准备CP2K输入文件
def write_cp2k_input(atoms, output_path):
    with open(output_path, 'w') as file:
        file.write('&GLOBAL\n')
        file.write('  PROJECT my_project\n')
        file.write('  RUN_TYPE ENERGY\n')
        file.write('&END GLOBAL\n\n')

        file.write('&FORCE_EVAL\n')
        file.write('  METHOD QUICKSTEP\n')
        file.write('  &DFT\n')
        file.write('    BASIS_SET_FILE_NAME  BASIS_MOLOPT\n')
        file.write('    POTENTIAL_FILE_NAME  POTENTIAL\n')
        file.write('    &MGRID\n')
        file.write('      CUTOFF 400\n')
        file.write('    &END MGRID\n')
        file.write('    &XC\n')
        file.write('      &XC_FUNCTIONAL PBE\n')
        file.write('      &END XC_FUNCTIONAL\n')
        file.write('    &END XC\n')
        file.write('  &END DFT\n')
        file.write('  &SUBSYS\n')
        file.write('    &CELL\n')
        file.write('      ABC 10.0 10.0 10.0\n')
        file.write('    &END CELL\n')
        file.write('    &COORD\n')
        for atom in atoms:
            file.write(f'      {atom["element"]:2}  {atom["x"]:10.5f}  {atom["y"]:10.5f}  {atom["z"]:10.5f}\n')
        file.write('    &END COORD\n')
        file.write('    &KIND H\n')
        file.write('      BASIS_SET DZVP-MOLOPT-SR-GTH\n')
        file.write('      POTENTIAL GTH-PBE\n')
        file.write('    &END KIND\n')
        file.write('    &KIND C\n')
        file.write('      BASIS_SET DZVP-MOLOPT-SR-GTH\n')
        file.write('      POTENTIAL GTH-PBE\n')
        file.write('    &END KIND\n')
        file.write('  &END SUBSYS\n')
        file.write('&END FORCE_EVAL\n')

# 示例几何坐标输出文件路径
geometry_file_path = 'geometry.out'
# 生成的CP2K输入文件路径
cp2k_input_file_path = 'cp2k.inp'

# 读取几何坐标
atoms = read_geometry(geometry_file_path)
# 生成CP2K输入文件
write_cp2k_input(atoms, cp2k_input_file_path)

print(f'CP2K input file generated: {cp2k_input_file_path}')
