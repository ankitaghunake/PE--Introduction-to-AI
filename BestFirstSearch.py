import heapq

def best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = []  # priority queue: (heuristic, node)
    heapq.heappush(pq, (heuristic[start], start))

    while pq:
        h, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        print(current, end=" ")

        if current == goal:
            print("\nGoal reached!")
            return

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

# User input for graph
n = int(input("Enter number of vertices: "))
graph = {}

print("Enter node names:")
nodes = [input(f"Node {i+1}: ") for i in range(n)]

e = int(input("Enter number of edges: "))
print("Enter edges (u v):")
for _ in range(e):
    u, v = input().split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)  # undirected

# User input for heuristic values
heuristic = {}
print("Enter heuristic values for each node (estimated cost to goal):")
for node in nodes:
    h = int(input(f"h({node}) = "))
    heuristic[node] = h

# Start and goal nodes
start_node = input("Enter start node: ")
goal_node = input("Enter goal node: ")

print("\nBest-First Search traversal:")
best_first_search(graph, start_node, goal_node, heuristic)