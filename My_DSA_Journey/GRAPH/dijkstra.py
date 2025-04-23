from heapq import heappush, heappop
import itertools

class Graph:
    def __init__(self):
        self.adjacency_list = {}

class PriorityQueue:
    def __init__(self):
        self.pq = []  # List of entries in heap
        self.entry_finder = {}  # Mapping of tasks to entries
        self.counter = itertools.count()

    def __len__(self):
        return len(self.pq)

    def add_task(self, priority, task):
        if task in self.entry_finder:
            self.update_priority(priority, task)
            return
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def update_priority(self, priority, task):
        entry = self.entry_finder[task]
        entry[-1] = priority
        # Re-sort the heap
        self.pq.sort()

    def pop_task(self):
        while self.pq:
            priority, _, task = heappop(self.pq)
            del self.entry_finder[task]
            return priority, task
        raise KeyError("Pop from an empty priority queue")

def add_edge(graph, u, v, distance):
    if u in graph:
        graph[u].append((distance, v))
    else:
        graph[u] = [(distance, v)]

def adjacency_list():
    graph = {}
    edges = int(input("Enter number of edges: "))
    for _ in range(edges):
        u, v, distance = map(int, input("Enter edge (u v distance): ").split())
        add_edge(graph, u, v, distance)
    return graph

def dijkstra(graph, start):
    previous = {v: None for v in graph.keys()}
    visited = set()
    distance = {v: float("inf") for v in graph.keys()}
    distance[start] = 0
    queue = PriorityQueue()
    queue.add_task(0, start)
    while queue:
        remove_distance, remove = queue.pop_task()
        visited.add(remove)
        for dist, neighbor in graph[remove]:
            if neighbor in visited:
                continue
            new_distance = remove_distance + dist
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                previous[neighbor] = remove
                queue.add_task(new_distance, neighbor)
    return distance, previous

graph = adjacency_list()
print("Adjacency list representation of the graph:")
print(graph)

start_vertex = int(input("Enter the starting vertex: "))
distances, predecessors = dijkstra(graph, start_vertex)
print("Shortest distances from vertex", start_vertex)
print(distances)
print("Predecessors:")
print(predecessors)
