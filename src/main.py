import pygame
from constants import WIDTH, HEIGHT
from board import *
from levels import test2
from utils import *

FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Match the Tiles - Sliding Puzzle Game')


def main(level):
    run = True
    clock = pygame.time.Clock()

    RESET_SURF, RESET_RECT = makeText('Reset', TEXTCOLOR, WIDTH - 120, HEIGHT - 300)
    NEW_SURF, NEW_RECT = makeText('New Game', TEXTCOLOR, WIDTH - 120, HEIGHT - 260)
    SOLVE_SURF, SOLVE_RECT = makeText('Solve', TEXTCOLOR, WIDTH - 120, HEIGHT - 220)

    board = Board(level)
    
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


p1 = main(test2)