# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:14:04 2024

@author: Shiqing
"""

def remove_lines_with_characters(input_file, output_file, characters):
    """
    从输入文件中删除包含特定字符的行，并将结果写入输出文件。
    
    参数：
    input_file (str): 输入文件路径
    output_file (str): 输出文件路径
    characters (str): 要删除的行中包含的字符
    """
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if not any(char in line for char in characters):
                outfile.write(line)

# 使用示例
input_file = 'C:/Users/Shiqing/Desktop/test_pythonCodes/new-3.txt'
output_file = 'C:/Users/Shiqing/Desktop/test_pythonCodes/new-4.txt'
characters_to_remove = [' ! Normal Mode ', ' Name  Definition ', '--------']  # 替换为实际字符或字符串列表

remove_lines_with_characters(input_file, output_file, characters_to_remove)
