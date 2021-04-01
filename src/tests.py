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
# =============================================================================
#     i = 0
#     dicTime = {}
#     for level in levels:
#         i += 1
#         print(i)
#         dicLevel = {}
#         timeBFS = bfs(level)
#         timeDFS = dfs(level)
#         timeUC = uniform_cost(level)
#         timeID = iterativeDeepening(level)
#         timeG = greedy(level)
#         timeA = aStar(level)
#         
#         dicLevel['BFS'] = timeBFS
#         dicLevel['DFS'] = timeDFS
#         dicLevel['Uniform Cost'] = timeUC
#         dicLevel['Iterative Deepening'] = timeID
#         dicLevel['Greedy'] = timeG
#         dicLevel['A*'] = timeA
#         
#         dicTime['Level ' + str(i)] = dicLevel
#         
#     print(dicTime)
#     times_data = pd.DataFrame(dicTime)
#     file_name = '../docs/export_python_times.xlsx'
#     times_data.to_excel(file_name)
# =============================================================================
    
# =============================================================================
#     i = 0
#     dicPath = {}
#     for level in levels:
#         i += 1
#         print(i)
#         dicLevel = {}
#         pathBFS = len(bfs(level))
#         pathDFS = len(dfs(level))
#         pathUC = len(uniform_cost(level))
#         pathID = len(iterativeDeepening(level))
#         pathG = len(greedy(level))
#         pathA = len(aStar(level))
#         
#         dicLevel['BFS'] = pathBFS
#         dicLevel['DFS'] = pathDFS
#         dicLevel['Uniform Cost'] = pathUC
#         dicLevel['Iterative Deepening'] = pathID
#         dicLevel['Greedy'] = pathG
#         dicLevel['A*'] = pathA
#          
#         dicPath['Level ' + str(i)] = dicLevel
#         
#     print(dicPath)
#     path_data = pd.DataFrame(dicPath)
#     file_name = '../docs/export_python_path.xlsx'
#     path_data.to_excel(file_name)
# =============================================================================
    
    i = 0
    dicExpanded = {}
    for level in levels:
        i += 1
        print(i)
        dicLevel = {}
        expandedBFS = bfs(level)
        expandedDFS = dfs(level)
        expandedUC = uniform_cost(level)
        expandedID = iterativeDeepening(level)
        expandedG = greedy(level)
        expandedA = aStar(level)
        
        dicLevel['BFS'] = expandedBFS
        dicLevel['DFS'] = expandedDFS
        dicLevel['Uniform Cost'] = expandedUC
        dicLevel['Iterative Deepening'] = expandedID
        dicLevel['Greedy'] = expandedG
        dicLevel['A*'] = expandedA
         
        dicExpanded['Level ' + str(i)] = dicLevel
         
    print(dicExpanded)
    path_data = pd.DataFrame(dicExpanded)
    file_name = '../docs/export_python_expanded.xlsx'
    path_data.to_excel(file_name)
    
    
        
        
    
tests()
        
        
        
        