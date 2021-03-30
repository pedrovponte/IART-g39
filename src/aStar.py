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

    # Calculates heuristic of root - not needed
    # root.heuristic = heuristic(root.state) #+ heuristic2(root.state) + heuristic3(root.state)
    visited = []
    current=stack.pop(0)

    seen=[]
    seen.append(current.state)

    while objectiveTest(current.state)==False:
        expanded = expand_node(current)
        for x in expanded:
            x.heuristic = heuristic(x.state) + x.depth
            if x.state not in seen:
                stack.append(x)
                seen.append(x.state)
                #print(x.state)
                
        #print("----------------------------")
        '''for i in stack:
            print(i.state)'''
        #print("S")
        #print(seen)
        # Sort by heuristic value
        stack.sort(key = lambda x: x.heuristic)
        current = stack.pop(0)
    #print("H")
    path = []
    while current.parent is not None:
        path.insert(0,current.operator)
        current = current.parent

    endTime = time.time()

    timeElapsed = endTime - startTime

    if timeElapsed>1:
        print("Time: " + str(round(timeElapsed,3)) + "s")
    else:
        print("Time: " + str(round(timeElapsed*1000,3)) + "ms")

    return path

print(aStar(level18))

    
    