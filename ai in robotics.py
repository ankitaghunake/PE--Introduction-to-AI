import heapq

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pq = []
    heapq.heappush(pq, (0 + abs(start[0]-goal[0]) + abs(start[1]-goal[1]), 0, start, [start]))
    visited = set()

    while pq:
        (est_total, cost, (x, y), path) = heapq.heappop(pq)
        if (x, y) == goal:
            return path
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = cost + 1
                est_total = new_cost + abs(nx - goal[0]) + abs(ny - goal[1])
                heapq.heappush(pq, (est_total, new_cost, (nx, ny), path + [(nx, ny)]))
    return None

# 0 = free cell, 1 = obstacle
grid = [
    [0,0,0,0,1],
    [1,1,0,0,0],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,0,1,0]
]

start = (0,0)
goal = (4,4)

path = a_star(grid, start, goal)

print("🤖 AI Robotics Path Planning using A* Search")
print("Grid (0=Free, 1=Obstacle):")
for row in grid:
    print(row)

print(f"\nStart: {start} | Goal: {goal}")
print(f"Path found: {path}")
