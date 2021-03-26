from states import *
import time
from levels import *

def iterativeDeepening(start, maxDepth=17):
    seen = []

    startTime = time.time()
    print("Iterative Deepening start")

    start_node=Node(start, None, None, 0, 0)
    dfs_stack=[]
    dfs_stack.append(start_node)
    current=dfs_stack.pop()
    path=[]
    seen.append(current.state)

    for i in range(maxDepth+1):
        while objectiveTest(current.state)==False:
            temp=expand_node(current)
            for item in temp:
                if (item.depth<=i):
                    dfs_stack.insert(0,item)
                else:
                    continue
            if len(dfs_stack)!=0:
                current=dfs_stack.pop()
                seen.append(current.state)
            else:
                dfs_stack.append(start_node)
                seen=[]
                break
        if (objectiveTest(current.state)):            
            break
        elif i==maxDepth:
            return "No Results Found"

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



