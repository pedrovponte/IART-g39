from states import *
import time
from levels import *

def bfs(start):
    """Performs a breadth first search from the start state to the goal"""   

    startTime = time.time()
    print("BFS start")

    # A list (can act as a queue) for the nodes.

    start_node=Node(start, None, None, 0, 0)
    fringe=[]
    fringe.append(start_node)
    current=fringe.pop(0)
    path=[]
    
    while(objectiveTest(current.state)!=True):
        fringe.extend(expand_node(current))
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
'''print(bfs([
     		['X','-','-','IY'],
     		['IB','-','-','-'],
     		['X','FB','-','-'],
     		['X','FY','-','-']
 		]))'''
  
     
# test2 = [
#      		['-','-','-','FR'],
#      		['IR','-','X','-'],
#      		['X','IG','-','-'],
#      		['-','-','-','FG']
#  		]
# 
# print(bfs(test2))
# 
# 
# test3 = [
#     		['-','-','-','-','FB'],
#     		['-','-','IB','-','X'],
#     		['-','-','-','X','-'],
#      		['-','IB','X','-','FB'],
#             ['X', '-', '-', '-','-']
#  		]
#  
# print(bfs(test3))
#    
# print(bfs(level9))
# =============================================================================


