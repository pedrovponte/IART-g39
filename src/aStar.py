## More or less Working

from states import *
import time
from pythonds.basic.stack import Stack
from levels import *
import math
from heuristics import *

def aStar(start, depth = 100):
    # Start Timer
    startTime = time.time()
    print("A* start")

    # Create Root node and add to stack
    root = Node(start, None, None, 0, 0)
    stack = [root]
    
    current=stack.pop(0)

    # Records all nodes already seen
    seen = []
    seen.append(current)
    expanded_nodes = 0

    while objectiveTest(current.state) == False:
        # Gets all expanded nodes from current node
        expanded = expand_node(current)
        expanded_nodes += 1

        for x in expanded:
            # calculates heuristic = number of rows/columns inline with final destinations plus depth
            x.heuristic = heuristic(x.state) + x.depth

            if any(y.state == x.state for y in seen) == False:
                # Adds to stack if hasn't already been seen
                stack.append(x)
                seen.append(x)
            for i in range(len(seen)):
                if x.state == seen[i].state and x.depth<seen[i].depth:
                    seen[i] = x
                    stack.append(x)

        # Sorts stack by heuristic value and updates current node
        stack.sort(key = lambda x: x.heuristic)
        current = stack.pop(0)

    # Gets the resulting path
    path = []
    while current.parent is not None:
        path.insert(0, current.operator)
        current = current.parent

    endTime = time.time()

    # Calculates and prints the time
    timeElapsed = endTime - startTime

    if timeElapsed>1:
        print("Time: " + str(round(timeElapsed, 3)) + "s")
    else:
        print("Time: " + str(round(timeElapsed*1000, 3)) + "ms")

    
    return path
#    return str(round(timeElapsed,6))
#    return expanded_nodes

# print(aStar(level20))

    
    