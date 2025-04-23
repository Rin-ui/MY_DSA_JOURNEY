# Initialize global variables
n = int(input("Number of nodes in a graph: "))
g = {}  # Adjacency list representing a graph
visited = [False] * n  # Boolean list containing True or False based on whether the node is visited or not

# Populate the adjacency list
print("Enter edges as 'node1 node2 node3 ...' each line represents a node and its adjacent nodes (space-separated):")
for i in range(n): # The loop starting from for i in range(n): to g[i] = nodes[1:]: This loop iterates over each node in the graph and populates the adjacency list g. For each node, it reads input from the user representing the adjacent nodes, skips the first element (the current node itself), and stores the rest as adjacent nodes.
    nodes = list(map(int, input().split()))  # Certainly! Let's break down the line `nodes = list(map(int, input().split()))`:

#1.`input()`: This function reads a line of input from the user.

#2. `split()`: This method splits the input line into a list of strings, using whitespace (spaces, tabs, etc.) as the delimiter. For example, if the user inputs `"1 2 3"`, `split()` will produce `["1", "2", "3"]`.

#3. `map(int, ...)`: This is a built-in Python function that applies the `int()` function to each element in the iterable passed to it. In this case, it converts each string element from the split input into an integer. For example, `map(int, ["1", "2", "3"])` will produce an iterator containing `[1, 2, 3]`.

#4. `list(...)`: This converts the iterator returned by `map` into a list. This step is necessary because `map` returns an iterator object, and converting it to a list makes it more accessible for further manipulation. For example, `list(map(int, ["1", "2", "3"]))` will produce `[1, 2, 3]`.

#So, altogether, `nodes = list(map(int, input().split()))` reads a line of input from the user, splits it into substrings separated by whitespace, converts each substring into an integer, and stores the integers in a list named `nodes`. This is commonly used to process input containing space-separated integers into a list of integers for further use in the code.
# use of map function :- Map in Python is a function that works as an iterator to return a result after applying a function to every item of an iterable (tuple, lists, etc.). It is used when you want to apply a single transformation function to all the iterable elements. The iterable and function are passed as arguments to the map in Python.
    g[i] = nodes[1:]  # The first element is the node itself, so we skip it and store the adjacent nodes  ( we want to access the adjacent nodes not the currect node)
# The reason we skip the first element (nodes[0]) is that the first element represents the node i itself. In an adjacency list representation of a graph, we are interested in storing only the adjacent nodes, not the node itself.
def dfs(at, path=[]):
    if visited[at]:
        return
    visited[at] = True
    path.append(at)  # Append the current node to the path
    print("->".join(map(str, path)))  # Print the current path
    # print("->".join(map(str, path))): This line converts each element in the path list to a string, joins them with "->", and prints the resulting path. 
    #This prints the DFS path up to the current node.

#    The line `print("->".join(map(str, path)))` is a concise way to print the elements of the list `path` separated by `"->"`. Let's break it down:

#1. `map(str, path)`: This part of the line applies the `str()` function to each element in the list `path`. It converts each element from an integer to a string. For example, if `path` is `[1, 2, 3]`, `map(str, path)` will produce an iterator containing `['1', '2', '3']`.

#2. `"->".join(...)`: This part of the line joins the elements returned by `map(str, path)` using the string `"->"` as a separator. The `join()` method concatenates all the elements in the iterable (in this case, the list of strings) into a single string, using the specified separator between each pair of elements. For example, ` "->".join(['1', '2', '3'])` will produce the string `'1->2->3'`.

#3. `print(...)`: Finally, the `print()` function is used to output the resulting string to the console.

#So, altogether, `print("->".join(map(str, path)))` converts each integer element in the list `path` to a string, joins them together with `"->"`, and prints the resulting string. This is a compact way to print the elements of the list `path` separated by `"->"`. In the context of DFS traversal, this line prints the current path as the traversal progresses.
    neighbours = g.get(at, [])  # Get neighbors of the current node 'at'
    # neighbours = g.get(at, []): This line retrieves the adjacent nodes of the current node at from the adjacency list g. 
    #If the node at does not exist in the graph, it returns an empty list [].
    for next_node in neighbours:
        dfs(next_node, path)  # Pass the current path to the next node

# Start DFS at node 0
start_node = 0
dfs(start_node)
