from buildings import *
from troops import *
import numpy as np
import graphics as gr


class Player:
    def __init__(self, team, troops, buildings, resources, buttons):
        self.team = team
        self.troops = troops
        self.buildings = buildings
        self.resources = resources
        self.buttons = buttons

    def buy(self, item):
        if all(np.greater_equal(self.resources, item.cost)):
            for index, res in enumerate(self.resources):
                self.resources[index] = res - item.cost[index]
            item.team = self.team
            if isinstance(item, Troop):
                self.troops.append(item)  # this item is the troop that is being added
            elif isinstance(item, Building):
                item.level += 1  # this item is the building that is being upgraded

    def death(self):
        for item in self.troops:
            if item.hp <= 0:
                self.troops.remove(item)
        for item in self.buildings:
            if item.hp <= 0:
                self.buildings.remove(item)

    def update(self, enmy_trps):
        for building in self.buildings:
            if building.level > 0:
                if isinstance(building, Lumbermill):
                    building.add_wood(self)
                if isinstance(building, Mine):
                    building.add_gold(self)
                    building.add_iron(self)
        for troop in self.troops:
            troop.track()
            troop.move()
            troop.collision(self.troops)
            troop.collision(enmy_trps)
            troop.attack()

        self.death()

    def update_window(self, screen):
        select = 0
        for building in self.buildings:
            building.open_window(screen)
            if isinstance(building, Castle):
                building.buy_warrior(self)
                building.buy_archer(self)
            elif isinstance(building, Lumbermill):
                building.buy_upgrade(self)
            elif isinstance(building, Mine):
                building.buy_upgrade(self)

            '''
            deleting the buttons if no building is selected:
            '''

            if building.selected:
                select += 1

            if select == 0:
                self.buttons = {}

        for button in self.buttons.values():
            gr.draw_object((button.x, button.y), (0, 0), gr.img('Window_box'), screen)

    def draw_all(self, cam_pos, screen):
        for building in self.buildings:
            b_img = gr.img(building.name)
            if isinstance(building, Lumbermill) and building.level == 0:
                b_img = gr.img('Trees')
            elif isinstance(building, Mine) and building.level == 0:
                b_img = gr.img('Rocks')
            gr.draw_object((building.x, building.y), cam_pos, b_img, screen)
        for troop in self.troops:
            gr.draw_object((troop.x, troop.y), cam_pos, gr.img(troop.name), screen)

    def select_troop(self, pos):
        for troop in self.troops:
            troop.select(pos)

    def select_build(self, pos):
        for building in self.buildings:
            building.select(pos)


players = [Player(1, [],
                  [Castle(1, (100, 0))] + [Lumbermill(1, tree) for tree in gr.tree_positionsN] + [Mine(1, rock)
                                                                                                        for rock in
                                                                                                        gr.rock_positionsN],
                  [0, 100, 0, 0], {}), Player(2, [], [Castle(2, (2600, 1600))] + [Lumbermill(2, tree) for tree in
                                                                                     gr.tree_positionsS] + [
                                                  Mine(2, rock) for rock in gr.rock_positionsS], [0, 100, 0, 0], {})]
