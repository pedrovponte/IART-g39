import pygame
from constants import *
from piece import *

class Board:
    def __init__(self, input_board, square_size):
        self.square_size = square_size
        self.board = [] 
        self.input_board = input_board
        self.create_board(input_board)
        

    def draw(self, window):
        bg = pygame.image.load("Tiles/background.jpg")
        window.blit(bg, (0, 0))
        
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
                    
                


 