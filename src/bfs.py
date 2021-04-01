from states import *
import time
from levels import *

def bfs(start):
    #Performs a breadth first search from the start state to the goal
    
    # Start Timer
    startTime = time.time()
    print("BFS start")
    
    # Vector with boards already seen, so there is no cicles
    seen = []
    
    # Initial node
    start_node = Node(start, None, None, 0, 0)
    
    # A list (in form of a stack) for the nodes.
    bfs_stack = []
    bfs_stack.append(start_node)

    # Current node
    current = bfs_stack.pop(0)

    # Final path to be returned
    path = []

    seen.append(current.state)    
    
    while(objectiveTest(current.state) != True):
        # Gets all the possible expandable nodes
        temp = expand_node(current)

        for item in temp:
            # Check for cicles and repeated states
            if (item.state not in seen):
                bfs_stack.append(item)
            else:
                continue

        # Updates current node
        current = bfs_stack.pop(0)

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
        print("Time: " + str(round(timeElapsed, 10)) + "s")
    else:
        print("Time: " + str(round(timeElapsed*1000, 3)) + "ms")

    return path


# ===========================Test purposes=====================================
# print(bfs([
#       		['X','-','-','IY'],
#       		['IB','-','-','-'],
#       		['X','FB','-','-'],
#       		['X','FY','-','-']
#   		]))
#    
# test2 = [
#       		['-','-','-','FR'],
#       		['IR','-','X','-'],
#       		['X','IG','-','-'],
#       		['-','-','-','FG']
#   		]
#  
# print(bfs(test2))
#  
#  
# test3 = [
#      		['-','-','-','-','FB'],
#      		['-','-','IB','-','X'],
#      		['-','-','-','X','-'],
#       		['-','IB','X','-','FB'],
#              ['X', '-', '-', '-','-']
#   		]
#   
# print(bfs(test3))
#     
# print(bfs(level20))
# 
# =============================================================================


