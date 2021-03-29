import pygame
from constants import *
from piece import *

class Board:
    def __init__(self, input_board, square_size):
        # self.algorithm = utils.chooseAlg()
        self.square_size = square_size
        self.board = [] 
        self.input_board = input_board
        self.create_board(input_board)

    def draw(self, window):
        window.fill(BLUE)
        
        for row in range(len(self.input_board)):
            for col in range(len(self.input_board)):
                pygame.draw.rect(window, WHITE, (row*self.square_size + 140, col*self.square_size + 60, self.square_size, self.square_size), 0)
                pygame.draw.rect(window, BLACK, (row*self.square_size + 140, col*self.square_size + 60, self.square_size, self.square_size), 1)
        
        for row in range(len(self.input_board)):
            for col in range(len(self.input_board)):
                piece = self.board[row][col]
                if(piece != 0):
                    piece.draw_piece(window)
    
    def create_board(self, input_board):
        for row in range(len(input_board)):
            self.board.append([])
            for col in range(len(input_board)):
                if(input_board[row][col] == '-'):
                	self.board[row].append(0)
                else:
                    self.board[row].append(Piece(row, col, colors[input_board[row][col]], self.square_size))
                    
                
# =============================================================================
#                 elif(input_board[row][col] == 'IB'):
#                     self.board[row].append(Piece(row, col, colors[input_board[row][col]], self.square_size))
#                 elif(input_board[row][col] == 'IG'):
#                     self.board[row].append(Piece(row, col, colors[input_board[row][col]], self.square_size))
#                 elif(input_board[row][col] == 'IO'):
#                     self.board[row].append(Piece(row, col, colors[input_board[row][col]], self.square_size))
#                 elif(input_board[row][col] == 'IP'):
#                     self.board[row].append(Piece(row, col, colors[input_board[row][col]], self.square_size))
#                 elif(input_board[row][col] == 'IR'):
#                     self.board[row].append(Piece(row, col, colors[input_board[row][col]], self.square_size))
#                 elif(input_board[row][col] == 'IY'):
#                     self.board[row].append(Piece(row, col, colors[input_board[row][col]], self.square_size))
#                 elif(input_board[row][col] == 'FB'):
#                 	self.board[row].append(Piece(row, col, colors[input_board[row][col]], self.square_size))
#                 elif(input_board[row][col] == 'FG'):
#                 	self.board[row].append(Piece(row, col, colors[input_board[row][col]], self.square_size))
#                 elif(input_board[row][col] == 'FO'):
#                 	self.board[row].append(Piece(row, col, colors[input_board[row][col]], self.square_size))
#                 elif(input_board[row][col] == 'FP'):
#                 	self.board[row].append(Piece(row, col, colors[input_board[row][col]], self.square_size))
#                 elif(input_board[row][col] == 'FR'):
#                 	self.board[row].append(Piece(row, col, colors[input_board[row][col]], self.square_size))
#                 elif(input_board[row][col] == 'FY'):
#                 	self.board[row].append(Piece(row, col, colors[input_board[row][col]], self.square_size))
# =============================================================================
                
                

                     

    


"""


    def move(self, piece, movements):
        r = 0
        for row in self.board:
            c = 0
            for col in self.board[r]:
                if [r,c] in movements:
                    self.board[r][c] = piece
                elif self.board[r][c] == piece:
                    self.board[r][c] = '0'
                c += 1
            r += 1
    def can_move(self, piece, x, y):
        positions_to_move = self.select_piece(piece)
        positions_after_move = []
        for pos in positions_to_move:
            positions_after_move.append([pos[0]+y,pos[1]+x])
        for pos in positions_after_move:
            if pos[0] not in [0, 1, 2, 3] or pos[1] not in [0, 1, 2, 3]:
                print("Out of bounds move")
                return False
            if self.board[pos[0]][pos[1]] not in ['0', piece]:
                print("Piece blocking the movement: " + self.board[pos[0]][pos[1]])
                return False
        self.move(piece, positions_after_move)
        self.join_color(piece, positions_after_move)
        self.moves += 1
        return True
    def move_left(self, piece):
        self.can_move(piece, -1, 0)
        self.printBoard()
        self.win()
    def move_right(self, piece):
        self.can_move(piece, 1, 0)
        self.printBoard()
        self.win()
    def move_up(self, piece):
        self.can_move(piece, 0, -1)
        self.printBoard()
        self.win()
    def move_down(self, piece):
        self.can_move(piece, 0, 1)
        self.printBoard()
        self.win()

"""

 