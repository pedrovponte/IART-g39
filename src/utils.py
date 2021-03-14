import pygame  


def chooseAlg():

    print("Please, choose which search method do you wish to use:")
    print("1) Human Interaction.")
    print("A) Breadth-first search.")
    print("B) Depth-first search.")
    print("C) Progressive deepening.")
    print("D) Uniform cost search.")
    print("E) Greedy.")
    print("F) A*.")

    ans=input()
    
    if ans == "A" or ans == "a":
        return 'A'
    elif ans == "B" or ans == "b":
        return 'B'
    elif ans == "C" or ans == "c":
        return 'C'
    elif ans == "D" or ans == "d":
        return 'D'
    elif ans == "E" or ans == "e":
        return 'E'
    elif ans == "F" or ans == "f":
        return 'F'
    elif ans == "1":
        return '1'
    else:
        chooseAlg()

# create the Surface and Rect objects for some text.        
def makeText(text, color, top, left):
    pygame.font.init()
    BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
    
    textSurf = BASICFONT.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)