adjacency_matrix = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]


def inorder_traversal(node, adjacency_matrix, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    children = [
        i for i, is_edge in enumerate(adjacency_matrix[node - 1], start=1) if is_edge
    ]
    if len(children) > 0:
        inorder_traversal(children[0], adjacency_matrix, visited)
    print(node, end=" ")
    for child in children[1:]:
        inorder_traversal(child, adjacency_matrix, visited)


print("Adjacency Matrix:")
for row in adjacency_matrix:
    print(row)

print("\nInorder Traversal starting from Node 2:")
inorder_traversal(2, adjacency_matrix)
