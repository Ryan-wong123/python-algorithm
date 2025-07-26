import sys
from collections import defaultdict
import fileinput

'''
To ensure deterministic output in Kruskal-based clustering algorithms
—especially for autograders or reproducible research:

1. Edge Sorting Order: Sort edges by a 3-level key
    Primary: Edge weight (ascending)
    Secondary: Lexicographically smaller node
    Tertiary: Lexicographically larger node
    This ensures that ties in weights are broken consistently.
2. Cluster Formation: Remove the last (k - 1) edges added to the MST, 
                      assuming edges were added in sorted order.
    This is deterministic if:
        The MST edges are added in the same order every time 
        (which is guaranteed by the sorting rule above).
        You don't re-sort the MST before removing edges. 
3. Cluster Output Order: Sort clusters
    1. Descending size
    2. Lexicographically smallest node in the cluster
4. Node Representation: Ensure all node names are treated as case-sensitive 
                        strings and consistently formatted (e.g., no whitespace issues).

Summary of Deterministic Rules:
    Step	            Rule
    Edge Sorting	    (weight, min(u, v), max(u, v))
    MST Construction	Add edges in sorted order
    Edge Removal	    Remove last (k - 1) edges added to MST
    Cluster Sorting	    (-len(cluster), sorted(cluster))
    Node Sorting	    sorted(cluster)                                                             
'''

class UnionFind:
    def __init__(self, nodes):
        # Initializes each node as its own parent
        self.parent = {node: node for node in nodes}

    def find(self, x):
        #Finds the root of a node with path compression
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]] # Path compression
            x = self.parent[x]
        return x

    def union(self, x, y):
        # Merges two sets if they are disjoint
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.parent[px] = py
        return True

def kruskal_mst(edges, nodes):
    uf = UnionFind(nodes)
    mst = []

    # Sort edges deterministically by:
    # 1. Weight
    # 2. Lexicographically smaller node
    # 3. Lexicographically larger node
    sorted_edges = sorted(edges, key=lambda x: (x[0], min(x[1], x[2]), max(x[1], x[2])))

    # Adds edges until we form a spanning tree with (n - 1) edges
    for weight, u, v in sorted_edges:
        if uf.union(u, v):  # Only add edge if u and v are in different components
            mst.append((weight, u, v))
        if len(mst) == len(nodes) - 1:
            break

    return mst


# Remove the last k−1 edges to split MST into k clusters
def get_clusters_from_mst(mst, k, nodes):
    for _ in range(k - 1):
        if mst:
            mst.pop() # remove last-added edge

    # Rebuild clusters from remaining MST edges
    uf = UnionFind(nodes)
    for weight, u, v in mst:
        uf.union(u, v)

    # Group nodes by their root parent       
    clusters = defaultdict(list)
    for node in nodes:
        clusters[uf.find(node)].append(node)
        
    # Sorts clusters by:
    # 1. Size (descending)
    # 2. Lexicographically smallest node
    sorted_clusters = sorted(clusters.values(), key=lambda c: (-len(c), sorted(c)))
    return [sorted(cluster) for cluster in sorted_clusters]

if __name__ == "__main__":
    edges = []
    nodes = set()

    # Read from stdin or file
    input_lines = []
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as file:
            input_lines = file.readlines()
    else:
        input_lines = [line for line in sys.stdin]

    # Parse edges and node names
    k = int(input_lines[0])
    for line in input_lines[1:]:
        u, v, w = line.strip().split()
        edges.append((float(w), u, v))
        nodes.update([u, v])

    # Build MST and extracts clusters
    mst = kruskal_mst(edges, list(nodes))
    clusters = get_clusters_from_mst(mst, k, nodes)

    # Output the clusters
    print(f"Formed {k} clusters:")
    for idx, cluster in enumerate(clusters, 1):
        print(f"Cluster {idx}: {cluster}")