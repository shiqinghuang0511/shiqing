import os
import csv

# 获取当前目录下的所有 .out 文件
out_files = [f for f in os.listdir('.') if f.endswith('.out')]

# 初始化一个列表来存储每个文件的能量值
energy_data = [['FileName', 'Energy (a.u.)']]

# 定义要搜索的关键字
keyword = "Total energy:"

# 遍历每个 .out 文件
for out_file in out_files:
    with open(out_file, 'r') as file:
        lines = file.readlines()
        # 查找最后出现的能量值
        for line in reversed(lines):
            if keyword in line:
                # 提取能量值并添加到列表
                energy_value = line.split(keyword)[-1].strip()
                # 去掉文件名的后缀
                file_name_without_extension = os.path.splitext(out_file)[0]
                energy_data.append([file_name_without_extension, energy_value])
                break

# 将结果写入 cp2k_Energy.csv 文件
with open('cp2k_Energy.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(energy_data)

print("Energy values have been successfully extracted and saved to cp2k_Energy.csv")
