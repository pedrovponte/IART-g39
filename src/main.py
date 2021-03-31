import pygame, sys, time
from constants import WIDTH, HEIGHT
from board import *
from levels import *
from utils import *
from states import *
from bfs import *
from dfs import *
from uniform_cost import *
from greedy import *
from aStar import *
from iterativeDeepening import *
import msvcrt as m

FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Match the Tiles - Sliding Puzzle Game')


def main():
    run = True
    display_menu = True
    display_level = True
    display_alg = True
    display_mode = True
    clock = pygame.time.Clock()
    moves = 0
    
    width, height = 840, 640
    square_width, square_height = 500, 500
    
    
    while display_menu:
        WINDOW.fill(BLUE)
        WINDOW.blit(GAMENAME_SURF, GAMENAME_RECT)
        WINDOW.blit(PLAYER_SURF, PLAYER_RECT)
        WINDOW.blit(COMPUTER_SURF, COMPUTER_RECT)
    
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if PLAYER_RECT.collidepoint(event.pos):
                    mode = 'player'
                    display_menu = False
                    display_mode = False
                    break
                elif COMPUTER_RECT.collidepoint(event.pos):
                    display_menu = False
                    break
                
        if(display_menu != False):
            pygame.display.update()
            
    
    while display_mode:
        WINDOW.fill(BLUE)
        WINDOW.blit(CHOOSEMODE_SURF, CHOOSEMODE_RECT)
        WINDOW.blit(BFS_SURF, BFS_RECT)
        WINDOW.blit(DFS_SURF, DFS_RECT)
        WINDOW.blit(UNIFORM_SURF, UNIFORM_RECT)
        WINDOW.blit(GREEDY_SURF, GREEDY_RECT)
        WINDOW.blit(ASTAR_SURF, ASTAR_RECT)
        WINDOW.blit(ITERATIVE_SURF, ITERATIVE_RECT)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if BFS_RECT.collidepoint(event.pos):
                    mode = 'bfs'
                    display_mode = False
                    break
                elif DFS_RECT.collidepoint(event.pos):
                    mode = 'dfs'
                    display_mode = False
                    break
                elif UNIFORM_RECT.collidepoint(event.pos):
                    mode = 'uniform'
                    display_mode = False
                    break
                elif GREEDY_RECT.collidepoint(event.pos):
                    mode = 'greedy'
                    display_mode = False
                    break
                elif ASTAR_RECT.collidepoint(event.pos):
                    mode = 'astar'
                    display_mode = False
                    break
                elif ITERATIVE_RECT.collidepoint(event.pos):
                    mode = 'iterative'
                    display_mode = False
                    break
                
        if(display_mode != False):
            pygame.display.update()
    
            
    while display_level:
        WINDOW.fill(BLUE)
        WINDOW.blit(CHOOSELEVEL_SURF, CHOOSELEVEL_RECT)
        WINDOW.blit(LEVEL1_SURF, LEVEL1_RECT)
        WINDOW.blit(LEVEL2_SURF, LEVEL2_RECT)
        WINDOW.blit(LEVEL3_SURF, LEVEL3_RECT)
        WINDOW.blit(LEVEL4_SURF, LEVEL4_RECT)
        WINDOW.blit(LEVEL5_SURF, LEVEL5_RECT)
        WINDOW.blit(LEVEL6_SURF, LEVEL6_RECT)
        WINDOW.blit(LEVEL7_SURF, LEVEL7_RECT)
        WINDOW.blit(LEVEL8_SURF, LEVEL8_RECT)
        WINDOW.blit(LEVEL9_SURF, LEVEL9_RECT)
        WINDOW.blit(LEVEL10_SURF, LEVEL10_RECT)
        WINDOW.blit(LEVEL11_SURF, LEVEL11_RECT)
        WINDOW.blit(LEVEL12_SURF, LEVEL12_RECT)
        WINDOW.blit(LEVEL13_SURF, LEVEL13_RECT)
        WINDOW.blit(LEVEL14_SURF, LEVEL14_RECT)
        WINDOW.blit(LEVEL15_SURF, LEVEL15_RECT)
        WINDOW.blit(LEVEL16_SURF, LEVEL16_RECT)
        WINDOW.blit(LEVEL17_SURF, LEVEL17_RECT)
        WINDOW.blit(LEVEL18_SURF, LEVEL18_RECT)
        WINDOW.blit(LEVEL19_SURF, LEVEL19_RECT)
        WINDOW.blit(LEVEL20_SURF, LEVEL20_RECT)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if LEVEL1_RECT.collidepoint(event.pos):
                    level = level1
                    perfect = PERFECT1
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL2_RECT.collidepoint(event.pos):
                    level = level2
                    perfect = PERFECT2
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL3_RECT.collidepoint(event.pos):
                    level = level3
                    perfect = PERFECT3
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL4_RECT.collidepoint(event.pos):
                    level = level4
                    perfect = PERFECT4
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL5_RECT.collidepoint(event.pos):
                    level = level5
                    perfect = PERFECT5
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL6_RECT.collidepoint(event.pos):
                    level = level6
                    perfect = PERFECT6
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL7_RECT.collidepoint(event.pos):
                    level = level7
                    perfect = PERFECT7
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL8_RECT.collidepoint(event.pos):
                    level = level8
                    perfect = PERFECT8
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL9_RECT.collidepoint(event.pos):
                    level = level9
                    perfect = PERFECT9
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL10_RECT.collidepoint(event.pos):
                    level = level10
                    perfect = PERFECT10
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL11_RECT.collidepoint(event.pos):
                    level = level11
                    perfect = PERFECT11
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL12_RECT.collidepoint(event.pos):
                    level = level12
                    perfect = PERFECT12
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL13_RECT.collidepoint(event.pos):
                    level = level13
                    perfect = PERFECT13
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL14_RECT.collidepoint(event.pos):
                    level = level14
                    perfect = PERFECT14
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL15_RECT.collidepoint(event.pos):
                    level = level15
                    perfect = PERFECT15
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL16_RECT.collidepoint(event.pos):
                    level = level16
                    perfect = PERFECT16
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL17_RECT.collidepoint(event.pos):
                    level = level17
                    perfect = PERFECT17
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL18_RECT.collidepoint(event.pos):
                    level = level18
                    perfect = PERFECT18
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL19_RECT.collidepoint(event.pos):
                    level = level19
                    perfect = PERFECT19
                    initial_level = level
                    display_level = False
                    break
                elif LEVEL20_RECT.collidepoint(event.pos):
                    level = level20
                    perfect = PERFECT20
                    initial_level = level
                    display_level = False
                    break
                
        if(display_level != False):
            pygame.display.update()
            
    
    rows, cols = len(level), len(level)
    square_size = square_width // cols    
    
    board = Board(level, square_size)
    allMoves = []
    path = None
            
    
    if(mode == 'bfs'):
        path = bfs(level)
        print("ALL MOVES: ", path)
    elif(mode == 'dfs'):
        path = dfs(level)
        print("ALL MOVES: ", path)
    elif(mode == 'uniform'):
        path = uniform_cost(level)
        print("ALL MOVES: ", path)
    elif(mode == 'greedy'):
        path = greedy(level)
        print("ALL MOVES: ", path)
    elif(mode == 'astar'):
        path = aStar(level)
        print("ALL MOVES: ", path)
    elif(mode == 'iterative'):
        path = iterativeDeepening(level)
        print("ALL MOVES: ", path)
    
    
    while run:
        clock.tick(FPS)
        move = None
        
        board.draw(WINDOW)
        WINDOW.blit(RESET_SURF, RESET_RECT)
        WINDOW.blit(QUIT_SURF, QUIT_RECT)
        WINDOW.blit(HINT_SURF, HINT_RECT)
        PERFECT_SURF, PERFECT_RECT = makeText('Perfect Moves: ' + perfect, TEXTCOLORWHITE, 660, 150, 20)
        
        
        if objectiveTest(level):
            pygame.display.update()
            time.sleep(2)
            terminate()
            run = False
            break
        
        if(mode == 'player'):
            WINDOW.blit(PERFECT_SURF, PERFECT_RECT)
            MOVES_SURF, MOVES_RECT = makeText('Moves: ' + str(moves), TEXTCOLORWHITE, 700, 175, 20)
            WINDOW.blit(MOVES_SURF, MOVES_RECT)
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
                if event.type == pygame.MOUSEBUTTONUP:
                    if RESET_RECT.collidepoint(event.pos):
                        level = initial_level
                        board = Board(level, square_size)
                        allMoves = []
                        path = None
                    elif QUIT_RECT.collidepoint(event.pos):
                        terminate()
                        run = False
                        continue
                    elif HINT_RECT.collidepoint(event.pos):
                        path = []
                        path = aStar(level)
                        move = path[0]
            
            
            if move:
                level = effects(level, move)
                allMoves.append(move)
                print("ALL MOVES: ", allMoves)
                moves = len(allMoves)
                board = Board(level, square_size)
                
        
        else:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        move = path.pop(0)
                        level = effects(level, move)
                        allMoves.append(move)
                        board = Board(level, square_size)
                if event.type == pygame.MOUSEBUTTONUP:
                    if RESET_RECT.collidepoint(event.pos):
                        level = initial_level
                        board = Board(level, square_size)
                        allMoves = []
                        path = None
                    elif QUIT_RECT.collidepoint(event.pos):
                        terminate()
                        run = False
                        break
                    
        if(run != False):
            pygame.display.update()
        
    
def terminate():    
    pygame.quit()
    

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    main()
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
    #main(level10, 'bfs')
    #main(level1, 'dfs')
    #main(level2, 'dfs')
    #main(level3, 'dfs')
    #main(level4, 'dfs')
    #main(level5, 'dfs')
    #main(level6, 'dfs')
    #main(level7, 'dfs')
    #main(level8, 'dfs')
    #main(level9, 'dfs')
    #main(level10, 'dfs')
    #main(level1, 'uniform_cost')
    #main(level2, 'uniform_cost')
    #main(level3, 'uniform_cost')
    #main(level4, 'uniform_cost')
    #main(level5, 'uniform_cost')
    #main(level6, 'uniform_cost')
    #main(level7, 'uniform_cost')
    #main(level8, 'uniform_cost')
    #main(level9, 'uniform_cost')
    #main(level10, 'uniform_cost')
    #main(level1, 'greedy')
    #main(level2, 'greedy')
    #main(level3, 'greedy')
    #main(level4, 'greedy')
    #main(level5, 'greedy')
    #main(level6, 'greedy')
    #main(level7, 'greedy')
    #main(level8, 'greedy')
    #main(level9, 'greedy')
    #main(level10, 'greedy')
    