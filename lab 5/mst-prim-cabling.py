# mst-prism-cabling.py
import heapq
import sys

'''
To make Prim's algorithm deterministic:
    1. Sort neighbors in each adjacency list
    2. Use consistent tie-breaking in the heap
    3. Always start from the same node

Determinism Achieved By:
    Sorting neighbors by weight and name
    Starting from the smallest node
    Using consistent heap structure
'''

def prim_mst(num_nodes, edges):
    import heapq

    # Build the graph as an adjacency list
    graph = {}
    for u, v, w in edges:
        w = int(w)
        graph.setdefault(u, []).append((w, v))
        graph.setdefault(v, []).append((w, u))

    # Sort each adjacency list by weight, then lexicographically by node name
    for node in graph:
        graph[node].sort(key=lambda x: (x[0], x[1]))

    visited = set()
    mst_edges = []
    total_cost = 0

    # Start from the lexicographically smallest node
    start = min(graph.keys())
    min_heap = [(0, start, None)]  # (weight, to_node, from_node)

    while min_heap and len(visited) < num_nodes:
        weight, u, prev = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        if prev is not None:
            mst_edges.append((prev, u, weight))
            total_cost += weight
        for w, v in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v, u))

    # Print the MST edges and total cost
    for u, v, w in mst_edges:
        print(f"{u} -- {v} : {w}")
    print(f"Total Cost: {total_cost}")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        # Read from file passed as argument
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            num_nodes = int(file.readline())
            edges = [line.strip().split() for line in file]
    else:
        # Read from stdin (for autograder)
        lines = sys.stdin.read().strip().split('\n')
        num_nodes = int(lines[0])
        edges = [line.strip().split() for line in lines[1:]]

    prim_mst(num_nodes, edges)