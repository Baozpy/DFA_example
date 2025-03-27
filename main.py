import pygame

from wildfire import Wildfire

if __name__ == '__main__':

    x = 200
    y = 200

    pygame.init()
    pygame.display.set_caption("Wildfire Model")
    wildfire = Wildfire(x, y)
    wildfire.run()
