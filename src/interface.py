
import game
from game import Game
import levels
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

# define a main function
def main():
    BACKGROUND = (0, 0, 0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0, 0, 255)
    ORANGE = (62 , 124, 124)

    colours = {
        '0': WHITE,
        '1': RED,
        '2': GREEN,
        '3': BLUE,
        '4': ORANGE
    }

   # game.init()
   # screen = game.display.set_mode((600,600))


    # main loop
    while running:
        screen.fill(BACKGROUND)
       # draw_game(screen)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()