from collections import deque

# Input number of vertices
n = int(input("Enter number of vertices: "))

# Initialize adjacency matrix
graph = [[0 for _ in range(n)] for _ in range(n)]

# Input edges
e = int(input("Enter number of edges: "))
print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1  # undirected

# Input starting node
start = int(input("Enter starting node for BFS: "))

# BFS traversal
visited = [False] * n
queue = deque()

visited[start] = True
queue.append(start)

print("BFS Traversal:", end=" ")
while queue:
    curr = queue.popleft()
    print(curr, end=" ")

    for i in range(n):
        if graph[curr][i] == 1 and not visited[i]:
            queue.append(i)
            visited[i] = True