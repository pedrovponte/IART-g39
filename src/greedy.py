from dfs import dfs
from states import *
import time
from pythonds.basic.stack import Stack
from levels import *



def h(state): #uma no sitio certo
    # print(state.state)
    dmatch=0
    for row in state.state:
        for cel in row:
            if(cel[0]=='F'):
                dmatch+=1
    state.heuristic=dmatch


def h2(state): #mesma linha ou mesma coluna
    dmatch=0
    for row in state.state:
        for cel in row:
            for cel2 in row:
                if(len(cel)==2 and len(cel2)==2):
                    if(cel[1]=='B' and cel[0]=='I' and cel2[1]=='B' and cel2[0]=='F'):
                        dmatch+=1
                    if(cel[1]=='O' and cel[0]=='I' and cel2[1]=='O' and cel2[0]=='F'):
                        dmatch+=1


    state.heuristic=dmatch



def greedy(start):
    print("Greedy Start")
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






    ######################################################################################################





# =============================================================================
# print(greedy([
#      ['X','-','-','IY'],
#      ['IB','-','-','-'],
#      ['X','FB','-','-'],
#      ['X','FY','-','-']
#      ]))
# 
# print(greedy(level3))
# =============================================================================

