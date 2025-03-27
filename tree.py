import random

max_growth_rate = 10
max_weight = 255
min_fire_speed = 50


class Tree:

    def __init__(self):
        self.weight = 0
        self.growth_rate = int(random.random() * max_growth_rate + 1)
        self.fire_rate = int(random.random() * 100 + min_fire_speed)
        self.on_fire = False
        self.is_dead = False
        self.going_fire = False

    def tree_life(self):
        if self.is_dead:
            return
        if self.on_fire:
            self.weight -= self.fire_rate
            if self.weight <= 0:
                self.is_dead = True
                self.on_fire = False
        elif self.weight < max_weight:
            self.weight += self.growth_rate
            if self.weight > max_weight:
                self.weight = max_weight
        if self.going_fire:
            self.on_fire = True
            self.going_fire = False

    def next(self, going_fire):
        self.tree_life()
        self.going_fire = going_fire


if __name__ == '__main__':
    tree = Tree()
    print("Tree growth rate: %d" % tree.growth_rate)
    print("Tree fire rate: %d" % tree.fire_rate)
    time = 0
    while tree.weight < max_weight:
        time += 1
        tree.next(False)
        print("Time: %d, tree weight: %d" % (time, tree.weight))

    tree.on_fire = True
    while not tree.is_dead:
        time += 1
        tree.next(False)
        print("Time: %d, tree weight: %d" % (time, tree.weight))
