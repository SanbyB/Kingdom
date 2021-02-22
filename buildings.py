import troops as tr
import graphics as gr


class Building:
    def __init__(self, team, name, pos, hp, damage, attack_range, attack_speed, cost):
        self.team = team
        self.name = name
        self.x, self.y = pos
        self.hp = hp
        self.damage = damage
        self.attack_range = attack_range
        self.attack_speed = attack_speed
        self.cost = cost
        self.level = 0
        self.target = None
        self.selected = False
        self.image_size = gr.img_size(name)
        self.x_hit, self.y_hit = self.image_size
        self.tag = None

    def select(self, click):
        if self.x < click[0] < self.x_hit + self.x and self.y < click[1] < self.y_hit + self.y:
            self.selected = True
        else:
            self.selected = False

    def open_window(self, screen):
        if self.selected:
            gr.draw_object((600, 300), (0, 0), gr.img('Window'), screen)

    def add_button(self, player, obj, pos, but):
        if self.selected:
            player.buttons[but] = Button(obj, pos)  # 'but' is the index in the dict of buttons


class Button:
    def __init__(self, obj, pos):
        self.obj = obj
        self.x, self.y = pos
        self.image_size = gr.img_size('Window_box')

    def click(self, click, player):
        if self.x < click[0] < self.x + self.image_size[0] and self.y < click[1] < self.y + self.image_size[1]:
            player.buy(self.obj)


class Castle(Building):
    def __init__(self, team, pos):
        super().__init__(team, 'Castle', pos, 1, 2, 20, 10, (0, 0, 0, 0))

    def spawn(self):
        x, y = 100, 0
        if self.team == 2:
            x, y = 2600, 1600
        return x, y

    def buy_warrior(self, player):
        x, y = self.spawn()
        self.add_button(player, tr.Warrior(self.team, x, y), (660, 370), '1')

    def buy_archer(self, player):
        x, y = self.spawn()
        self.add_button(player, tr.Archer(self.team, x, y), (660, 490), '2')


class Lumbermill(Building):
    def __init__(self, team, pos):
        super().__init__(team, 'LumberMill', pos, 10, 0, 0, 1, (0, 5, 0, 0))

    def buy_upgrade(self, player):
        self.add_button(player, self, (660, 370), '1')

    def add_wood(self, player):
        player.resources[0] += self.level * 0.01


class Mine(Building):
    def __init__(self, team, pos):
        super().__init__(team, 'Mine', pos, 1000, 0, 0, 1, (5, 0, 0, 0))

    def buy_upgrade(self, player):
        self.add_button(player, self, (660, 370), '1')

    def add_gold(self, player):
        player.resources[1] += self.level * 0.01

    def add_iron(self, player):
        if self.level > 2:
            player.resources[2] += (self.level - 1) * 0.01




