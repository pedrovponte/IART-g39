from states import *
import time
from pythonds.basic.stack import Stack
from levels import *
import math
from heuristics import *

def aStar(start, depth = 100):
    startTime = time.time()
    print("A* start")

    root = Node(start, None, None, 0, 0)
    stack = [root]

    root.heuristic = heuristic(root.state) + heuristic2(root.state) + heuristic3(root.state)
    visited = []
    depth = 1

    while stack:
        stack.sort(key = lambda x: x.heuristic)

        s = stack.pop(0)
        depth = s.depth

        if objectiveTest(s.state):
            path = []
            current = s
            while current is not None:
                path.append(current.operator)
                current = current.parent
                
            path.pop(len(path)-1) # delete None from array

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
                x.heuristic = s.heuristic + heuristic(x.state) + heuristic2(x.state) + heuristic3(x.state)
                stack.append(x)

            visited.append(s)    

# print(aStar(level11))

    
    