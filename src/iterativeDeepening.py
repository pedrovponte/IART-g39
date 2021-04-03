from states import *
import time
from levels import *

def iterativeDeepening(start, maxDepth=17):
    # Performs an iteratice deepening algorithm search from the start state to the goal

    # Start Timer
    startTime = time.time()
    print("Iterative Deepening start")

    # Vector with boards already seen, so there is no cicles
    seen = []

    # Initial node
    start_node = Node(start, None, None, 0, 0)

    # A list (in form of a stack) for the nodes.
    it_stack = []
    it_stack.append(start_node)

    # Current node
    current = it_stack.pop()

    # Final path to be returned
    path = []

    seen.append(current.state)
    expanded_nodes = 0

    # Performs a seach for a soluction within the given depth
    for i in range(maxDepth + 1):
        # Searches for a soluction
        while objectiveTest(current.state) == False:
            # Gets all the possible expandable nodes
            temp = expand_node(current)
            expanded_nodes += 1
            
            # Adds to stack all nodes within the current depth limit
            for item in temp:
                if (item.depth <= i):
                    it_stack.insert(0, item)
                else:
                    continue
            
            # Verifies if there is any node to be analysed, otherwise cleans stack and seen list and moves to the following depth
            if len(it_stack) != 0:
                current = it_stack.pop()
                seen.append(current.state)
            else:
                it_stack.append(start_node)
                seen = []
                break
        
        # Verifies if the objective is reached, otherwise if the limit is reached there is no soluction
        if (objectiveTest(current.state)):            
            break
        elif i == maxDepth:
            return "No Results Found"

    # Records the path to be returned
    while(current.parent != None):
        path.insert(0, current.operator)
        current = current.parent

    # Calculates time of the function
    endTime = time.time()
    timeElapsed = endTime - startTime

    # Prints time in a friendly way
    if timeElapsed > 1:
        print("Time: " + str(round(timeElapsed, 3)) + "s")
    else:
        print("Time: " + str(round(timeElapsed*1000, 3)) + "ms")

    return path



