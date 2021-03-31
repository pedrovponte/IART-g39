import pygame
from utils import *


# images
"""

X_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/wall.png')
W_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/white_tile.png')
IB_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/blue_initial_tile.png')
FB_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/blue_final_tile.png')
IG_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/green_initial_tile.png')
FG_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/green_final_tile.png')
IO_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/orange_initial_tile.png')
FO_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/orange_final_tile.png')
IP_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/purple_initial_tile.png')
FP_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/purple_final_tile.png')
IR_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/red_initial_tile.png') 
FR_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/red_final_tile.png')
IY_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/yellow_initial_tile.png')
FY_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/yellow_final_tile.png')
IBFB_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/blue_tile.png')
IGFG_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/green_tile.png')
IOFO_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/orange_tile.png')
IPFP_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/purple_tile.png')
IRFR_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/red_tile.png')
IYFY_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/yellow_tile.png')
IBFG_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/blue_greenc_tile.png')
IBFO_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/blue_orangec_tile.png')
IBFP_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/blue_purplec_tile.png')
IBFR_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/blue_redc_tile.png')
IBFY_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/blue_yellowc_tile.png')
IGFB_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/green_bluec_tile.png')
IGFO_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/green_orangec_tile.png')
IGFP_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/green_purplec_tile.png')
IGFR_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/green_redc_tile.png')
IGFY_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/green_yellowc_tile.png')
IOFB_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/orange_bluec_tile.png')
IOFG_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/orange_greenc_tile.png')
IOFP_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/orange_purplec_tile.png')
IOFR_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/orange_redc_tile.png')
IOFY_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/orange_yellowc_tile.png')
IPFB_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/purple_bluec_tile.png')
IPFG_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/purple_greenc_tile.png')
IPFO_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/purple_orangec_tile.png')
IPFR_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/purple_redc_tile.png')
IPFY_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/purple_yellowc_tile.png')
IRFB_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/red_bluec_tile.png')
IRFG_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/red_greenc_tile.png')
IRFO_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/red_orangec_tile.png')
IRFP_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/red_purplec_tile.png')
IRFY_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/red_yellowc_tile.png')
IYFB_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/yellow_bluec_tile.png')
IYFG_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/yellow_greenc_tile.png')
IYFO_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/yellow_orangec_tile.png')
IYFP_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/yellow_purplec_tile.png')
IYFR_TILE = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/yellow_redc_tile.png')
LOADING = pygame.image.load('C:/Users/Mariana Ramos/Desktop/3ano/iart/IART-g39/src/Tiles/yellow_redc_tile.png')

"""
X_TILE = pygame.image.load('Tiles/wall.png')
W_TILE = pygame.image.load('Tiles/white_tile.png')
IB_TILE = pygame.image.load('Tiles/blue_initial_tile.png')
FB_TILE = pygame.image.load('Tiles/blue_final_tile.png')
IG_TILE = pygame.image.load('Tiles/green_initial_tile.png')
FG_TILE = pygame.image.load('Tiles/green_final_tile.png')
IO_TILE = pygame.image.load('Tiles/orange_initial_tile.png')
FO_TILE = pygame.image.load('Tiles/orange_final_tile.png')
IP_TILE = pygame.image.load('Tiles/purple_initial_tile.png')
FP_TILE = pygame.image.load('Tiles/purple_final_tile.png')
IR_TILE = pygame.image.load('Tiles/red_initial_tile.png') 
FR_TILE = pygame.image.load('Tiles/red_final_tile.png')
IY_TILE = pygame.image.load('Tiles/yellow_initial_tile.png')
FY_TILE = pygame.image.load('Tiles/yellow_final_tile.png')
IBFB_TILE = pygame.image.load('Tiles/blue_tile.png')
IGFG_TILE = pygame.image.load('Tiles/green_tile.png')
IOFO_TILE = pygame.image.load('Tiles/orange_tile.png')
IPFP_TILE = pygame.image.load('Tiles/purple_tile.png')
IRFR_TILE = pygame.image.load('Tiles/red_tile.png')
IYFY_TILE = pygame.image.load('Tiles/yellow_tile.png')
IBFG_TILE = pygame.image.load('Tiles/blue_greenc_tile.png')
IBFO_TILE = pygame.image.load('Tiles/blue_orangec_tile.png')
IBFP_TILE = pygame.image.load('Tiles/blue_purplec_tile.png')
IBFR_TILE = pygame.image.load('Tiles/blue_redc_tile.png')
IBFY_TILE = pygame.image.load('Tiles/blue_yellowc_tile.png')
IGFB_TILE = pygame.image.load('Tiles/green_bluec_tile.png')
IGFO_TILE = pygame.image.load('Tiles/green_orangec_tile.png')
IGFP_TILE = pygame.image.load('Tiles/green_purplec_tile.png')
IGFR_TILE = pygame.image.load('Tiles/green_redc_tile.png')
IGFY_TILE = pygame.image.load('Tiles/green_yellowc_tile.png')
IOFB_TILE = pygame.image.load('Tiles/orange_bluec_tile.png')
IOFG_TILE = pygame.image.load('Tiles/orange_greenc_tile.png')
IOFP_TILE = pygame.image.load('Tiles/orange_purplec_tile.png')
IOFR_TILE = pygame.image.load('Tiles/orange_redc_tile.png')
IOFY_TILE = pygame.image.load('Tiles/orange_yellowc_tile.png')
IPFB_TILE = pygame.image.load('Tiles/purple_bluec_tile.png')
IPFG_TILE = pygame.image.load('Tiles/purple_greenc_tile.png')
IPFO_TILE = pygame.image.load('Tiles/purple_orangec_tile.png')
IPFR_TILE = pygame.image.load('Tiles/purple_redc_tile.png')
IPFY_TILE = pygame.image.load('Tiles/purple_yellowc_tile.png')
IRFB_TILE = pygame.image.load('Tiles/red_bluec_tile.png')
IRFG_TILE = pygame.image.load('Tiles/red_greenc_tile.png')
IRFO_TILE = pygame.image.load('Tiles/red_orangec_tile.png')
IRFP_TILE = pygame.image.load('Tiles/red_purplec_tile.png')
IRFY_TILE = pygame.image.load('Tiles/red_yellowc_tile.png')
IYFB_TILE = pygame.image.load('Tiles/yellow_bluec_tile.png')
IYFG_TILE = pygame.image.load('Tiles/yellow_greenc_tile.png')
IYFO_TILE = pygame.image.load('Tiles/yellow_orangec_tile.png')
IYFP_TILE = pygame.image.load('Tiles/yellow_purplec_tile.png')
IYFR_TILE = pygame.image.load('Tiles/yellow_redc_tile.png')



# colors dictionary

colors = {
    'X' : X_TILE,
    'W' : W_TILE,
    'IB' : IB_TILE,
    'FB' : FB_TILE,
    'IG' : IG_TILE,
    'FG' : FG_TILE,
    'IO' : IO_TILE,
    'FO' : FO_TILE,
    'IP' : IP_TILE,
    'FP' : FP_TILE,
    'IR' : IR_TILE,
    'FR' : FR_TILE,
    'IY' : IY_TILE,
    'FY' : FY_TILE,
    'IBFB' : IBFB_TILE,
    'IGFG' : IGFG_TILE,
    'IOFO' : IOFO_TILE,
    'IPFP' : IPFP_TILE,
    'IRFR' : IRFR_TILE,
    'IYFY' : IYFY_TILE,
    'IBFG' : IBFG_TILE,
    'IBFO' : IBFO_TILE,
    'IBFP' : IBFP_TILE,
    'IBFR' : IBFR_TILE,
    'IBFY' : IBFY_TILE,
    'IGFB' : IGFB_TILE,
    'IGFO' : IGFO_TILE,
    'IGFP' : IGFP_TILE,
    'IGFR' : IGFR_TILE,
    'IGFY' : IGFY_TILE,
    'IOFB' : IOFB_TILE,
    'IOFG' : IOFG_TILE,
    'IOFP' : IOFP_TILE,
    'IOFR' : IOFR_TILE,
    'IOFY' : IOFY_TILE,
    'IPFB' : IPFB_TILE,
    'IPFG' : IPFG_TILE,
    'IPFO' : IPFO_TILE,
    'IPFR' : IPFR_TILE,
    'IPFY' : IPFY_TILE,
    'IRFB' : IRFB_TILE,
    'IRFG' : IRFG_TILE,
    'IRFO' : IRFO_TILE,
    'IRFP' : IRFP_TILE,
    'IRFY' : IRFY_TILE,
    'IYFB' : IYFB_TILE,
    'IYFG' : IYFG_TILE,
    'IYFO' : IYFO_TILE,
    'IYFP' : IYFP_TILE,
    'IYFR' : IYFR_TILE
}



PERFECT1 = '2'
PERFECT2 = '3'
PERFECT3 = '3'
PERFECT4 = '4'
PERFECT5 = '10'
PERFECT6 = '7'
PERFECT7 = '11'
PERFECT8 = '11'
PERFECT9 = '8'
PERFECT10 = '7'
PERFECT11 = '10'
PERFECT12 = '8'
PERFECT13 = '6'
PERFECT14 = '13'
PERFECT15 = '13'
PERFECT16 = '12'
PERFECT17 = '14'
PERFECT18 = '14'
PERFECT19 = '8'
PERFECT20 = '9'


# rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235)

WIDTH, HEIGHT = 840, 640
SQUARE_WIDTH, SQUARE_HEIGHT = 500, 500
ROWS, COLS = 4, 4
SQUARE_SIZE = SQUARE_WIDTH//COLS

# Text
TEXTCOLOR = BLACK
TEXTCOLORWHITE = WHITE

GAMENAME_SURF, GAMENAME_RECT = makeText('Match the Tiles', TEXTCOLOR, 215, 100, 55)
PLAYER_SURF, PLAYER_RECT = makeText('Player Mode', TEXTCOLOR, 350, 270, 25)
COMPUTER_SURF, COMPUTER_RECT = makeText('Computer Mode', TEXTCOLOR, 328, 320, 25)

RESET_SURF, RESET_RECT = makeText('Reset', TEXTCOLOR, 720, 300, 20)
QUIT_SURF, QUIT_RECT = makeText('Quit', TEXTCOLOR, 720, 325, 20)
HINT_SURF, HINT_RECT = makeText('Hint', TEXTCOLOR, 720, 275, 20)

CHOOSELEVEL_SURF, CHOOSELEVEL_RECT = makeText('Choose Level', TEXTCOLOR, 325, 50, 30)
LEVEL1_SURF, LEVEL1_RECT = makeText('Level 1', TEXTCOLOR, 225, 125, 25)
LEVEL2_SURF, LEVEL2_RECT = makeText('Level 2', TEXTCOLOR, 225, 155, 25)
LEVEL3_SURF, LEVEL3_RECT = makeText('Level 3', TEXTCOLOR, 225, 185, 25)
LEVEL4_SURF, LEVEL4_RECT = makeText('Level 4', TEXTCOLOR, 225, 215, 25)
LEVEL5_SURF, LEVEL5_RECT = makeText('Level 5', TEXTCOLOR, 225, 245, 25)
LEVEL6_SURF, LEVEL6_RECT = makeText('Level 6', TEXTCOLOR, 225, 275, 25)
LEVEL7_SURF, LEVEL7_RECT = makeText('Level 7', TEXTCOLOR, 225, 305, 25)
LEVEL8_SURF, LEVEL8_RECT = makeText('Level 8', TEXTCOLOR, 225, 335, 25)
LEVEL9_SURF, LEVEL9_RECT = makeText('Level 9', TEXTCOLOR, 225, 365, 25)
LEVEL10_SURF, LEVEL10_RECT = makeText('Level 10', TEXTCOLOR, 225, 395, 25)
LEVEL11_SURF, LEVEL11_RECT = makeText('Level 11', TEXTCOLOR, 500, 125, 25)
LEVEL12_SURF, LEVEL12_RECT = makeText('Level 12', TEXTCOLOR, 500, 155, 25)
LEVEL13_SURF, LEVEL13_RECT = makeText('Level 13', TEXTCOLOR, 500, 185, 25)
LEVEL14_SURF, LEVEL14_RECT = makeText('Level 14', TEXTCOLOR, 500, 215, 25)
LEVEL15_SURF, LEVEL15_RECT = makeText('Level 15', TEXTCOLOR, 500, 245, 25)
LEVEL16_SURF, LEVEL16_RECT = makeText('Level 16', TEXTCOLOR, 500, 275, 25)
LEVEL17_SURF, LEVEL17_RECT = makeText('Level 17', TEXTCOLOR, 500, 305, 25)
LEVEL18_SURF, LEVEL18_RECT = makeText('Level 18', TEXTCOLOR, 500, 335, 25)
LEVEL19_SURF, LEVEL19_RECT = makeText('Level 19', TEXTCOLOR, 500, 365, 25)
LEVEL20_SURF, LEVEL20_RECT = makeText('Level 20', TEXTCOLOR, 500, 395, 25)

CHOOSEMODE_SURF, CHOOSEMODE_RECT = makeText('Choose Computer Mode', TEXTCOLOR, 225, 75, 30)
BFS_SURF, BFS_RECT = makeText('Breadth-First Search', TEXTCOLOR, 200, 150, 25)
DFS_SURF, DFS_RECT = makeText('Depth-First Search', TEXTCOLOR, 200, 200, 25)
UNIFORM_SURF, UNIFORM_RECT = makeText('Uniform Cost Search', TEXTCOLOR, 200, 250, 25)
GREEDY_SURF, GREEDY_RECT = makeText('Greedy Search', TEXTCOLOR, 200, 300, 25)
ASTAR_SURF, ASTAR_RECT = makeText('A Star Search', TEXTCOLOR, 200, 350, 25)
ITERATIVE_SURF, ITERATIVE_RECT = makeText('Iterative Deepening Search', TEXTCOLOR, 200, 400, 25)