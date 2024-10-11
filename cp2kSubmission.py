# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:36:04 2024

@author: Shiqing
"""

import os

# 获取当前目录下的所有 .inp 文件
inp_files = [f for f in os.listdir('.') if f.endswith('.inp')]

# 创建 justSub.sh 文件
with open('justSub.sh', 'w') as just_sub_file:
    for inp_file in inp_files:
        # 去掉 .inp 后缀，获取文件名
        job_name = inp_file[:-4]
        
        # 创建对应的 .sh 文件
        sh_file_name = f'{job_name}.sh'
        with open(sh_file_name, 'w') as sh_file:
            sh_file.write(f'#!/bin/bash\n')
            sh_file.write(f'#SBATCH --job-name={job_name}\n')
            sh_file.write(f'#SBATCH --comment=chem_yangroup\n')
            sh_file.write(f'#SBATCH --partition=cpu40c\n')
            sh_file.write(f'#SBATCH --nodes=1\n')
            sh_file.write(f'#SBATCH --ntasks=40\n')
            sh_file.write(f'####SBATCH --time=200:00:00\n')
            sh_file.write(f'\n')
            sh_file.write(f'cp2k.ssmp -i {inp_file} -o {job_name}.out\n')
        
        # 将生成的 .sh 文件名添加到 justSub.sh 文件中
        just_sub_file.write(f'sbatch {sh_file_name}\n')
