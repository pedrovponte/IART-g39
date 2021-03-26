from states import *
import time
from pythonds.basic.stack import Stack
from levels import *
import math

def aStar(start, depth = 100):
    goal = getGoalBoard(start)

    startTime = time.time()
    print("A* start")

    root = Node(start, None, None, 0, 0)
    stack = [root]

    root.heuristic = heuristic1(root.state, goal)
    visited = []
    depth = 1

    while stack:
        #print("visited: ", len(visited))
        #print("DEPTH: ", depth)
        stack.sort(key = lambda x: x.heuristic)

        s = stack.pop(0)
        depth = s.depth

        if objectiveTest(s.state):
            path = []
            current = s
            while current is not None:
                path.append(current.operator)
                current = current.parent
                # print("PATH: ", path)
            
            #print("LAST: ", path[len(path)-1])
            path.pop(len(path)-1)
            #print("NEW PATH: ", path)

            endTime = time.time()

            timeElapsed = endTime - startTime

            if timeElapsed>1:
                print("Time: " + str(round(timeElapsed,3)) + "s")
            else:
                print("Time: " + str(round(timeElapsed*1000,3)) + "ms")

            return path[::-1]

        if s not in visited:
            expanded = expand_node(s)

            for x in expanded:
                x.heuristic = s.heuristic + heuristic1(x.state, goal)
                stack.append(x)

            visited.append(s)    
    
            
def getGoalBoard(board):
    goal = []
    for row in board:
        goal_col = []
        for col in row:
            if col[0] == 'I':
                goal_col.append('-')
            elif col[0] == 'F':
                goal_col.append('I' + col[1] + col)
            else:
                goal_col.append(col)
        goal.append(goal_col)
    
    #print('GOAL: ', goal)
    return goal

            
def heuristic(board, goal):
    h = 0
    
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            bij = board[i][j]
            i_b = i
            j_b = j

            for i_g, r in enumerate(goal):
                for j_g, c in enumerate(r):
                    if c == bij:
                        h += (abs(i_g - i_b) + abs(j_g - j_b))

    return h

def heuristic1(board, goal):
    h = 0
    
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            bij = board[i][j]
            i_b = i
            j_b = j

            for i_g, r in enumerate(goal):
                for j_g, c in enumerate(r):
                    if c == bij:
                        h += math.ceil(math.sqrt((abs(i_g - i_b))**2 + (abs(j_g - j_b))**2))

    return h

# print(aStar(level6))
    
    