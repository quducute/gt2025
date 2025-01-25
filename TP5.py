import sys


def create_adjacency_matrix(edges, nodes):
    size = len(nodes)
    adjacency_matrix = [[float("inf")] * size for _ in range(size)]

    for i in range(size):
        adjacency_matrix[i][i] = 0

    for u, v, w in edges:
        adjacency_matrix[nodes.index(u)][nodes.index(v)] = w

    return adjacency_matrix


def dijkstra(adjacency_matrix, source, target, nodes):
    size = len(adjacency_matrix)
    visited = [False] * size
    distances = [float("inf")] * size
    previous_nodes = [-1] * size

    distances[nodes.index(source)] = 0

    for _ in range(size):
        min_distance = float("inf")
        current_node = -1

        for i in range(size):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                current_node = i

        if current_node == -1:
            break

        visited[current_node] = True

        for neighbor in range(size):
            if (
                adjacency_matrix[current_node][neighbor] != float("inf")
                and not visited[neighbor]
            ):
                new_distance = (
                    distances[current_node] + adjacency_matrix[current_node][neighbor]
                )
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_node

    path = []
    current = nodes.index(target)
    while current != -1:
        path.append(nodes[current])
        current = previous_nodes[current]

    path.reverse()
    return path, distances[nodes.index(target)]


nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "L", "M"]
edges = [
    ("A", "C", 8),
    ("A", "F", 7),
    ("A", "B", 4),
    ("B", "E", 3),
    ("C", "D", 5),
    ("C", "F", 1),
    ("D", "H", 7),
    ("E", "H", 2),
    ("F", "E", 3),
    ("F", "H", 6),
    ("G", "H", 3),
    ("G", "M", 4),
    ("H", "L", 6),
    ("L", "M", 1),
]

adjacency_matrix = create_adjacency_matrix(edges, nodes)

print("Adjacency Matrix:")
for row in adjacency_matrix:
    print(row)

source = input("Enter the source node: ").strip()
target = input("Enter the target node: ").strip()

if source not in nodes or target not in nodes:
    print("Invalid nodes.")
else:
    path, total_weight = dijkstra(adjacency_matrix, source, target, nodes)

    print("Shortest Path:", " -> ".join(path))
    print("Weighted Sum of Shortest Path:", total_weight)
