from dfs import dfs
from heuristics import *
from states import *
import time
from pythonds.basic.stack import Stack
from levels import *


def greedy(board):
    print("Greedy Start")
    startTime = time.time()

    root=Node(board, None, None, 0, 0)
    fringe=[]
    path=[]
    fringe.append(root)

    current=fringe.pop(0)
    current.heuristic=heuristic(board)

    seen = []
    seen.append(current.state)    
    
    while(objectiveTest(current.state)!=True):
        temp=expand_node(current)
        for item in temp:
            # Check for cicles and repeated states
            if (item.state not in seen and item.state not in fringe):
                fringe.append(item)
            else:
                continue
        for item in fringe:
            item.heuristic=heuristic(board)+heuristic2(board)+heuristic3(board)
        fringe.sort(key =lambda x: x.heuristic)
        current=fringe.pop(0)
        seen.append(current.state)
    while(current.parent!=None):
        path.insert(0,current.operator)
        current=current.parent

    endTime = time.time()

    timeElapsed = endTime - startTime

    if timeElapsed>1:
        print("Time: " + str(round(timeElapsed,3)) + "s")
    else:
        print("Time: " + str(round(timeElapsed*1000,3)) + "ms")

    return path



# =============================================================================
# 
# print(greedy(level20))
# =============================================================================

