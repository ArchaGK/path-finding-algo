"""
This implementation is done a learning activity
to learn Astar algorithm.
source: https://www.redblobgames.com/
"""

from path_finding_algorithms import Helper_functions as hf

GraphMap = hf.GridWithWeights(10, 10)
GraphMap.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
GraphMap.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
                                       (4, 3), (4, 4), (4, 5), (4, 6),
                                       (4, 7), (4, 8), (5, 1), (5, 2),
                                       (5, 3), (5, 4), (5, 5), (5, 6),
                                       (5, 7), (5, 8), (6, 2), (6, 3),
                                       (6, 4), (6, 5), (6, 6), (6, 7),
                                       (7, 3), (7, 4), (7, 5)]}


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph, start, goal):
    frontier = hf.PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far

start, goal = (1, 2), (7, 8)
came_from, cost_so_far = a_star_search(GraphMap, start, goal)
hf.draw_grid(GraphMap, width=3, point_to=came_from, start=start, goal=goal)
print()
hf.draw_grid(GraphMap, width=3, number=cost_so_far, start=start, goal=goal)
print()
print()
hf.draw_grid(GraphMap, width=3, path=hf.reconstruct_path(came_from, start=(1, 2), goal=(7, 8)))