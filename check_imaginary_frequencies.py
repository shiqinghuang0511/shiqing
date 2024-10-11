# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:19:48 2024

@author: Shiqing
"""

import os

def check_imaginary_frequencies(log_file):
    with open(log_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "Frequencies --" in line:
                frequencies = line.split()[2:]
                for freq in frequencies:
                    if float(freq) < 0:
                        return True
    return False

# 指定文件夹路径
folder_path = 'C:/Users/Shiqing/OneDrive/YanGroup/yanxiaoyu/Simplified/gas_opt'

# 获取文件夹中的所有.log文件
files = [f for f in os.listdir(folder_path) if f.endswith('.log')]

# 检查每个文件是否含有虚频
for file in files:
    file_path = os.path.join(folder_path, file)
    has_imaginary = check_imaginary_frequencies(file_path)
    if has_imaginary:
        print(f"{file}: 含有虚频")
    else:
        print(f"{file}: 没有虚频")

print("检查完毕!")
