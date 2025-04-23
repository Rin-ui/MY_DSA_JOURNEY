# add node and edge usinng adjucency matrix
def add_node(v):
    global node_count
    if v in nodes:
        print(v ,"is already present in graph")
    else:
        # on adding node , number of node increamented by 1
        node_count = node_count+1
        nodes.append(v)       # node list is modified, now we need to modify the matrix
        for n in graph:  # n is 1st row of the graph
            n.append(0) # adding a new column, adding 0 at the end of every row
        temp = []  # adding a new row
        for i in range(node_count):  # the row will have 0 initially, row will be equal to the no of nodes in the graph
            temp.append(0)
            graph.append(temp)
def add_edge(v1,v2):
    # check if the nodes inbetween what we will establish the nodes are present or not
    if v1 not in nodes:  # nodes is a list that contains all the nodes of the graph
        print(v1,"not present in graph")
    elif v2 not in nodes:
        print(v2,"not present in graph")
    else:
        index1 = nodes.index(v1)  # we use index() to get index from a list
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1


def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print ( graph[i][j], end = " ")
        print() # for printing list in new line

nodes = []   
graph = []
node_count = 0   # defined outside functio -> global variable... if we try to modify a global variable inside a function, it will give an error.
print("before adding nodes")
print(nodes)
print(graph)
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_edge("A","B")
add_edge("B","E")
add_edge("E","B")
add_edge("B","D")
add_edge("D","A")
add_edge("D","C")
add_edge("C","A")
add_edge("E","F")
print("after adding nodes")
print(nodes)
print(graph)  # in nested list form
print_graph()  # in matrix form
