from states import *
import time
from pythonds.basic.stack import Stack
from levels import *
import math

# 1º heuristic - move to position with more rows/columns of final destinations

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
        
# 2º heuristic - move to position that puts more pieces in the correct place

def heuristic2(board):
    dmatch=0
    for row in board:
        for cel in row:
            if(cel[0] == 'F'):
                dmatch += 1
    return dmatch

# 3º heuristic - move to position that puts pieces closer to goal (< manhattan distance)

def heuristic3(board):
    return calculateManhattan(board)

            
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




# Auxiliar methods :

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

        
    
# List of all pieces positions    
def getPiecePositions(board):
    pieces = []
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if((board[row][col][0] == 'I' and len(board[row][col]) < 3) or (board[row][col][0] == 'I' and len(board[row][col]) > 2 and board[row][col][3] != board[row][col][1])):
               pieces.append([row, col, board[row][col][1]])
    return pieces 
    
# List of final pieces positions [[row, col, cor], [], ... ]
def getFinalPiecePositions(board):
    pieces = []
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if((board[row][col][0] == 'F') and (len(board[row][col]) < 3)):
               pieces.append([row, col, board[row][col][1]])
            elif(len(board[row][col]) > 2 and (len(board[row][col]) > 2 and board[row][col][1] != board[row][col][3])):
                pieces.append([row, col, board[row][col][3]])
    return pieces 
    
                    
# Verifys if there is a wall between piece(pieceX,pieceY) and final(finalX,finalY)                
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

# Verifys if there is a wall between piece(pieceX,pieceY) and final(finalX,finalY) 
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


def calculateManhattan(board):
    initialPieces = getPiecePositions(board)
    finalPieces = getFinalPiecePositions(board)
    manDict = 0
    for i,item in enumerate(initialPieces):
        for j,item2 in enumerate(finalPieces):
            if(item[2]==item2[2]):
                manDict += abs(item[0]-item2[0]) + abs(item[1]- item2[1])
    return manDict

print(calculateManhattan([
		['-','X','FG','X'],
		['X','X','FR','-'],
		['X','IR','-','-'],
		['IG','-','X','X']
		]))


    