from states import *
import time
from pythonds.basic.stack import Stack
from levels import *
import math
from heuristics import *

def aStar(start, depth = 100):
    # Performs an astar algorithm search from the start state to the goal
    
    # Start Timer
    startTime = time.time()
    print("A* start")

    # Create Root node and add to stack
    root = Node(start, None, None, 0, 0)
    stack = [root]
    
    # Current node
    current=stack.pop(0)

    # Records all nodes already seen to avoid cicles
    seen = []
    seen.append(current)
    expanded_nodes = 0

    while objectiveTest(current.state) == False:
        # Gets all expanded nodes from current node
        expanded = expand_node(current)
        expanded_nodes += 1

        for x in expanded:
            # calculates heuristic = number of rows/columns inline with final destinations plus depth
            x.heuristic = heuristic1(x.state) + x.depth

            if any(y.state == x.state for y in seen) == False:
                # Adds to stack if hasn't already been seen
                stack.append(x)
                seen.append(x)
            for i in range(len(seen)):
                if x.state == seen[i].state and x.depth < seen[i].depth:
                    seen[i] = x
                    stack.append(x)
                    
        if len(stack) == 0:
            print("NONE")
            return None

        # Sorts stack by heuristic value and updates current node
        stack.sort(key = lambda x: x.heuristic)
        current = stack.pop(0)

    # Gets the resulting path
    path = []
    while current.parent is not None:
        path.insert(0, current.operator)
        current = current.parent

    # Calculates and prints the time
    endTime = time.time()
    timeElapsed = endTime - startTime

    # Prints time in a friendly way
    if timeElapsed>1:
        print("Time: " + str(round(timeElapsed, 3)) + "s")
    else:
        print("Time: " + str(round(timeElapsed*1000, 3)) + "ms")

    return path


    
    