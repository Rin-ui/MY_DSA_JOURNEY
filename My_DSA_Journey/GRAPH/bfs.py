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

def print_graph(g):
    print("Graph:")
    for node, neighbours in g.items():
        print(node, "->", neighbours)

n = int(input("Enter number of nodes: "))
g = create_graph()
print_graph(g)
s = int(input("Enter starting node: "))
prev = bfs(s, g, n)
print("Previous nodes:", prev)
