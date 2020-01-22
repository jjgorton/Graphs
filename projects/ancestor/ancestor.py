from utils import Graph, Stack, Queue  # These may come in handy

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for vert in ancestors:
        graph.add_vertex(vert[0])
        graph.add_vertex(vert[1])

    for vert in ancestors:
        graph.add_edge(vert[1], vert[0])

    # print(graph.dft(starting_node))

    # print(graph.vertices)

    earliest = graph.bft(starting_node)[-1]
    if earliest == starting_node:
        return -1
    else:
        return earliest


# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# earliest_ancestor(test_ancestors, 8)

    