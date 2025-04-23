from collections import defaultdict

# Number of nodes
n = 8

# Corrected array of edges (assuming [3,7] instead of [3.7] and [5,2] was missing [])
A = [[0, 1], [1, 2], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# Initialize adjacency matrix with 0s
M = [[0]*n for _ in range(n)]

# Fill adjacency matrix for directed graph
for u, v in A:
    M[u][v] = 1

# For undirected graph, uncomment this too:
#     M[v][u] = 1

# Print adjacency matrix
print("Adjacency Matrix:")
for row in M:
    print(row)

# Initialize adjacency list using defaultdict
D = defaultdict(list)

# Fill adjacency list
for u, v in A:
    D[u].append(v)  # dict D at u (key) adds elements v which are connected by u 

# Print adjacency list
print("\nAdjacency List:")
for u in D:
    print(f"{u} -> {D[u]}")
