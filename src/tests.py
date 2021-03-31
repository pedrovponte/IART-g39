from uniform_cost import *
from bfs import *
from greedy import *
from dfs import *
from aStar import *
from iterativeDeepening import *
from levels import *
import pandas as pd

    
levels = [level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12, level13, level14, level15, level16, level17, level18, level19, level20]

def tests():
    i = 0
    dicTime = {}
    for level in levels:
        i += 1
        print(i)
        dicLevel = {}
        pathBFS, timeBFS = bfs(level)
        pathDFS, timeDFS = dfs(level)
        pathUC, timeUC = uniform_cost(level)
        pathID, timeID = iterativeDeepening(level)
        pathG, timeG = greedy(level)
        pathA, timeA = aStar(level)
        
        dicLevel['BFS'] = timeBFS
        dicLevel['DFS'] = timeDFS
        dicLevel['Uniform Cost'] = timeUC
        dicLevel['Iterative Deepening'] = timeID
        dicLevel['Greedy'] = timeG
        dicLevel['A*'] = timeA
        
        dicTime['Level ' + str(i)] = dicLevel
        
    print(dicTime)
    times_data = pd.DataFrame(dicTime)
    file_name = '../docs/export_python.xlsx'
    times_data.to_excel(file_name)
    
tests()
        
        
        
        