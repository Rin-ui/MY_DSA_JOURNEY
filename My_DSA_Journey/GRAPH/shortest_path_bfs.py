def bfs(s, g, n):   # s = starting node,  g = graph, n = number of nodes
    q = []
    enqueue(q, s)
    visited = [False]*n
    visited[s] = True
    prev = [None]*n
    while not isEmpty(q):
        node = dequeue(q)
        neighbours = g[node]
        for next_node in neighbours:
            if not visited[next_node]:
                enqueue(q, next_node)
                visited[next_node] = True
                prev[next_node] = node
    return prev

def enqueue(q, s):
    q.append(s)

def isEmpty(q):
    return len(q) == 0

def dequeue(q):
    return q.pop(0)

def add_edge(g,u,v):
    if u in g:
        g[u].append(v)
    else:
        g[u] = [v]

def create_graph():
    graph = {}
    edges = int(input("Enter number of edges: "))
    for _ in range(edges):
        u, v = map(int, input("Enter edge (u v): ").split())
        add_edge(graph, u, v)
    return graph 

n = int(input("Enter number of nodes: "))
g = create_graph()
s = int(input("Enter starting node: "))
prev = bfs(s, g, n)

def reconstructPath(s, e, prev):   # reconstructPath is a function that takes three arguments: s (the starting node), e (the ending node), and prev (the list of previous nodes obtained from BFS traversal).
    path = []    # It initializes an empty list path to store the reconstructed path.
    at = e           # Certainly! When we're reconstructing the path from the end node back to the start node, we need a way to keep track of the current node we're processing. 

# In this context, `at` is used as an iterator variable. It starts at the ending node `e`, which is the last node in the path. Then, as we traverse backwards through the path by following the `prev` pointers, `at` will be updated to the previous node of the current node in each iteration. 

# So, `at` essentially represents the current node being examined or processed during the reconstruction of the path. We start from the end node and trace back to the start node by following the `prev` pointers, updating `at` accordingly until we reach the start node.
    while at is not None:
        path.append(at)        # In the `reconstructPath` function, the line `path.append(at)` is used to add the current node (`at`) to the `path` list. 

# During the reconstruction process, we're traversing backward from the end node towards the start node. At each step, we add the current node to the `path` list because it's part of the reconstructed path. 

# By appending each node as we traverse backward, we effectively build the path in reverse order, starting from the end node and ending at the start node. Later, we reverse the list to obtain the correct order from the start node to the end node. 

# So, `path.append(at)` is crucial for accumulating the nodes in the reconstructed path during the backward traversal.
        at = prev[at]       # Update 'at' to its predecessor, obtained from the 'prev' list
    path.reverse()  # Reverse the path to obtain the correct order from 's' to 'e'
    if path[0] == s:  # Check if the first node in the path is indeed the starting node 's'
        return path    # If so, return the reconstructed path
    return []        # Otherwise, return an empty list indicating no valid path exists

start_node = int(input("Enter start node: "))
end_node = int(input("Enter end node: "))
path = reconstructPath(start_node, end_node, prev)
print("Shortest path:", path)

