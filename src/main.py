import pygame
from constants import WIDTH, HEIGHT
from board import *
from levels import *
from utils import *

FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Match the Tiles - Sliding Puzzle Game')


def main(level):
    run = True
    clock = pygame.time.Clock()
    
    width, height = 840, 640
    square_width, square_height = 500, 500
    rows, cols = len(level), len(level)
    square_size = square_width // cols

    RESET_SURF, RESET_RECT = makeText('Reset', TEXTCOLOR, width - 120, height - 300)
    NEW_SURF, NEW_RECT = makeText('New Game', TEXTCOLOR, width - 120, height - 260)
    SOLVE_SURF, SOLVE_RECT = makeText('Solve', TEXTCOLOR, width - 120, height - 220)

    board = Board(level, square_size)
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
        board.draw(WINDOW)
        WINDOW.blit(RESET_SURF, RESET_RECT)
        WINDOW.blit(NEW_SURF, NEW_RECT)
        WINDOW.blit(SOLVE_SURF, SOLVE_RECT)
        pygame.display.update()
        
    
    pygame.quit()


p1 = main(test3)