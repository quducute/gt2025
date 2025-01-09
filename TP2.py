import networkx as nx

edges = [
    (1, 2),
    (1, 4),
    (2, 3),
    (2, 6),
    (3, 7),
    (3, 8),
    (4, 5),
    (5, 5),
    (5, 9),
    (6, 5),
    (6, 7),
    (7, 5),
    (7, 8),
    (8, 9),
]

G = nx.DiGraph()
G.add_edges_from(edges)

adj_matrix = nx.adjacency_matrix(G).todense()
print("Adjacency Matrix:")
print(adj_matrix)

weakly_connected = nx.number_weakly_connected_components(G)
strongly_connected = nx.number_strongly_connected_components(G)

print(f"Weakly Connected Components: {weakly_connected}")
print(f"Strongly Connected Components: {strongly_connected}")
