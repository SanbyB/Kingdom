import objects as ob
import graphics as gr
import troops as trp
import pygame


class Castle(ob.Object):
    def __init__(self, team, x, y, selected, target):
        super().__init__(team, 1000, 2, 20, 10, x, y, 'Castle', selected, target, 0, 0)


class Window:
    def __init__(self, team, pos):
        self.team = team
        self.pos = pos
        self.x_hit, self.y_hit = gr.img_size('Window_box')
        self.im = gr.window_box


class Castle_Window(Window):
    def __init__(self, team, pos):
        super().__init__(team, pos)
        self.tp = {0: trp.Warrior, 1: trp.Archer, 2: trp.Spearman, 3: trp.Giant, 4: trp.Cannon}
        self.buy = self.tp[self.pos]
        self.name = {0: 'Warrior', 1: 'Archer', 2: 'Spearman', 3: 'Giant', 4: 'Cannon'}
        self.x, self.y = 660, 370 + (self.pos % 3) * self.y_hit
        if self.team == 'red':
            self.place = (100, 0)
        else:
            self.place = (2600, 1600)

    def window_text(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 40)
        buy = font.render('Buy ' + self.name[self.pos], True, (0, 0, 0))
        screen.blit(buy, (self.x, self.y))


def window_frame(screen):
    screen.blit(gr.window, (600, 300))

    x_hit, y_hit = gr.img_size('Window_box')

    for b in range(3):
        screen.blit(gr.window_box, (650, 350 + b * y_hit))
