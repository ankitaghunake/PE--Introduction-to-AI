import heapq

def best_first_search(graph, heuristics, start, goal):
    visited = set()
    pq = []
    heapq.heappush(pq, (heuristics[start], start, [start]))

    while pq:
        (cost, node, path) = heapq.heappop(pq)
        if node == goal:
            return path

        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                heapq.heappush(pq, (heuristics[neighbour], neighbour, path + [neighbour]))

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristics = {'A': 6, 'B': 4, 'C': 2, 'D': 7, 'E': 3, 'F': 0}
print("Best First Search Path:", best_first_search(graph, heuristics, 'A', 'F'))
