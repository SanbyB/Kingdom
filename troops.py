import numpy as np
import objects as ob


class Troop(ob.Object):
    def __init__(self, team, hp, damage, attack_range, attack_speed, movement_speed, x, y, name, selected, pos_targetx,
                 pos_targety, target, cost, level):
        self.movement_speed = movement_speed
        self.pos_targetx, self.pos_targety = pos_targetx, pos_targety
        super().__init__(team, hp, damage, attack_range, attack_speed, x, y, name, selected, target, cost, level)

    def velocity(self):
        dist_x, dist_y = self.pos_targetx, self.pos_targety
        dist = np.sqrt(dist_x ** 2 + dist_y ** 2)
        v_x = self.movement_speed * dist_x / dist
        v_y = self.movement_speed * dist_y / dist
        return v_x, v_y


class Warrior(Troop):
    def __init__(self, team, x, y):
        super().__init__(team, 50, 5, 10, 10, 3, x, y, 'Warrior', False, 0, 0, None, 50, 1)


class Archer(Troop):
    def __init__(self, team, x, y):
        super().__init__(team, 40, 4, 200, 10, 3, x, y, 'Archer', False, 0, 0, None, 100, 1)


class Spearman(Troop):
    def __init__(self, team, x, y):
        super().__init__(team, 40, 4, 200, 10, 3, x, y, 'Spearman', False, 0, 0, None, 100, 1)


class Giant(Troop):
    def __init__(self, team, x, y):
        super().__init__(team, 40, 4, 200, 10, 3, x, y, 'Giant', False, 0, 0, None, 100, 1)


class Cannon(Troop):
    def __init__(self, team, x, y):
        super().__init__(team, 40, 4, 200, 10, 3, x, y, 'Cannon', False, 0, 0, None, 100, 1)
