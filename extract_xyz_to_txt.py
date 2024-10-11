import os
import re

def extract_coordinates_and_name(log_file):
    coordinates = []
    atom_numbers = []
    molecule_name = os.path.basename(log_file).replace('.log', '')
    start_reading = False

    with open(log_file, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if "Standard orientation" in line:
            start_reading = True
            coordinates = []
            atom_numbers = []
            for j in range(i+5, len(lines)):  # Skip header and start reading coordinates
                if "---" in lines[j]:
                    break
                tokens = lines[j].split()
                if len(tokens) >= 6:
                    atom_numbers.append(tokens[1])  # Atom number
                    coordinates.append([float(tokens[3]), float(tokens[4]), float(tokens[5])])
        if start_reading and "---" in line:
            break

    return molecule_name, atom_numbers, coordinates

def write_to_txt():
    with open('optimized_coordinates.txt', 'w') as file:
        log_files = [f for f in os.listdir('.') if f.endswith('.log')]

        for log_file in log_files:
            molecule_name, atom_numbers, coordinates = extract_coordinates_and_name(log_file)

            # Write molecule name
            file.write(f'{molecule_name}\n')

            # Write coordinates and atom numbers
            if coordinates:
                for atom, coord in zip(atom_numbers, coordinates):
                    file.write(f'{atom} {coord[0]:.6f} {coord[1]:.6f} {coord[2]:.6f}\n')
            else:
                file.write('No optimized coordinates found\n')

            # Separate molecules with a blank line
            file.write('\n')

# Execute script
write_to_txt()
