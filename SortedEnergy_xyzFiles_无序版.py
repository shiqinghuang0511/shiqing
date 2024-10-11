# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 17:43:39 2024

@author: Shiqing
"""

def read_xyz_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    frames = []
    energies = []
    i = 0
    while i < len(lines):
        atom_count = int(lines[i].strip())
        energy_line = lines[i + 1]
        energy = float(energy_line.split()[2])
        energies.append(energy)
        frame = lines[i:i + atom_count + 2]
        frames.append((energy, frame))
        i += atom_count + 2
    
    return frames

def filter_and_sort_conformations(frames, threshold):
    # Sort frames based on energy
    frames.sort(key=lambda x: x[0])
    
    # Filter frames within the energy threshold
    base_energy = frames[0][0]
    threshold_energy = base_energy + threshold
    
    filtered_frames = [frame for energy, frame in frames if energy <= threshold_energy]
    
    return filtered_frames

def write_xyz_file(filename, frames):
    with open(filename, 'w') as file:
        for frame in frames:
            for line in frame:
                file.write(line)

input_file = 'isomers.xyz'
output_file = 'filtered_cluster.xyz'
threshold = 0.0095616006  # energy difference in a.u.

frames = read_xyz_file(input_file)
filtered_frames = filter_and_sort_conformations(frames, threshold)
write_xyz_file(output_file, filtered_frames)

print(f'Filtered {len(filtered_frames)} conformations out of {len(frames)} based on energy threshold.')
