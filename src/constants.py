import pygame

# images
WALL_TILE = pygame.image.load('Tiles/wall.png')
WHITE_TILE = pygame.image.load('Tiles/white_tile.png')
BLUE_TILE = pygame.image.load('Tiles/blue_tile.png')
BLUE_FINAL_TILE = pygame.image.load('Tiles/blue_final_tile.png')
GREEN_TILE = pygame.image.load('Tiles/green_tile.png')
GREEN_FINAL_TILE = pygame.image.load('Tiles/green_final_tile.png')
ORANGE_TILE = pygame.image.load('Tiles/orange_tile.png')
ORANGE_FINAL_TILE = pygame.image.load('Tiles/orange_final_tile.png')
PURPLE_TILE = pygame.image.load('Tiles/purple_tile.png')
PURPLE_FINAL_TILE = pygame.image.load('Tiles/purple_final_tile.png')
RED_TILE = pygame.image.load('Tiles/red_tile.png') 
RED_FINAL_TILE = pygame.image.load('Tiles/red_final_tile.png')
YELLOW_TILE = pygame.image.load('Tiles/yellow_tile.png')
YELLOW_FINAL_TILE = pygame.image.load('Tiles/yellow_final_tile.png')


#rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235)

WIDTH, HEIGHT = 840, 640
SQUARE_WIDTH, SQUARE_HEIGHT = 500, 500
ROWS, COLS = 4, 4
SQUARE_SIZE = SQUARE_WIDTH//COLS

TEXTCOLOR = BLACK