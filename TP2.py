import networkx as nx


def analyze_graph():
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

    weakly_connected_components = list(nx.weakly_connected_components(G))
    strongly_connected_components = list(nx.strongly_connected_components(G))

    print("Adjacency Matrix:")
    print(adj_matrix)

    print("\nWeakly Connected Components:")
    for component in weakly_connected_components:
        print(sorted(component))

    print("\nStrongly Connected Components:")
    for component in strongly_connected_components:
        print(sorted(component))


analyze_graph()
