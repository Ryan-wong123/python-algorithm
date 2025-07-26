import sys
import heapq

'''
    Complete deterministic version of Dijkstra's algorithm:
        �	Direct path preference: If a direct edge exists from start to end 
            with the shortest cost, it is chosen.
        �	Lexicographical tie-breaking: 
            . Among paths with equal cost, fewer nodes preferred
            . Otherwise lexicographically smallest path is selected.
'''

def dijkstra_enhanced(graph, start, end):
    """
     Enhanced deterministic Dijkstra:
    1. Lowest fare
    2. Fewest nodes
    3. Lexicographically smallest path
    """
    # Priority queue stores: (total_fare, number_of_nodes, path_so_far)
    queue = [(0, 1, [start])]  # Starting fare 0, 1 node in path, starting path

    visited = {}

    best_fare = float("inf")
    best_path = []

    while queue:
        current_fare, path_length, path = heapq.heappop(queue)
        current_node = path[-1]

        # Skip if we've already found a better path to this node
        if current_node in visited and visited[current_node] < current_fare:
            continue
        visited[current_node] = current_fare

        if current_node == end:
            if (current_fare < best_fare or
                (current_fare == best_fare and len(path) < len(best_path)) or
                (current_fare == best_fare and len(path) == len(best_path) and path < best_path)):
                best_fare = current_fare
                best_path = path
            continue

        for neighbor, weight in graph.get(current_node, {}).items():
            new_fare = current_fare + weight
            new_path = path + [neighbor]
            heapq.heappush(queue, (new_fare, len(new_path), new_path))

    if best_path:
        return best_fare, best_path
    return float("inf"), []


def parse_input(input_lines):
    """
    Convert input lines into a graph and identify start/end nodes.
    Each line except the last defines an edge: node1 node2 fare
    The last line defines the start and end nodes.
    """
    if len(input_lines) < 2:
        raise ValueError("Insufficient input data.")

    graph = {}
    for line in input_lines[:-1]:
        parts = line.strip().split()
        if len(parts) != 3:
            continue  # Skip malformed lines, lines that don't have exactly 3 parts
        node1, node2, fare = parts
        fare = int(fare)
        if node1 not in graph:
            graph[node1] = {}
        graph[node1][node2] = fare

    # Last line contains the start and end nodes
    start_end = input_lines[-1].strip().split()
    if len(start_end) != 2:
        raise ValueError("Last line must contain start and end nodes.")
    start, end = start_end

    return graph, start, end

def main():
    try:
        # Read input from file or standard input
        if len(sys.argv) == 2:
            with open(sys.argv[1]) as file:
                input_lines = file.readlines()
        else:
            input_lines = [line for line in sys.stdin]

        # Build the graph and get start/end nodes
        graph, start, end = parse_input(input_lines)

        # Run the enhanced Dijkstra algorithm
        fare, path = dijkstra_enhanced(graph, start, end)

        # Show the result
        if fare == float("inf"):
            print(f"No path found from {start} to {end}")
        else:
            print(f"Shortest path from {start} to {end}: {' -> '.join(path)} (Fare: {fare})")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
