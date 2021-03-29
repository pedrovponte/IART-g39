from states import *
import time
from pythonds.basic.stack import Stack
from levels import *
import math

def aStar(start, depth = 100):
    startTime = time.time()
    print("A* start")

    root = Node(start, None, None, 0, 0)
    stack = [root]

    root.heuristic = heuristic(root.state) + h(root.state)
    visited = []
    depth = 1

    while stack:
        stack.sort(key = lambda x: x.heuristic)

        s = stack.pop(0)
        depth = s.depth

        if objectiveTest(s.state):
            path = []
            current = s
            while current is not None:
                path.append(current.operator)
                current = current.parent
                
            path.pop(len(path)-1) # delete None from array

            endTime = time.time()

            timeElapsed = endTime - startTime

            if timeElapsed>1:
                print("Time: " + str(round(timeElapsed,3)) + "s")
            else:
                print("Time: " + str(round(timeElapsed*1000,3)) + "ms")

            return path[::-1]

        if s not in visited:
            expanded = expand_node(s)

            for x in expanded:
                x.heuristic = s.heuristic + heuristic(x.state) + heuristic2(x.state)
                stack.append(x)

            visited.append(s)    
    
            
def getGoalBoard(board):
    goal = []
    for row in board:
        goal_col = []
        for col in row:
            if col[0] == 'I':
                goal_col.append('-')
            elif col[0] == 'F':
                goal_col.append('I' + col[1] + col)
            else:
                goal_col.append(col)
        goal.append(goal_col)
    
    #print('GOAL: ', goal)
    return goal

            
# =============================================================================
# def heuristic(board, goal):
#     h = 0
#     
#     for i, row in enumerate(board):
#         for j, col in enumerate(row):
#             bij = board[i][j]
#             i_b = i
#             j_b = j
# 
#             for i_g, r in enumerate(goal):
#                 for j_g, c in enumerate(r):
#                     if c == bij:
#                         h += (abs(i_g - i_b) + abs(j_g - j_b))
# 
#     return h
# 
# def heuristic1(board, goal):
#     h = 0
#     
#     for i, row in enumerate(board):
#         for j, col in enumerate(row):
#             bij = board[i][j]
#             i_b = i
#             j_b = j
# 
#             for i_g, r in enumerate(goal):
#                 for j_g, c in enumerate(r):
#                     if c == bij:
#                         h += math.ceil(math.sqrt((abs(i_g - i_b))**2 + (abs(j_g - j_b))**2))
# 
#     return h
# =============================================================================

def heuristic(board):
    points = 0
    initialPieces = getPiecePositions(board)
    finalPieces = getFinalPiecePositions(board)
    for initPiece in initialPieces:
        points_piece = []
        for finalPiece in finalPieces:
            if finalPiece[2] == initPiece[2]:
                aux_points = 0
                if initPiece[0] == finalPiece[0]:
                    aux_points += checkWallBetweenRow(initPiece[0], initPiece[1], finalPiece[1], board)
                if initPiece[1] == finalPiece[1]:
                    aux_points += checkWallBetweenCol(initPiece[0], initPiece[1], finalPiece[0], board)
                if initPiece[0] != finalPiece[0]:
                    aux_points += 1
                if initPiece[1] != finalPiece[1]:
                    aux_points += 1
                points_piece.append(aux_points)
        points += min(points_piece)
    print('POINTS: ', points)
    return points
        
    
def heuristic2(board): #uma no sitio certo
    # print(state.state)
    dmatch=0
    for row in board:
        for cel in row:
            if(cel[0] == 'F'):
                dmatch += 1
    return dmatch


        
    
    
def getPiecePositions(board):
    pieces = []
    
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if((board[row][col][0] == 'I' and len(board[row][col]) < 3) or (board[row][col][0] == 'I' and len(board[row][col]) > 2 and board[row][col][3] != board[row][col][1])):
               pieces.append([row, col, board[row][col][1]])
    return pieces 
    


def getFinalPiecePositions(board):
    pieces = []
    
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if((board[row][col][0] == 'F') and (len(board[row][col]) < 3)):
               pieces.append([row, col, board[row][col][1]])
            elif(len(board[row][col]) > 2 and (len(board[row][col]) > 2 and board[row][col][1] != board[row][col][3])):
                pieces.append([row, col, board[row][col][3]])
    return pieces 
    
                    
                
def checkWallBetweenRow(pieceX, pieceY, finalY, board):
    if(pieceY < finalY):
        init = pieceY
        final = finalY
    else:
        init = finalY
        final = pieceY
        
    for i in range(init, final):
        if(board[pieceX][i] == 'X'): # caso tenha uma parede, vai ter de fazer pelo menos 2 movimentos
            return 2
        else:
            return 0
        
def checkWallBetweenCol(pieceX, pieceY, finalX, board):
    if(pieceX < finalX):
        init = pieceX
        final = finalX
    else:
        init = finalX
        final = pieceX
    
    for i in range(init, final):
        if(board[i][pieceY] == 'X'):
            return 2
        else:
            return 0


print(aStar(level10))
    
    