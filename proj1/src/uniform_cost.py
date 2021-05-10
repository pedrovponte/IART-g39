from states import *
import time
from pythonds.basic.stack import Stack
from levels import *


def uniform_cost(start):
    #Performs an uniform cost search from the start state to the goal

    # Start Timer
    startTime = time.time()
    print("Uniform cost start")

    # Vector with boards already seen, so there is no cicles
    visited = []

    # Initial node
    start_node = Node(start, None, None, 0, 0)

    # A list (in form of a stack) for the nodes.
    uc_stack = []
    uc_stack.append(start_node)

    # Current node
    current = uc_stack.pop(0)

    # Final path to be returned
    path = []

    visited.append(current.state)
    expanded_nodes = 0
    
    while(objectiveTest(current.state) != True):
        # Gets all the possible expandable nodes
        temp = expand_node(current)
        expanded_nodes += 1
        
        for item in temp:
            if item.state not in visited:
                visited.append(item.state)
                item.depth += current.depth
                uc_stack.append(item)

        # Sorts stack by depthh value and updates current node
        if len(uc_stack)!=0:
            uc_stack.sort(key = lambda x: x.depth)
            current = uc_stack.pop(0)
        else:
            return "No Soluction"
        
    # Records the path to be returned
    while(current.parent != None):
        path.insert(0, current.operator)
        current=current.parent

    # Calculates time of the function
    endTime = time.time()
    timeElapsed = endTime - startTime

    # Prints time in a friendly way
    if timeElapsed > 1:
        print("Time: " + str(round(timeElapsed, 3)) + "s")
    else:
        print("Time: " + str(round(timeElapsed*1000, 3)) + "ms")

    
    return path
