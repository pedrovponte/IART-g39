import pygame, sys, time
from constants import WIDTH, HEIGHT
from board import *
from levels import *
from utils import *
from states import *

FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Match the Tiles - Sliding Puzzle Game')


def main(level, mode):
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
    
    if(mode == 'bfs'):
        path = bfs(level)
    
    
    while run:
        clock.tick(FPS)
        move = None
        
        board.draw(WINDOW)
        WINDOW.blit(RESET_SURF, RESET_RECT)
        WINDOW.blit(NEW_SURF, NEW_RECT)
        WINDOW.blit(SOLVE_SURF, SOLVE_RECT)
        
        if(mode == 'player'):
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
                print("MOVE: ", move)
                level = effects(level, move)
                allMoves.append(move)
                print("ALL MOVES: ", allMoves)
                board = Board(level, square_size)
                
            
        
        elif(mode == 'bfs'):
            print("PATH: ", path)
            move = path.pop(0)
            print("MOVE: ", move)
            level = effects(level, move)
            allMoves.append(move)
            print("ALL MOVES: ", allMoves)
            print("LEVEL: ", level)
            board = Board(level, square_size)
                
        pygame.display.update()
        
        if(mode == 'bfs'):
            time.sleep(2)
        
        if objectiveTest(level):
            terminate()
            break
            
            
    
def terminate():    
    pygame.quit()


#main(level1, 'player')
#main(level2, 'player')
#main(level3, 'player')
#main(level4, 'player')
#main(level5, 'player')
#main(level6, 'player')
#main(level7, 'player')
#main(level8, 'player')
#main(level9, 'player')
#main(level10, 'player')
#main(level1, 'bfs')
#main(level2, 'bfs')
#main(level3, 'bfs')
#main(level4, 'bfs')
#main(level5, 'bfs')
#main(level6, 'bfs')
#main(level7, 'bfs')
#main(level8, 'bfs')
#main(level9, 'bfs')
main(level10, 'bfs')