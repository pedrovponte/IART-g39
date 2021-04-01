from dfs import dfs
from heuristics import *
from states import *
import time
from pythonds.basic.stack import Stack
from levels import *


def greedy(board):
    # Performs a greedy algorithm search from the start state to the goal

    # Start Timer
    startTime = time.time()
    print("Greedy Start")

    # Create Root node and add to stack
    root = Node(board, None, None, 0, 0)

    # A list (in form of a stack) for the nodes.
    greedy_stack = []
    greedy_stack.append(root)

    # Final path to be returned
    path = []

    # Current node
    current = greedy_stack.pop(0)
    current.heuristic = heuristic1(board)

    # Vector with boards already seen, so there is no cicles
    seen = []
    seen.append(current.state)   
    
    while(objectiveTest(current.state) != True):
        # Gets all the possible expandable nodes
        temp = expand_node(current)
        
        for item in temp:
            # calculates heuristic for each node in the stack
            item.heuristic = heuristic1(board) + item.depth
            # Check for cicles and repeated states
            if (item.state not in seen):
                greedy_stack.append(item)
            else:
                continue
        
        # Sorts stack by heuristic value and updates current node
        greedy_stack.sort(key = lambda x: x.heuristic)
        current = greedy_stack.pop(0)

        # Inserts node to seen list so it is not again
        seen.append(current.state)

    # Records the path to be returned
    while(current.parent != None):
        path.insert(0,current.operator)
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



# ===========================Test purposes=====================================
# 
print(greedy(level10))
# =============================================================================

