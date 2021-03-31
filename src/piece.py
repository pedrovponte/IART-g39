import pygame
from constants import *

class Piece:
    def __init__(self, row, col, color, square_size):
        self.row = row
        self.col = col
        self.color = color
        self.square_size = square_size
        
        self.x = 0
        self.y = 0
        self.calcultate_pos()
        
        
    def calcultate_pos(self):
        self.x = self.square_size * self.col + 142.85
        self.y = self.square_size * self.row + 62.75
        
        
    def draw_piece(self, window):
        self.color = pygame.transform.scale(self.color, (self.square_size - 5, self.square_size - 5))
        window.blit(self.color, (self.x, self.y))