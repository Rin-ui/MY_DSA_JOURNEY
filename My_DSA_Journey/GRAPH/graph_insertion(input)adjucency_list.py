def add_node(v):
    global graph
    if v in graph:
        print(v, "is already present in graph")
    else:
        graph[v] = []   # adding a new node means adding new key in the dictionary, whose value is an empty list

def add_edge(v1, v2):
    global graph
    if v1 not in graph:
        print(v1, "not present in graph")
    elif v2 not in graph:
        print(v2, "not in graph")
    else:
        graph[v1].append(v2)  # accessing graph through key
        graph[v2].append(v1)

graph = {}

# Take user input for nodes
while True:
    node = input("Enter a node (or type 'done' to finish adding nodes): ").strip()
    if node.lower() == 'done':
        break
    add_node(node)

# Take user input for edges
while True:
    edge_input = input("Enter an edge (or type 'done' to finish adding edges), e.g., 'A B': ").strip()
    if edge_input.lower() == 'done':
        break
    edge = edge_input.split()
    if len(edge) != 2:
        print("Invalid input. Please enter two nodes separated by a space.")
        continue
    add_edge(edge[0], edge[1])

print(graph)




# Enter a node (or type 'done' to finish adding nodes): A
#Enter a node (or type 'done' to finish adding nodes): B
#node (or type 'done' to finish adding nodes): D
#Enter a node (or type 'done' to finish adding nodes): E
#Enter a node (or type 'done' to finish adding nodes): F
#Enter a node (or type 'done' to finish adding nodes): done
#Enter an edge (or type 'done' to finish adding edges), e.g., 'A B': A B
#Enter an edge (or type 'done' to finish adding edges), e.g., 'A B': A C
#Enter an edge (or type 'done' to finish adding edges), e.g., 'A B': A D
#Enter an edge (or type 'done' to finish adding edges), e.g., 'A B': B E
#Enter an edge (or type 'done' to finish adding edges), e.g., 'A B': B D
#Enter an edge (or type 'done' to finish adding edges), e.g., 'A B': E D
#Enter an edge (or type 'done' to finish adding edges), e.g., 'A B': D C
#Enter an edge (or type 'done' to finish adding edges), e.g., 'A B': done
#{'A': ['B', 'C', 'D'], 'B': ['A', 'E', 'D'], 'C': ['A', 'D'], 'D': ['A', 'B', 'E', 'C'], 'E': ['B', 'D'], 'F': []}
#PS C:\Users\rajas\DSA(PY)>