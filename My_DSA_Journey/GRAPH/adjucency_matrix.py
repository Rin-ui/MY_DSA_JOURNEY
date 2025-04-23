# Function to create an empty adjacency matrix
def create_empty_adj_matrix(n):
    return [[0] * n for _ in range(n)]

# Function to add an edge to the adjacency matrix
def add_edge(adj_matrix, u, v):
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1  # If the graph is undirected

# Function to create the graph based on user input
def create_graph():
    n = int(input("Enter the number of nodes: "))
    adj_matrix = create_empty_adj_matrix(n)
    edges = int(input("Enter the number of edges: "))
    for _ in range(edges):
        u, v = map(int, input("Enter edge (u v): ").split())
        add_edge(adj_matrix, u, v)
    return adj_matrix

# Example usage:
adj_matrix = create_graph()
print("Adjacency matrix representation of the graph:")
for row in adj_matrix:
    print(row)
