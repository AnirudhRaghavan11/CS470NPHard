#Reduction of Vertex Cover to Hamiltonian Circuit - Anirudh Raghavan
#reads the instance of the vertex cover problem from the file
#extracts the number of verticies n from the first line
#reads the edges and stores them in a list of tuples
#stop when we hit the $ character
def read_vertex_cover(file):
    with open(file, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
        if '$' in lines:
            lines = lines[:lines.index('$')]
        n = int(lines[0])
        edges = [tuple(map(int, line.split())) for line in lines[1:]]
    return n, edges

#For each vertex u and its adjacent vertices v in the input graph G, it creates two copies of each vertex, u_prime_1, u_prime_2, v_prime_1, and v_prime_2.
#converts the vertex cover problem to a hamiltonian circuit problem
#takes the number of verticies n and the list of edges as input
def vertex_cover_to_hamiltonian(n, edges):
    G = {}
    for u, v, _ in edges:
        G[u] = G.get(u, []) + [v]
        G[v] = G.get(v, []) + [u]

    G_hamiltonian = {}
    for u, adj_list in G.items():
        for v in adj_list:
            u_prime_1, u_prime_2 = (u, "1"), (u, "2")
            v_prime_1, v_prime_2 = (v, "1"), (v, "2")

            if u_prime_1 not in G_hamiltonian:
                G_hamiltonian[u_prime_1] = []
            if u_prime_2 not in G_hamiltonian:
                G_hamiltonian[u_prime_2] = []
            if v_prime_1 not in G_hamiltonian:
                G_hamiltonian[v_prime_1] = []
            if v_prime_2 not in G_hamiltonian:
                G_hamiltonian[v_prime_2] = []

            G_hamiltonian[u_prime_1].append(u_prime_2)
            G_hamiltonian[u_prime_2].append(v_prime_1)
            G_hamiltonian[u_prime_1].append(v_prime_2)
            G_hamiltonian[v_prime_1].append(v_prime_2)

    return G_hamiltonian


def write_hamiltonian(file, G_hamiltonian):
    with open(file, 'w') as f:
        f.write(f"{len(G_hamiltonian)}\n")
        for u, adj_list in G_hamiltonian.items():
            for v in adj_list:
                f.write(f"{u[0]} {v[0]}\n")
        f.write("$\n")

# Read Vertex Cover problem from a file
n, edges = read_vertex_cover('vertexcover.dat')

# Convert Vertex Cover problem to Hamiltonian Circuit problem
G_hamiltonian = vertex_cover_to_hamiltonian(n, edges)

# Write the Hamiltonian Circuit problem to another file
write_hamiltonian('vertextoHam.dat', G_hamiltonian)
