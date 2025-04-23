# Step 1:- imitialise 3 Global or class scope variables.
#n = int(input("number of nodes in a graph: "))
#graph = adjucency list representing a graph
#visited = [false, false,false.....]  .. size n  ( boolean list conatining true or false based on whether the node is visited or not)
# Step 2:-
#def dfs(at):
#    if visited[at]: return    (base case): to check if we visited this node, if yes , we have nothing to do, so return
 #   visited[at] = true        (else, mark the code as visited, therefore marked true )
  #  neighbour = graph[at]     (to explore all the neighbours of the node, which is into the adjucency list )
 #   for next in neighbour:     (pull all the neighbours of the node and explore them depth first, looping over each)
#        dfs(next)               (and re-calling, dfs for the next node to visit the neighbour of the newly visited node, thus the fuction calls recursively)
# Step 3:-  start dfs at node 0
#start_node = 0
#dfs(start_node)     dfs has only 1 argument which is the current node

n = int(input("number of nodes in a graph: "))
graph = {}   # adjucency list representing graph 
# list in Python is typically denoted by [ ]. However, in this case, we're representing the graph using an adjacency list, which is commonly implemented using a dictionary in Python rather than a list.

#Using a dictionary allows for more efficient access to the neighbors of each node. 
#Each key in the dictionary represents a node, and the corresponding value is a list of its adjacent nodes. 
#This structure is well-suited for graphs where the nodes are not necessarily numbered sequentially from 0 to n-1, which is often the case in real-world scenarios.
# g = {
#    0: [1, 2],
#    1: [3],
#    2: [4],
#    3: [],
#    4: [5],
#    5: []
# }
# In this example, node 0 is connected to nodes 1 and 2, node 1 is connected to node 3, and so on. 
#Using a dictionary allows us to easily access the neighbors of each node by their keys.
visited = [False] * n  # Boolean list containing True or False based on whether the node is visited or not
g = {
    0: [1, 2],  # Node 0 is connected to nodes 1 and 2
    1: [3],     # Node 1 is connected to node 3
    2: [4],     # Node 2 is connected to node 4
    3: [],      # Node 3 has no outgoing edges
    4: [5],     # Node 4 is connected to node 5
    5: []       # Node 5 has no outgoing edges
}
def dfs(at):
    if visited[at]:   # in visited listonly the visited nodes will be stored
        return
    else:
        visited[at] = True
        neighbours = graph[at]    # Certainly! In the line `neighbours = g[at]`, `g` is the dictionary representing the graph, and `at` is the current node for which we want to find the neighbors.

#Let's break down the line:

#- `g`: This is the adjacency list representation of the graph. It's a dictionary where each key represents a node in the graph, and the corresponding value is a list of nodes that are adjacent to that key node.

#- `at`: This variable represents the current node we are visiting during the DFS traversal.

#When we write `g[at]`, it means we are accessing the value associated with the key `at` in the dictionary `g`. In the context of an adjacency list, this operation returns the list of nodes that are adjacent to the current node `at`. These adjacent nodes are considered the neighbors of node `at`.

#So, `neighbours = g[at]` assigns the list of neighboring nodes of the current node `at` to the variable `neighbours`, allowing us to iterate over these neighbors in the subsequent loop to explore them further during the DFS traversal.
        for next_node in neighbours:
            dfs(next_node)  
# Start DFS at node 0
start_node = 0
dfs(start_node)
    




