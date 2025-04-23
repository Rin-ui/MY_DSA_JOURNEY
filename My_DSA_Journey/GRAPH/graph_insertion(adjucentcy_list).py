def add_node(v):
    global graph
    if v in graph:
        print(v,"is already present in graph")
    else:
        graph[v] = []   # adding a new node means adding new key in the dictionary ,whose value is an empty list
def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"not present in graph")
    elif v2 not in graph:
        print(v2,"not in graph")
    else:
        graph[v1].append(v2) # accessing graph through key
        graph[v2].append(v1)
graph = { }
add_node("A")
add_node("B")
add_edge("A","B")
print(graph)