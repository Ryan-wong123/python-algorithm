# algorithms.py
from collections import deque
import heapq

# Helper: valid moves
DIRECTIONS = [(-1,0),(1,0),(0,-1),(0,1)]

def in_bounds(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def neighbors(grid, node):
    x, y = node
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if in_bounds(grid, nx, ny) and grid[nx][ny] != 1:
            yield (nx, ny)

# Reconstruct path from came_from
def reconstruct_path(came_from, end):
    path = []
    while end in came_from:
        path.append(end)
        end = came_from[end]
    return path[::-1]

# DFS (no backtracking)
def dfs(grid, start, end):
    stack = [start]
    came_from = {}
    visited = set([start])
    while stack:
        current = stack.pop()
        if current == end:
            return reconstruct_path(came_from, end)
        for n in neighbors(grid, current):
            if n not in visited:
                visited.add(n)
                came_from[n] = current
                stack.append(n)
    return []

# BFS
def bfs(grid, start, end):
    queue = deque([start])
    came_from = {}
    visited = set([start])
    while queue:
        current = queue.popleft()
        if current == end:
            return reconstruct_path(came_from, end)
        for n in neighbors(grid, current):
            if n not in visited:
                visited.add(n)
                came_from[n] = current
                queue.append(n)
    return []

# Dijkstra
def dijkstra(grid, start, end):
    heap = [(0, start)]
    came_from = {}
    cost = {start: 0}
    while heap:
        current_cost, current = heapq.heappop(heap)
        if current == end:
            return reconstruct_path(came_from, end)
        for n in neighbors(grid, current):
            new_cost = current_cost + 1
            if n not in cost or new_cost < cost[n]:
                cost[n] = new_cost
                came_from[n] = current
                heapq.heappush(heap, (new_cost, n))
    return []

# A* Search
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, end):
    open_set = [(heuristic(start, end), 0, start)]
    came_from = {}
    cost = {start: 0}
    while open_set:
        _, g, current = heapq.heappop(open_set)
        if current == end:
            return reconstruct_path(came_from, end)
        for n in neighbors(grid, current):
            new_cost = g + 1
            if n not in cost or new_cost < cost[n]:
                cost[n] = new_cost
                priority = new_cost + heuristic(n, end)
                came_from[n] = current
                heapq.heappush(open_set, (priority, new_cost, n))
    return []

# Backtracking (recursive)
def backtracking(grid, start, end):
    path = []
    visited = set()
    found = []

    def backtrack(pos):
        if pos == end:
            found.extend(path + [end])
            return True
        x, y = pos
        visited.add(pos)
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            next_pos = (nx, ny)
            if in_bounds(grid, nx, ny) and grid[nx][ny] != 1 and next_pos not in visited:
                path.append(next_pos)
                if backtrack(next_pos):
                    return True
                path.pop()
        visited.remove(pos)
        return False

    backtrack(start)
    return found
