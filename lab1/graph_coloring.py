def graph_coloring(graph, n):
    result = [-1] * n  # -1 means no color assigned yet
    result[0] = 0      # First vertex gets the first color (0)

    # Assign colors to remaining vertices
    for u in range(1, n):
        used_colors = set()

        # Check colors of adjacent vertices
        for neighbor in graph[u]:
            if result[neighbor] != -1:
                used_colors.add(result[neighbor])

        # Assign the smallest available color
        for color in range(n):
            if color not in used_colors:
                result[u] = color
                break

    # Output result
    print("Vertex\tColor")
    for u in range(n):
        print(f"{u}\t{result[u]}")
    
    print("Minimum number of colors required:", max(result) + 1)



def main():
    num_edges = int(input("Enter the number of edges: "))
    print("Enter each edge as two space-separated integers (e.g., '0 1'):")

    edges = []
    max_vertex = -1

    for _ in range(num_edges):
        u, v = map(int, input().split())
        edges.append((u, v))
        max_vertex = max(max_vertex, u, v)

    n = max_vertex + 1  # Total number of vertices
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Perform graph coloring
    graph_coloring(graph, n)

if __name__ == "__main__":
    main()