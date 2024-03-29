# README Contents

This project contains the following Python files and data files:

## Python Files:

1. `main.py`: Contains the Traveling Salesman Problem (TSP) code, including a brute force algorithm and a heuristic algorithm.
2. `hcp.py`: Contains the reduction from Hamiltonian Circuit Problem (HCP) to TSP.
3. `vertexcovertoham.py`: Contains the reduction from Vertex Cover to HCP. To get the final TSP problem, run this code first, then run hcp.py.

## Data Files:

1. `travellingsalesman.dat`: This file has the input for the TSP problem and can be used to test the brute force and heuristic algorithms. It can be changed for different test cases.
2. `hamiltonian.dat`: This file is for the HCP to TSP reduction. hcp.py takes this file as input and produces hamiltoniantoTsp.dat, which contains the TSP problem after the reduction.
3. `vertexcover.dat`: This file contains the input for the Vertex Cover problem to be reduced to HCP. The Python file vertexcovertoham.py takes this file as input and produces vertextoHam.dat, which is then used as input for hcp.py. The output file hamiltoniantoTsp.dat can then be used as input for the TSP code.

# Problem Description

This project aims to solve the Traveling Salesman Problem (TSP) by reducing two NP-hard problems to TSP: the Hamiltonian Circuit Problem (HCP) and the Vertex Cover problem.

The TSP is an optimization problem in which a salesman must visit a given set of cities, each city exactly once, and return to the starting city, minimizing the total distance traveled. This problem is known to be NP-hard.

## Algorithms:

1. **Brute Force Algorithm**: This algorithm generates all possible permutations of the cities and calculates the total distance for each permutation, selecting the one with the minimum distance.

2. **Heuristic Algorithm**: This algorithm is a greedy approach that selects the nearest unvisited city at each step until all cities are visited, then returns to the starting city. This algorithm provides a near-optimal solution but may not always find the optimal solution.

# Build

The project can be run using Python 3. To run the different parts of the project, execute the following Python files:

1. For the TSP code, run `main.py`.
2. For the HCP to TSP reduction, run `hcp.py`.
3. For the Vertex Cover to HCP to TSP reduction, run `vertexcovertoham.py` followed by `hcp.py`.

# Test Cases:

Sample test cases for the Vertex Cover problem are provided in the following format:

```plaintext
<number_of_vertices>
<edge1_u> <edge1_v> <edge1_weight>
<edge2_u> <edge2_v> <edge2_weight>
...
$
```

**Different test cases can be created by modifying the input files:**

1. For the TSP algorithms, modify `travellingsalesman.dat`.
2. For the HCP to TSP reduction, modify `hamiltonian.dat`.
3. For the Vertex Cover to HCP to TSP reduction, modify `vertexcover.dat`.

**The following files are produced:**
1. The `hcp.py` produces `hamiltoniantoTsp.dat`, which contains the TSP problem after the reduction.
2. The `vertexcovertoham.py` produces `vertextoHam.dat`, which is then used as input for `hcp.py`. The output file `hamiltoniantoTsp.dat` can then be used as input for the TSP code in `main.py`.

# Data Sets:

The data sets provided in the .dat files serve as examples to test the implemented algorithms and reductions. You can change the content of these files to experiment with different problem instances and test the
performance of the algorithms.


# Limitations/Deficiencies:

1. The brute force algorithm for TSP has a high time complexity (O(n!)), which makes it impractical for solving large instances of the problem.
2. The heuristic algorithm, while more efficient than the brute force approach, may not always find the optimal solution.
3. The reductions from HCP to TSP and Vertex Cover to HCP to TSP add extra complexity to the problem, which may also impact the performance of the TSP algorithms when solving the transformed instances.

# Mappings:

1. **HCP to TSP**: The HCP is reduced to TSP by creating a complete graph where the weight of each edge corresponds to the distance between the two cities in the original problem. If an edge is not part of the original graph, its weight is set to a large value. Solving the TSP for this complete graph yields a Hamiltonian circuit in the original graph.

2. **Vertex Cover to HCP to TSP**: The Vertex Cover problem is first reduced to HCP by creating a Hamiltonian graph in which each vertex in the original graph is replaced by two vertices connected by an edge. Edges in the original graph are replaced by a pair of edges connecting the corresponding vertices in the Hamiltonian graph. Solving the HCP for this Hamiltonian graph provides a solution to the Vertex Cover problem. The HCP is then further reduced to TSP using the HCP to TSP mapping described above.

## Hamiltonian Circuit Problem to Traveling Salesman Problem

The Hamiltonian Circuit problem can be reduced to the TSP problem by converting the graph into a complete graph and setting the edge weights as follows:

1. If an edge exists between two vertices in the original graph, set the weight of the corresponding edge in the complete graph to 1.
2. If an edge does not exist between two vertices in the original graph, set the weight of the corresponding edge in the complete graph to a large value (e.g., M, where M is greater than the total number of vertices).
By doing this, we ensure that the optimal TSP solution will have a total cost less than or equal to the number of vertices in the graph, which corresponds to a Hamiltonian Circuit.

## Vertex Cover to Hamiltonian Circuit to Traveling Salesman Problem

The reduction from the Vertex Cover problem to the Hamiltonian Circuit problem can be explained as follows:

Given a graph G and an integer k, the goal is to construct a new graph G' such that G has a vertex cover of size k if and only if G' has a Hamiltonian Circuit. The reduction is based on the idea of constructing a "widget" for each edge in the graph G.

For each edge (u, v) in the graph G, create a widget with the following structure:

1. Make two copies of vertex u: u_1 and u_2.
2. Make two copies of vertex v: v_1 and v_2.
3. Connect u_1 to u_2, u_1 to v_2, u_2 to v_1, and v_1 to v_2.

In the new graph G', there are three ways to traverse the widget:

1. Enter from u_1, go somewhere else in the graph, and then come back through v_2.
2. Enter and exit through u_1 and u_2.
3. Enter and exit through v_1 and v_2.

By replacing each edge in G with a widget and making the proper connections, we can create a graph G' that has a Hamiltonian Circuit if and only if G has a vertex cover of size k. This transformation can be done in polynomial time, as it involves a linear number of operations based on the number of edges in the graph G.
Then we can apply the reduction from the Hamiltonian Circuit problem to the Traveling Salesman problem described above to solve the TSP problem, which will give the reduction from vertex cover to TSP. 