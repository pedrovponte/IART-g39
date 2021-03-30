from states import *
import time
from pythonds.basic.stack import Stack
from levels import *


def uniform_cost(start):
    print("Uniform cost start")

    startTime = time.time()

    start_node=Node(start, None, None, 0, 0)
    fringe=[]
    visited = []
    path=[]
    fringe.append(start_node)
    current=fringe.pop(0)
    while(objectiveTest(current.state)!=True):
        temp=expand_node(current)
        for item in temp:
            if item.state not in visited:
                item.depth+=current.depth
                fringe.append(item)
        fringe.sort(key =lambda x: x.depth)
        current=fringe.pop(0)
        visited.append(current.state)
        
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
# print(uniform_cost([
#     ['X','-','-','IY'],
#     ['IB','-','-','-'],
#     ['X','FB','-','-'],
#     ['X','FY','-','-']
#     ]))
#    
# print(uniform_cost(level20))
# =============================================================================


