import heapq

def a_star(graph, heuristics, start, goal):
    # Priority Queue: (total_cost, cost_so_far, node, path)
    pq = []
    heapq.heappush(pq, (heuristics[start], 0, start, [start]))

    while pq:
        (est_total, cost, node, path) = heapq.heappop(pq)

        # Goal Check
        if node == goal:
            return path, cost

        # Explore Neighbors
        for neighbor, weight in graph.get(node, []):
            new_cost = cost + weight
            est_total = new_cost + heuristics[neighbor]
            heapq.heappush(pq, (est_total, new_cost, neighbor, path + [neighbor]))

    return None, float('inf')


# Example Graph (Weighted)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values (Estimated distance to Goal)
heuristics = {'A': 6, 'B': 4, 'C': 2, 'D': 7, 'E': 3, 'F': 0}

# Run A* Search
path, cost = a_star(graph, heuristics, 'A', 'F')

# Attractive Output
print("🌟 A* Search Algorithm 🌟")
print("Graph:", graph)
print(f"\nPath found: {' → '.join(path)}")
print(f"Total Cost: {cost}")
