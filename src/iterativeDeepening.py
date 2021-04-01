from states import *
import time
from levels import *

def iterativeDeepening(start, maxDepth=17):
    seen = []

    startTime = time.time()
    print("Iterative Deepening start")

    start_node = Node(start, None, None, 0, 0)
    it_stack = []
    it_stack.append(start_node)
    current = it_stack.pop()
    path = []
    seen.append(current.state)
    expanded_nodes = 0

    for i in range(maxDepth + 1):
        while objectiveTest(current.state) == False:
            temp = expand_node(current)
            expanded_nodes += 1
            
            for item in temp:
                if (item.depth <= i):
                    it_stack.insert(0, item)
                else:
                    continue
            if len(it_stack) != 0:
                current = it_stack.pop()
                seen.append(current.state)
            else:
                it_stack.append(start_node)
                seen = []
                break
        if (objectiveTest(current.state)):            
            break
        elif i == maxDepth:
            return "No Results Found"

    while(current.parent != None):
        path.insert(0, current.operator)
        current = current.parent

    endTime = time.time()

    timeElapsed = endTime - startTime

    if timeElapsed > 1:
        print("Time: " + str(round(timeElapsed, 3)) + "s")
    else:
        print("Time: " + str(round(timeElapsed*1000, 3)) + "ms")

    return path
#    return str(round(timeElapsed,6))
#    return expanded_nodes


# =============================================================================
# print(iterativeDeepening([
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
# print(iterativeDeepening(test2))
# 
# test3 = [
# 		['-','-','-','-','FB'],
# 		['-','-','IB','-','X'],
# 		['-','-','-','X','-'],
# 		['-','IB','X','-','FB'],
#       ['X', '-', '-', '-','-']
# 		]
#  
# print(iterativeDeepening(test3))
# 
# print(iterativeDeepening(level10))
# =============================================================================



