import pygame
import os

"""
# images
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
LOADING = pygame.image.load('Tiles/loading.png')



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


# rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235)

WIDTH, HEIGHT = 840, 640
SQUARE_WIDTH, SQUARE_HEIGHT = 500, 500
ROWS, COLS = 4, 4
SQUARE_SIZE = SQUARE_WIDTH//COLS

TEXTCOLOR = BLACK