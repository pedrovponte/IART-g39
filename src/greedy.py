from states import *
import time
from pythonds.basic.stack import Stack


def greedy(start):
    print("Greedy start")

    startTime = time.time()


    start_node=Node(start, None, None, 0, 0)
    fringe=[]
    path=[]
    fringe.append(start_node)
    current=fringe.pop(0)
    while(objectiveTest(current.state)!=True):
        fringe.extend(expand_node(current))
        for item in fringe:
            h(item)
        fringe.sort(key =lambda x: x.heuristic)
        current=fringe.pop(0)
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
# print(greedy([
#     ['X','-','-','IY'],
#     ['IB','-','-','-'],
#     ['X','FB','-','-'],
#     ['X','FY','-','-']
#     ]))
#
# print(greedy(level6))
# =============================================================================
