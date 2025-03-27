import sys

import pygame

from map import Map

max_fps = 50
RED = (255, 0, 0)
# 黑色空地
BACKGROUND = (0, 0, 0)


class Wildfire:
    cell_width = 3
    cell_height = 3

    def __init__(self, x, y):
        self.time = 0
        self.total_cell = x * y
        self.screen = pygame.display.set_mode([x * self.cell_width, y * self.cell_height])
        self.map = Map(x, y)

    # draw cells
    def draw_cells(self):
        for row in self.map.cells:
            for cell in row:
                x = cell.x
                y = cell.y
                if cell.tree is None:
                    color = BACKGROUND
                else:
                    if cell.tree.on_fire:
                        color = (cell.tree.weight, 0, 0)
                    else:
                        color = (0, cell.tree.weight, 0)
                pygame.draw.rect(self.screen, color,
                                 [x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height])
        pygame.display.flip()

    def show(self):
        self.draw_cells()

    def run(self):
        clock = pygame.time.Clock()

        while True:
            self.time += 1
            print(format("Time: %d") % self.time)

            # clock tick
            clock.tick(max_fps)

            # action exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # show
            self.show()

            # next
            self.map.next()
