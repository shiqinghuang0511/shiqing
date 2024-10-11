import os

# Function to generate ORCA input file content
def generate_orca_input(xyz_filename, charge=0, multiplicity=1, method="PBE0", basis_set="def2-SVP",
                        nprocs=8, memory="4000", solvent="water"):
    # Read the content of the .xyz file
    with open(xyz_filename, 'r') as f:
        lines = f.readlines()

    # Extract the number of atoms and atomic coordinates
    num_atoms = int(lines[0].strip())
    coordinates = lines[2:num_atoms + 2]  # Skip first two lines (number of atoms and comment)

    # Create the ORCA input content
    input_content = f"""!{method} {basis_set} Opt D3 freq def2/J tightSCF 
%maxcore {memory}
%pal nprocs {nprocs} end
%cpcm smd true
  SMDsolvent "{solvent}"
end
%geom Calc_Hess true end
* xyz {charge} {multiplicity}
"""
    input_content += "".join(coordinates)
    input_content += "*\n"

    return input_content

# Bash script content for submission
bash_script_content = "#!/bin/bash\n\n"

# Iterate over all .xyz files in the current directory
for xyz_file in os.listdir("."):
    if xyz_file.endswith(".xyz"):
        # Generate ORCA input content
        orca_input = generate_orca_input(xyz_file)

        # Determine the output filename
        inp_filename = os.path.splitext(xyz_file)[0] + ".inp"
        out_filename = os.path.splitext(xyz_file)[0] + ".out"

        # Write the ORCA input to a file
        with open(inp_filename, 'w') as f:
            f.write(orca_input)

        # Append to bash script for submission
        bash_script_content += f"/home/shiqing/hsq/software/orca600/orca {inp_filename} > {out_filename} &\n"

# Write the bash script to a file
bash_script_path = "submit_all.sh"
with open(bash_script_path, 'w') as f:
    f.write(bash_script_content)

# Make the bash script executable
os.chmod(bash_script_path, 0o755)

print("ORCA input files and submission script generated in the current directory.")
