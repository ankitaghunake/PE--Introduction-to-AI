import heapq

def a_star(graph, heuristics, start, goal):
    pq = []
    heapq.heappush(pq, (0 + heuristics[start], 0, start, [start]))

    while pq:
        (est_total, cost, node, path) = heapq.heappop(pq)
        if node == goal:
            return path

        for neighbour, weight in graph[node]:
            new_cost = cost + weight
            est_total = new_cost + heuristics[neighbour]
            heapq.heappush(pq, (est_total, new_cost, neighbour, path + [neighbour]))

    return None

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristics = {'A': 6, 'B': 4, 'C': 2, 'D': 7, 'E': 3, 'F': 0}
print("A* Search Path:", a_star(graph, heuristics, 'A', 'F'))
