n = int(input("Number of nodes in a graph: "))
g = {}  # Adjacency list representing a graph
visited = [False] * n  # Boolean list containing True or False based on whether the node is visited or not
count = 0
components = []

def findComponent():
    for i in range(n):
        if not visited[i]:
            count = count + 1
            components.append([])
            dfs(i)
    return count, components

def dfs(at):
    visited[at] = True
    components[count - 1].append(at)
    for next_node in g[at]:
        if not visited[next_node]:
            dfs(next_node)

def printComponents():
    print("Connected Components:")
    for component in components:
        print(component)

# Example usage:
# Assuming g is a dictionary where keys are nodes and values are lists of adjacent nodes
# g = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
# Then call findComponent() after setting up your graph, it will return count and components.
# After that, call printComponents() to print the connected components.

        