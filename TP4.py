import heapq


def construct_adjacency_matrix():
    return [
        [0, 4, 0, 0, 2, 0, 0, 0, 0],
        [4, 0, 7, 0, 0, 5, 0, 0, 0],
        [0, 7, 0, 1, 0, 8, 0, 0, 0],
        [0, 0, 1, 0, 0, 6, 0, 3, 0],
        [2, 0, 0, 0, 0, 9, 10, 0, 0],
        [0, 5, 8, 6, 9, 0, 2, 0, 0],
        [0, 0, 0, 0, 10, 2, 0, 8, 0],
        [0, 0, 0, 3, 0, 0, 8, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
    ]


def prim_algorithm(matrix, root):
    n = len(matrix)
    visited = [False] * n
    edges = []
    min_heap = [(0, root, -1)]
    total_weight = 0

    while min_heap:
        weight, current_node, parent = heapq.heappop(min_heap)
        if visited[current_node]:
            continue

        visited[current_node] = True
        if parent != -1:
            edges.append((parent, current_node, weight))
            total_weight += weight

        for neighbor, edge_weight in enumerate(matrix[current_node]):
            if edge_weight > 0 and not visited[neighbor]:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_node))

    return edges, total_weight


def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def kruskal_algorithm(matrix):
    n = len(matrix)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] > 0:
                edges.append((matrix[i][j], i, j))

    edges.sort()
    parent = list(range(n))
    rank = [0] * n

    mst_edges = []
    total_weight = 0

    for weight, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_edges.append((u, v, weight))
            total_weight += weight

    return mst_edges, total_weight


matrix = construct_adjacency_matrix()
print("Adjacency Matrix:")
for row in matrix:
    print(row)

root = int(input("Enter the root node (0-indexed): "))

prim_mst, prim_weight = prim_algorithm(matrix, root)
print("\nPrim's MST:")
print("Edges:", prim_mst)
print("Total Weight:", prim_weight)

kruskal_mst, kruskal_weight = kruskal_algorithm(matrix)
print("\nKruskal's MST:")
print("Edges:", kruskal_mst)
print("Total Weight:", kruskal_weight)
