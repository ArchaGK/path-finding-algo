"""
This implementation is done a learning activity
to learn BFS algorithm.
source: https://www.redblobgames.com/
"""
from path_finding_algorithms import Helper_functions as hf



base_graph = hf.SimpleGraph()

base_graph.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}

print (base_graph.edges)


def breadth_first_search_1(graph, start):
    # print out what we find
    frontier = hf.Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True

breadth_first_search_1(base_graph, 'A')

print()

breadth_first_search_1(base_graph, 'C')