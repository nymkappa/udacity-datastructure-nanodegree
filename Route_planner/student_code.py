import math
import heapq           

# A* heuristic function
# Return the estimated distance between a node and the goal node (straight line)
def heuristic(location1, location2):
    distance_to_goal = math.sqrt(pow(location2[0] - location1[0], 2) +
                                 pow(location2[1] - location1[1], 2))
    return distance_to_goal
    

# A* algorythm implementation
# Inspired by:
#     - https://www.redblobgames.com/pathfinding/a-star/implementation.html
#     - https://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode
def shortest_path(M, start, goal):
    if start == goal:
        return [start]
    
    visited_cost = {} # stored visited nodes and their associated optimal cost
    visited_cost[start] = 0
    
    frontier = [] # priority queue
    heapq.heappush(frontier, (0, start))
    
    come_from = {} # Used to generate the path back once we reached our goal

    safe = 0
    while len(frontier) > 0:
        current = heapq.heappop(frontier)[1]

        # We reached our goal, and thanks to the min priority queue, we know it's
        # the optimal path, we are done
        if current == goal:
            break

        for intersection in M.roads[current]:
            distance_nodes = math.sqrt(pow(M.intersections[intersection][0] - M.intersections[current][0], 2) +
                                       pow(M.intersections[intersection][1] - M.intersections[current][1], 2))
            cost = visited_cost[current] + distance_nodes

            # Add the neighbor node to the priority queue when the new path is shorter
            # that previously computed
            if intersection not in visited_cost or cost < visited_cost[intersection]:
                visited_cost[intersection] = cost
                frontier_cost = cost + heuristic(M.intersections[intersection], M.intersections[goal])
                come_from[intersection] = current
                heapq.heappush(frontier, (frontier_cost, intersection))
                

    # Go backward until the starting point to generate the final path
    path = []
    while current in come_from:
        path.insert(0, come_from[current])
        current = come_from[current]
    if len(path) > 0:
        path.append(goal)
    
    return path