#reduction of hamiltonian cycle problem to tsp - Anirudh Raghavan
def read_hamiltonian_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_nodes = int(lines[0].strip())
        edges = [tuple(map(int, line.strip().split())) for line in lines[1:] if line.strip() != '$']
    return num_nodes, edges

def hamiltonian_to_tsp(num_nodes, edges):
    tsp_values = []

    for i in range(1, num_nodes):
        for j in range(i + 1, num_nodes + 1):
            if (i, j) in edges or (j, i) in edges:
                weight = 1
            else:
                weight = num_nodes + 1  # Assign a large weight to non-existing edges
            tsp_values.append((i, j, weight))

    return tsp_values



def write_dat_file(file_path, tsp_values):
    with open(file_path, 'w') as file:
        file.write(f"{len(tsp_values)}\n")
        for value in tsp_values:
            file.write(f"{value[0]} {value[1]} {value[2]}\n")
        file.write("$\n")


# Read the Hamiltonian input file
hcp_file_path = 'vertextoHam.dat'
num_nodes, edges = read_hamiltonian_file(hcp_file_path)

# Convert the Hamiltonian instance to a TSP instance
tsp_values = hamiltonian_to_tsp(num_nodes, edges)

# Write the TSP instance to a file
tsp_file_path = 'hamiltoniantoTsp.dat'
write_dat_file(tsp_file_path, tsp_values)
