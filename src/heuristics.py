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
        # print('INIT PIECE:', initPiece)
        # print('INIT FINAL PIECE:', finalPieces)
        for finalPiece in finalPieces:
            if finalPiece[2] == initPiece[2]:
                #aux_points = 0
                if initPiece[0] == finalPiece[0]:
                    points += checkWallBetweenRow(initPiece[0], initPiece[1], finalPiece[1], board)
                if initPiece[1] == finalPiece[1]:
                    points += checkWallBetweenCol(initPiece[0], initPiece[1], finalPiece[0], board)
                if initPiece[0] != finalPiece[0]:
                    points += 1
                if initPiece[1] != finalPiece[1]:
                    points += 1
                #points_piece.append(aux_points)
                #choosed_piece.append(finalPiece)
        '''print('AUX_POINTS: ', aux_points)
        print('CHOOSED_PIECE: ', choosed_piece)
        min_value = min(points_piece)
        min_index = points_piece.index(min_value)
        print('MIN_INDEX: ', min_index)
        choosed = choosed_piece[min_index]
        points += min_value
        finalPieces.remove(choosed)'''
        # print('FINALPIECES: ', finalPieces)
        # time.sleep(2)
        
    #print('POINTS: ', points)
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
# def heuristic4(board):
#     points = 0
#     initialPieces = getPiecePositions(board)
#     finalPieces = getFinalPiecePositions(board)
#     for initPiece in initialPieces:
#         points_piece = []
#         choosed_piece = []
#         for finalPiece in finalPieces:
#             if finalPiece[2] == initPiece[2]:
#                 aux_points = 0
#                 if initPiece[0] != finalPiece[0]:
#                     aux_points += 1
#                 if initPiece[1] != finalPiece[1]:
#                     aux_points += 1
#                 points_piece.append(aux_points)
#                 choosed_piece.append(finalPiece)
#         # print('AUX_POINTS: ', aux_points)
#         # print('CHOOSED_PIECE: ', choosed_piece)
#         min_value = min(points_piece)
#         min_index = points_piece.index(min_value)
#         # print('MIN_INDEX: ', min_index)
#         choosed = choosed_piece[min_index]
#         points += min_value
#         finalPieces.remove(choosed)
#         # print('FINALPIECES: ', finalPieces)
#         
#         
#     print('POINTS: ', points)
#     return points
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

'''print(calculateManhattan([
		['-','X','FG','X'],
		['X','X','FR','-'],
		['X','IR','-','-'],
		['IG','-','X','X']
		]))
'''

print("H1")
print(heuristic([
        ['X', '-', '-', 'IR'],
        ['X', '-', 'IO', 'X'],
        ['X', '-', 'FO', '-'],
        ['X', 'FR', 'X', '-']
        ]))