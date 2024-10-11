# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:06:00 2024

@author: Shiqing
"""

import os

# 指定文件夹路径
folder_path = 'C:/Users/Shiqing/OneDrive/YanGroup/yanxiaoyu/Simplified/gas_sp'

# 获取文件夹中的所有.gjf文件
files = [f for f in os.listdir(folder_path) if f.endswith('.gjf')]

for file in files:
    # 构建完整的文件路径
    file_path = os.path.join(folder_path, file)
    
    # 打开并读取文件
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # 只保留前四行，并在后面添加两个空行
    new_lines = lines[:4]
    
    # 将修改后的内容写回文件
    with open(file_path, 'w') as f:
        f.writelines(new_lines)

print("所有文件处理完毕!")
