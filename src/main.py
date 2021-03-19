import pygame
from constants import WIDTH, HEIGHT
from board import *
from levels import *
from utils import *
from states import *

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
    allMoves = []
    
    while run:
        clock.tick(FPS)
        move = None
        
        board.draw(WINDOW)
        WINDOW.blit(RESET_SURF, RESET_RECT)
        WINDOW.blit(NEW_SURF, NEW_RECT)
        WINDOW.blit(SOLVE_SURF, SOLVE_RECT)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_a) and precond(level, "left"):
                    move = "left"
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and precond(level, "right"):
                    move = "right"
                elif event.key in (pygame.K_UP, pygame.K_w) and precond(level, "up"):
                    move = "up"
                elif event.key in (pygame.K_DOWN, pygame.K_s) and precond(level, "down"):
                    move = "down"
        
        if move:
            board.board = effects(level, move)
            allMoves.append(move)
        
        board = Board(level, square_size)
            
        pygame.display.update()
    
    pygame.quit()


p1 = main(test3)