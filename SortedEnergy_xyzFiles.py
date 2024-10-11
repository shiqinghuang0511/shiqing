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
        frames.append(frame)
        i += atom_count + 2
    
    return energies, frames

def filter_conformations(energies, frames, threshold):
    threshold_energy = energies[0] + threshold
    filtered_energies = []
    filtered_frames = []
    
    for energy, frame in zip(energies, frames):
        if energy <= threshold_energy:
            filtered_energies.append(energy)
            filtered_frames.append(frame)
        else:
            break
    
    return filtered_energies, filtered_frames

def write_xyz_file(filename, frames):
    with open(filename, 'w') as file:
        for frame in frames:
            for line in frame:
                file.write(line)

input_file = 'cluster.xyz'
output_file = 'filtered_cluster.xyz'
threshold = 0.0095616006  # energy difference in a.u. 相当于6 kcal/mol; 如果想要10 kcal/mol, 请改为 0.015936001

energies, frames = read_xyz_file(input_file)
filtered_energies, filtered_frames = filter_conformations(energies, frames, threshold)
write_xyz_file(output_file, filtered_frames)

print(f'Filtered {len(filtered_frames)} conformations out of {len(frames)} based on energy threshold.')
