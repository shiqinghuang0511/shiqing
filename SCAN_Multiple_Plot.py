# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 18:05:42 2024

@author: Shiqing
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 使用seaborn的默认样式
sns.set(style='whitegrid')

# 设置全局的字体和图表风格
plt.rcParams.update({
    'font.size': 12,
    'figure.figsize': (16, 12),  # 调整图像大小以适应所有子图
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 12,
    'lines.linewidth': 2,
    'lines.markersize': 6,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'figure.autolayout': True
})

# 获取当前文件夹下所有的txt文件
files = [f for f in os.listdir() if f.endswith('.txt')]
n_files = len(files)

# 计算子图的行列数，保证能放下所有图
n_cols = min(3, n_files)
n_rows = (n_files + n_cols - 1) // n_cols

# 创建一个包含所有子图的组合图
fig, axs = plt.subplots(n_rows, n_cols, figsize=(16, 12))

# 扁平化axs数组，以便于迭代，即使只有一行
axs = axs.flatten()

for i, file in enumerate(files):
    # 读取文件，跳过前四行，并使用正则表达式分隔列数据
    data = pd.read_csv(file, skiprows=4, delim_whitespace=True, names=['Scan Coordinate', 'Total Energy (KCal/Mol)'])
    
    # 绘制图表到对应的子图
    ax = axs[i]
    ax.plot(data['Scan Coordinate'], data['Total Energy (KCal/Mol)'], marker='o', color='blue', linestyle='-', label='Total Energy')
    
    # 设置标题和标签
    ax.set_title(f'Plot of {file}')
    ax.set_xlabel('Scan Coordinate')
    ax.set_ylabel('Total Energy (KCal/Mol)')
    
    # 添加网格线
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # 添加图例
    ax.legend(loc='best')
    
    # 增加次刻度线
    ax.minorticks_on()
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')

    # 美化边框
    for spine in ax.spines.values():
        spine.set_edgecolor('gray')
        spine.set_linewidth(0.5)

# 删除多余的空子图
for j in range(i + 1, len(axs)):
    fig.delaxes(axs[j])

# 保存整合后的高清图片
plt.savefig('combined_plot.tif', format='tif')
plt.close()
