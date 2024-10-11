# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:00:00 2024

@author: Shiqing
"""

import os

# 读取初始gjf文件内容
with open('3c_scan.gjf', 'r') as file:
    lines = file.readlines()

# 定义扫描参数
atom1 = 16  # 键的第一个原子，移动它
atom2 = 17  # 键的第二个原子，保持不动

# 直接粘贴原子编号范围
connected_atoms_str = "10-15,21-23,25-30,42-47,51-62"
# 解析原子编号范围
connected_atoms = []
for part in connected_atoms_str.split(','):
    if '-' in part:
        start, end = map(int, part.split('-'))
        connected_atoms.extend(range(start, end + 1))
    else:
        connected_atoms.append(int(part))

step_size = 0.05  # 步长 (Å)
num_steps = 50  # 扫描的步数

# 生成多个文件夹以保存扫描结果
output_dir = "relax_scan_results"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 从坐标部分开始找到对应键的初始距离
def get_distance(atom1, atom2, coords):
    try:
        x1, y1, z1 = coords[atom1 - 1]  # 原子编号从1开始，Python列表从0开始
        x2, y2, z2 = coords[atom2 - 1]
    except IndexError:
        print(f"Error: One of the atom indices {atom1} or {atom2} is out of range.")
        return None
    return ((x2 - x1) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5

# 调整原子位置，保持原子17不动，同时移动与原子15相连的原子
def adjust_distance(coords, atom1, atom2, connected_atoms, new_distance):
    x1, y1, z1 = coords[atom1 - 1]  # 移动atom1
    x2, y2, z2 = coords[atom2 - 1]  # 固定atom2

    # 当前距离
    current_distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5

    # 计算比例因子
    scale = new_distance / current_distance

    # 根据比例因子调整atom1的位置
    new_x1 = x2 + (x1 - x2) * scale
    new_y1 = y2 + (y1 - y2) * scale
    new_z1 = z2 + (z1 - z2) * scale

    # 更新atom1的坐标
    coords[atom1 - 1] = [new_x1, new_y1, new_z1]

    # 计算原子15的位移量
    dx = new_x1 - x1
    dy = new_y1 - y1
    dz = new_z1 - z1

    # 移动与原子15相连的原子
    for atom in connected_atoms:
        x, y, z = coords[atom - 1]
        coords[atom - 1] = [x + dx, y + dy, z + dz]

    return coords

# 提取分子坐标
def extract_coords(lines):
    coords = []
    for line in lines:
        parts = line.split()
        if len(parts) == 4:  # 假设4列是x,y,z坐标
            try:
                coords.append([float(x) for x in parts[1:]])
            except ValueError:
                print(f"Error: Invalid line format in coordinates: {line}")
                return None
    return coords

# 更新坐标部分
def update_coords(lines, coords):
    new_lines = []
    coord_idx = 0
    for line in lines:
        parts = line.split()
        if len(parts) == 4:  # 更新x,y,z
            atom = parts[0]
            new_x, new_y, new_z = coords[coord_idx]
            new_lines.append(f"{atom:<2} {new_x:>14.8f} {new_y:>14.8f} {new_z:>14.8f}\n")
            coord_idx += 1
        else:
            new_lines.append(line)
    return new_lines

# 提取原子坐标
coords = extract_coords(lines)
if coords is None or len(coords) < max(atom1, atom2):
    print(f"Error: Atom indices {atom1} or {atom2} are out of range for the given coordinate set.")
else:
    # 获取原子初始距离
    initial_distance = get_distance(atom1, atom2, coords)
    if initial_distance is not None:
        print(f"Initial distance between atom {atom1} and {atom2}: {initial_distance:.4f} Å")

        # 生成多个输入文件
        for step in range(num_steps + 1):
            # 计算新的距离
            new_distance = initial_distance + step * step_size

            # 调整atom1的坐标，并同步移动相连的原子
            new_coords = adjust_distance(coords.copy(), atom1, atom2, connected_atoms, new_distance)

            # 更新gjf文件的坐标部分
            new_lines = update_coords(lines, new_coords)

            # 文件名
            output_file_name = f'scan_{step:02}.gjf'
            output_file = os.path.join(output_dir, output_file_name)

            # 在文件开头添加 %chk=xxx.chk
            new_lines.insert(0, f"%chk={output_file_name[:-4]}.chk\n")

            # 在文件末尾添加扫描指令
            new_lines.append("B 16 17 F\n\n")

            # 保存新的gjf文件
            with open(output_file, 'w') as file:
                file.writelines(new_lines)

            print(f"Generated: {output_file}")
