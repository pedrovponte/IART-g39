from dfs import dfs
from heuristics import *
from states import *
import time
from pythonds.basic.stack import Stack
from levels import *


def greedy(board):
    print("Greedy Start")
    startTime = time.time()

    root = Node(board, None, None, 0, 0)
    greedy_stack = []
    path = []
    greedy_stack.append(root)

    current = greedy_stack.pop(0)
    current.heuristic = heuristic(board)

    seen = []
    seen.append(current.state)    
    
    while(objectiveTest(current.state) != True):
        temp = expand_node(current)
        for item in temp:
            # Check for cicles and repeated states
            if (item.state not in seen and item.state not in greedy_stack):
                greedy_stack.append(item)
            else:
                continue
        for item in greedy_stack:
            item.heuristic = heuristic(board)
        greedy_stack.sort(key = lambda x: x.heuristic)
        current = greedy_stack.pop(0)
        seen.append(current.state)
    while(current.parent != None):
        path.insert(0,current.operator)
        current = current.parent

    endTime = time.time()

    timeElapsed = endTime - startTime

    if timeElapsed > 1:
        print("Time: " + str(round(timeElapsed, 3)) + "s")
    else:
        print("Time: " + str(round(timeElapsed*1000, 3)) + "ms")

    return path
#    return path, str(round(timeElapsed,6))



# =============================================================================
# 
# print(greedy(level20))
# =============================================================================

