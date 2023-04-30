#travelling salesman problem - Anirudh Raghavan
import itertools
import matplotlib.pyplot as plt
import networkx as nx
import math

tsp_values = []
def read_dat_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_nodes = int(lines[0].strip())
        for line in lines[1:]:
            if line.strip() == '$':
                break
            values = line.strip().split()
            tsp_values.append((int(values[0]), int(values[1]), int(values[2])))
    return tsp_values

# ...

# Read the input .dat file
input_file = "hamiltoniantoTsp.dat"  # Replace with the path to your input .dat file
tsp_values = read_dat_file(input_file)

# ...
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def brute_force_tsp(tsp_values):
    tsp_size = len(tsp_values)
    min_cost = float('inf')
    optimal_path = []

    # Convert the tsp_values into a dictionary for easy lookup
    tsp_dict = {(i, j): w for i, j, w in tsp_values}
    tsp_dict.update({(j, i): w for i, j, w in tsp_values})

    nodes = set(i for i, j, w in tsp_values)
    for permutation in itertools.permutations(nodes):
        cost = sum(tsp_dict[(permutation[i], permutation[i + 1])] for i in range(len(permutation) - 1))
        cost += tsp_dict[(permutation[-1], permutation[0])]

        if cost < min_cost:
            min_cost = cost
            optimal_path = list(permutation)

    optimal_path.append(optimal_path[0])
    return optimal_path, min_cost


def nearest_neighbor_tsp(tsp_values):
    tsp_dict = {(a, b): w for a, b, w in tsp_values}
    tsp_dict.update({(b, a): w for a, b, w in tsp_values})

    nodes = sorted(set(a for a, b, w in tsp_values))
    unvisited = nodes.copy()
    start_node = unvisited.pop(0)
    path = [start_node]
    cost = 0

    while unvisited:
        min_distance = float('inf')
        nearest_neighbor = None

        for node in unvisited:
            distance = tsp_dict[(start_node, node)]
            if distance < min_distance:
                min_distance = distance
                nearest_neighbor = node

        cost += min_distance
        path.append(nearest_neighbor)
        unvisited.remove(nearest_neighbor)
        start_node = nearest_neighbor

    path.append(path[0])
    cost += tsp_dict[(start_node, path[0])]
    return path, cost


# Call the brute_force_tsp and nearest_neighbor_tsp functions here
optimal_path, optimal_cost = brute_force_tsp(tsp_values)
print(
    f"Certified optimal solution (brute force):\nTour: {' -> '.join(map(str, optimal_path))}\nCost: {optimal_cost:.2f}")

near_optimal_path, near_optimal_cost = nearest_neighbor_tsp(tsp_values)
print(
    f"\nNear-optimal solution (heuristic):\nTour: {' -> '.join(map(str, near_optimal_path))}\nCost: {near_optimal_cost:.2f}")

# Display the graph visualization here
# ...
def build_graph(tsp_values):
    G = nx.Graph()
    for i, j, w in tsp_values:
        G.add_edge(i, j, weight=w)
    return G

def visualize_tsp_solution(G, pos, path, title):
    path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='white', node_size=1200, font_size=16, font_color='black',
            font_weight='bold', edgecolors='black', linewidths=2)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='blue', width=2)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, font_color='black', font_weight='bold')
    plt.axis('off')
    plt.title(title)
    plt.show()

# Call the build_graph function here
G = build_graph(tsp_values)

# Since we don't have coordinates for the graph visualization, you can either provide them manually or use a layout algorithm
# Here, I'll use the spring layout algorithm from NetworkX
pos = nx.spring_layout(G, seed=42)

# Display the graph visualizations
visualize_tsp_solution(G, pos, optimal_path, 'Optimal TSP Solution (Brute Force)')
visualize_tsp_solution(G, pos, near_optimal_path, 'Near-optimal TSP Solution (Heuristic)')