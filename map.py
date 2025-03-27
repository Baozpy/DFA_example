import random

from tree import Tree

thunder_rate = 0.5


class Map:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cells = []
        for i in range(x):
            row = []
            for j in range(y):
                tree = MapCell(i, j)
                row.append(tree)
            self.cells.append(row)

    def cell_going_fire(self, cell):
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if cell.x + i < 0 or cell.x + i >= self.x:
                    continue
                if cell.y + j < 0 or cell.y + j >= self.y:
                    continue
                neighbor = self.cells[cell.x + i][cell.y + j]
                # 如果这个cell的neighbor有树并且着火了
                if neighbor.tree is not None and neighbor.tree.on_fire:
                    return True
        return False

    def next(self):
        for row in self.cells:
            for cell in row:
                if cell.tree is not None:
                    cell.tree.next(self.cell_going_fire(cell))
                    if cell.tree.is_dead:
                        cell.tree = None
                else:
                    cell.tree_born()
        self.thunder()
    # 打雷后随机选中一个格子着火
    def thunder(self):
        if random.random() < thunder_rate:
            x = int(random.random() * self.x)
            y = int(random.random() * self.y)
            tree = self.cells[x][y].tree
            if tree is not None and not tree.on_fire and not tree.is_dead:
                tree.on_fire = True
                print("thunder at (%d, %d)" % (x, y))


tree_born_rate = 0.01


class MapCell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tree = None

    def tree_born(self):
        if random.random() < tree_born_rate:
            self.tree = Tree()
