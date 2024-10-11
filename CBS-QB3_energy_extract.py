import os
import csv

def extract_energies(log_file):
    enthalpy = None
    free_energy = None
    with open(log_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "CBS-QB3 Enthalpy=" in line:
                enthalpy = float(line.split('=')[1].strip().split()[0])
            if "CBS-QB3 Free Energy=" in line:
                free_energy = float(line.split('=')[1].strip().split()[0])
    return enthalpy, free_energy

# 指定文件夹路径
folder_path = 'C:/Users/Shiqing/OneDrive/YanGroup/yanxiaoyu/Simplified/gas_sp'

# 获取文件夹中的所有.log文件
files = [f for f in os.listdir(folder_path) if f.endswith('.log')]

# 输出CSV文件的路径
output_csv = 'extracted_energies.csv'

# 创建并写入CSV文件
with open(output_csv, 'w', newline='') as csvfile:
    fieldnames = ['Filename', 'CBS-QB3 Enthalpy', 'CBS-QB3 Free Energy']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for file in files:
        file_path = os.path.join(folder_path, file)
        enthalpy, free_energy = extract_energies(file_path)
        writer.writerow({'Filename': file, 'CBS-QB3 Enthalpy': enthalpy, 'CBS-QB3 Free Energy': free_energy})

print(f"数据已提取并保存到 {output_csv}")
