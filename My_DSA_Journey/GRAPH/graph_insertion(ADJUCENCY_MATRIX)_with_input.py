def add_node(v):
    global node_count
    if v in nodes:
        print(v ,"is already present in graph")
    else:
        node_count = node_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"not present in graph")
    elif v2 not in nodes:
        print(v2,"not present in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()

nodes = []
graph = []
node_count = 0

print("Enter nodes separated by space:")
nodes_input = input().split()

for node in nodes_input:
    add_node(node)

print("Enter edges (node1 node2) separated by space (type 'done' when finished):")
while True:
    edge_input = input().split()    # edge_input = input().split(): This line prompts the user to input an edge, and input() function reads the input as a string. Then split() method splits the input string into a list of substrings based on whitespace. So, if the user inputs something like "A B", edge_input will be ['A', 'B'].
                                    # if edge_input[0] == 'done':: Here, the code checks if the first element of edge_input is equal to 'done'. This is done to allow the user to exit the input loop. If the user types 'done', the loop will break, and no further edges will be added.
    if edge_input[0] == 'done':
        break
    add_edge(edge_input[0], edge_input[1])   # edge_input[0]: This accesses the first element of the edge_input list, which corresponds to the first node of the edge entered by the user.
                                            # edge_input[1]: This accesses the second element of the edge_input list, which corresponds to the second node of the edge entered by the user.

print("Nodes after addition:")
print(nodes)
print("Graph adjacency matrix:")
print_graph()


#Enter nodes separated by space:
# A B C D
# Enter edges (node1 node2) separated by space (type 'done' when finished):
# A B
# B C
# C D
# done
# Nodes after addition:
# ['A', 'B', 'C', 'D']
# Graph adjacency matrix:
# 0 1 0 0 
# 1 0 1 0 
# 0 1 0 1 
# 0 0 1 0 
