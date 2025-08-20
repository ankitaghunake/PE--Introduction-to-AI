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
start = int(input("Enter starting node for DFS: "))

# DFS traversal
visited = [False] * n
stack = []

visited[start] = True
stack.append(start)

print("DFS Traversal:", end=" ")
while stack:
    curr = stack.pop()
    print(curr, end=" ")

    # Push neighbors in reverse order to match Java logic
    for i in range(n-1, -1, -1):
        if graph[curr][i] == 1 and not visited[i]:
            stack.append(i)
            visited[i] = True