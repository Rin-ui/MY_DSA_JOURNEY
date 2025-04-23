def add_edge(graph, u, v):
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]  # Initialize with a list
def create_graph():
    graph = {}
    edges = int(input("Enter number of edges: "))
    for _ in range(edges):
        u,v = map(int, input("Enter edge (u v) : ").split())
        add_edge(graph,u,v)
    return graph  # Corrected indentation
graph = create_graph()
print("Adjacency list representation of the graph:")
print(graph)
