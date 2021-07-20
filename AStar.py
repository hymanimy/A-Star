from Node import *

def heuristic(node1, node2):
    # currently manhattan distance
    x = abs(node1.r - node2.r) + abs(node1.c - node2.c)
    return x

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from.keys():
        current = came_from[current]
        path.append(current)
    return path[::-1]

def find_lowest_f_score(nodes):
    lowest_score = float('inf')
    lowest_node = None
    for node in nodes: 
        if node.fScore < lowest_score:
            lowest_score = node.fScore 
            lowest_node = node
    return lowest_node 


def a_star(grid, start, goal):
    open_set = {start} # set of nodes to be searched, may need expanded 
    came_from = dict() # dictionary which maps a node to the one which preceeds it (with the lowest cost)
    start.gScore = 0 # gScore is the cheapest known cost from the start to the current node 
    start.fScore = heuristic(start, goal)
    current = start

    while len(open_set) > 0:
        current = find_lowest_f_score(open_set)
        if current == goal:
            return reconstruct_path(came_from, current)

        open_set.remove(current)
        for neighbour in current.get_neighbours(grid):
            d = ((current.r - neighbour.r)**2 + (current.c - neighbour.c)**2)**0.5 # neighbours are 1 unit away from current 
            tentative_gScore = current.gScore + d # distance from start to the neighbour through current (may not be the best)
            if tentative_gScore < neighbour.gScore:
                came_from[neighbour] = current # if this is the best g score, go through current
                neighbour.gScore = tentative_gScore
                neighbour.fScore = neighbour.gScore + heuristic(neighbour, goal)
                if neighbour not in open_set: # line technically not needed but it is illustrative
                    open_set.add(neighbour)

    print("No path was found!")    
    return reconstruct_path(came_from, current) # show the final failing path

def show_solution(grid, start, goal, path):
    if path == None:
        path = []
    for row in grid:
        s = ""
        for node in row: 
            if node == start or node == goal:
                s += "o "
            elif node in path:
                s += "* "
            elif node.wall: 
                s += ". "
            else:
                s += "  "
        print(s)
    print()

if __name__ == "__main__":
    ROWS, COLS = 20, 20
    grid = [[Node(r, c) for c in range(COLS)] for r in range(ROWS)]
    start = grid[0][0]
    goal = grid[-1][-1]
    start.wall = False
    goal.wall = False
    solution_path = a_star(grid, start, goal)
    show_solution(grid, start, goal, solution_path)


