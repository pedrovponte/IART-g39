import pygame
from constants import *

class Board:
    def __init__(self, board):
        # self.algorithm = utils.chooseAlg()
        self.board = board

    def draw(self, window):
        window.fill(BLUE)
        
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(window, WHITE, (row*SQUARE_SIZE + 140,col*SQUARE_SIZE + 60,SQUARE_SIZE,SQUARE_SIZE), 0)
                pygame.draw.rect(window, BLACK, (row*SQUARE_SIZE + 140,col*SQUARE_SIZE + 60,SQUARE_SIZE,SQUARE_SIZE), 1)

    


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

 