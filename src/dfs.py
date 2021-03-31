from states import *
import time
from levels import *

def dfs(start, depth=14):
    seen = []

    startTime = time.time()
    print("DFS start")

    start_node = Node(start, None, None, 0, 0)
    dfs_stack = []
    dfs_stack.append(start_node)
    current = dfs_stack.pop()
    path = []
    seen.append(current.state)

    while(objectiveTest(current.state) != True):
        temp = expand_node(current)
        #for i in temp:
        #    print(i.state)
        for item in temp:
            if (item.state not in seen):
                dfs_stack.insert(0,item)
            else:
                continue
        current = dfs_stack.pop()
        seen.append(current.state)
        while (current.depth > depth):
            if len(dfs_stack) == 0:
                return None
            current = dfs_stack.pop()

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
 #   return path, str(round(timeElapsed,6))



# =============================================================================
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



