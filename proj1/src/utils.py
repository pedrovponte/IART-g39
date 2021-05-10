import pygame  

# create the Surface and Rect objects for some text.        
def makeText(text, color, top, left, size):
    pygame.font.init()
    BASICFONT = pygame.font.Font('freesansbold.ttf', size)
    
    textSurf = BASICFONT.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)