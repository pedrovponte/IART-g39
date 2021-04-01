from states import *
import time
from levels import *

def dfs(start, depth=14):
    #Performs a depth first search from the start state to the goal with depth of 14 or given number

    # Start Timer
    startTime = time.time()
    print("DFS start")

    # Vector with boards already seen, so there is no cicles
    seen = []

    # Initial node
    start_node = Node(start, None, None, 0, 0)

    # A list (in form of a stack) for the nodes.
    dfs_stack = []
    dfs_stack.append(start_node)

    # Current node
    current = dfs_stack.pop()

    # Final path to be returned
    path = []

    seen.append(current.state)

    while(objectiveTest(current.state) != True):
        # Gets all the possible expandable nodes
        temp = expand_node(current)

        for item in temp:
            # Check for cicles and repeated states
            if (item.state not in seen):
                dfs_stack.insert(0,item)
            else:
                continue
        
        # Updates current node
        current = dfs_stack.pop()

        # Inserts node to seen list so it is not again
        seen.append(current.state)

        # Checks if current node has a depth higher than the maximum given, if it is advances to the next
        while (current.depth > depth):
            # If the stack is empty than there is no soluction
            if len(dfs_stack) == 0:
                return None
            # Updates current node
            current = dfs_stack.pop()

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
# print(dfs([
# 		['X','-','-','IY'],
# 		['IB','-','-','-'],
# 		['X','FB','-','-'],
# 		['X','FY','-','-']
# 		]))
# 
# test2 = [
# 		['-','-','-','FR'],
# 		['IR','-','X','-'],
# 		['X','IG','-','-'],
# 		['-','-','-','FG']
# 		]
# print(dfs(test2))
# 
# test3 = [
# 		['-','-','-','-','FB'],
# 		['-','-','IB','-','X'],
# 		['-','-','-','X','-'],
# 		['-','IB','X','-','FB'],
#       ['X', '-', '-', '-','-']
# 		]
#  
# print(dfs(test3))
# 
# print(dfs(level20))
# =============================================================================



