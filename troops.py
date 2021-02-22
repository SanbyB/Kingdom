import numpy as np
import graphics as gr


class Troop:
    def __init__(self, team, name, pos, hp, damage, attack_range, attack_speed, movement_speed, cost):
        self.team = team
        self.name = name
        self.x, self.y = pos
        self.hp = hp
        self.damage = damage
        self.attack_range = attack_range
        self.attack_speed = attack_speed
        self.movement_speed = movement_speed
        self.cost = cost
        self.level = 0
        self.target = (0, 0)
        self.target_ob = None
        self.selected = False
        self.image_size = gr.img_size(name)
        self.x_hit, self.y_hit = self.image_size
        self.tag = None

    def select(self, click):  # selects a troop that is left clicked
        if self.x < click[0] < self.x + self.image_size[0] and self.y < click[1] < self.y + self.image_size[1]:
            self.selected = True
        else:
            self.selected = False

    def targ(self, click, targets):  # sets the target location for the troop
        if self.selected:
            self.target = np.array(click) - np.array((self.x, self.y)) - np.array(
                self.image_size) / 2  # moves middle of the troop to target
            self.selected = False
            self.target_ob = None
            for target in targets:
                if target.x < click[0] < target.x_hit + target.x and target.y < click[1] < target.y_hit + target.y:
                    self.target_ob = target

    def movement(self, rng):  # moves the troop to the target
        if self.target[0] == 0 and self.target[1] == 0:
            pass  # avoids the division by zero error that follows if the target is (0, 0)
        elif abs(rng[0]) > 2 and abs(rng[1]) > 2:
            dist_x, dist_y = self.target
            dist = np.sqrt(dist_x ** 2 + dist_y ** 2)  # pythagorean distance
            v_x = self.movement_speed * dist_x / dist  # velocity vector
            v_y = self.movement_speed * dist_y / dist
            self.x += v_x
            self.y += v_y
            tarx = self.target[0]
            tary = self.target[1]
            tarx -= v_x
            tary -= v_y
            self.target = tarx, tary
        else:
            self.target = (0, 0)

    def track(self):
        if self.target_ob is not None:  # tracking a targeted troop
            if self.target_ob.team != self.team and abs(
                    self.target_ob.x + self.target_ob.x_hit / 2 - self.x - self.x_hit / 2) < self.attack_range and abs(
                self.target_ob.y + self.target_ob.y_hit / 2 - self.y - self.y_hit / 2) < self.attack_range:
                self.target = (0, 0)
            else:
                self.target = self.target_ob.x - self.x, self.target_ob.y - self.y

    def move(self):
        if self.target_ob is None:
            self.movement(self.target)
        elif self.target_ob.team != self.team:
            self.movement(
                abs(np.array(self.target)) - np.array(((self.x_hit + self.target_ob.x_hit) / 2 + self.attack_range,
                                                       (self.y_hit + self.target_ob.y_hit) / 2 + self.attack_range)))

        else:
            self.movement(abs(np.array(self.target)) - np.array(((self.x_hit + self.target_ob.x_hit) / 2,
                                                                 (self.y_hit + self.target_ob.y_hit) / 2)))

    def collision(self, troops):
        for troop in troops:
            if troop != self and (
                    abs(troop.x + troop.x_hit / 2 - self.x - self.x_hit / 2) <= (troop.x_hit + self.x_hit) / 2 and abs(
                troop.y + troop.y_hit / 2 - self.y - self.y_hit / 2) <= (troop.y_hit + self.y_hit) / 2):
                if troop.x > self.x:
                    troop.x += 1
                else:
                    troop.x -= 1
                if troop.y > self.y:
                    troop.y += 1
                else:
                    troop.y -= 1
        if self.x < -200:
            self.x = -198
        if self.y < -280:
            self.y = -278


class Warrior(Troop):
    def __init__(self, team, x, y):
        super().__init__(team, 'Warrior', (x, y), 50, 5, 10, 10, 14, (1, 1, 0, 0))


class Archer(Troop):
    def __init__(self, team, x, y):
        super().__init__(team, 'Archer', (x, y), 50, 4, 300, 10, 14, (2, 2, 0, 0))

