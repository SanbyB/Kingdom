import pygame
import graphics as gr


class Object:
    def __init__(self, team, hp, damage, attack_range, attack_speed, x, y, name, selected, target, cost, level):
        self.team = team
        self.name = name
        self.hp = hp
        self.damage = damage
        self.attack_range = attack_range
        self.attack_speed = attack_speed
        self.x, self.y = x, y
        self.selected = selected
        self.target = target
        self.cost = cost
        self.level = level
        self.im = pygame.image.load(r'C:\Users\bensa\PycharmProjects\Kingdom\graphics\\' + name + '.png')
        self.x_hit = gr.img_size(name)[0]
        self.y_hit = gr.img_size(name)[1]

    def draw_object(self, screen, cam_pos):
        cam_r, cam_u = cam_pos
        screen.blit(self.im, (self.x + cam_r, self.y + cam_u))


def draw(lt, cam_pos):
    for x in lt:
        Object.draw_object(x, gr.screen, cam_pos)


def select(ob, mouse_pos, cam_pos, desel):
    mx, my = mouse_pos
    cr, cu = cam_pos
    for o in ob:
        if o.selected and o.x < mx - cr < o.x + o.x_hit and o.y < my - cu < o.y + o.y_hit:
            o.selected = False
        else:
            if desel:  # deselecting objects
                o.selected = False
            if o.x < mx - cr < o.x + o.x_hit and o.y < my - cu < o.y + o.y_hit:  # selecting an object
                o.selected = True


def move_attack(troop, mouse_pos, cam_pos):
    mx, my = mouse_pos
    cr, cu = cam_pos
    for t in troop:
        if t.selected:  # selecting a location as a target
            t.pos_targetx, t.pos_targety = (mx - cr - t.x_hit / 2 - t.x, my - cu - t.y_hit / 2 - t.y)
            t.selected = False
            t.target = None
            for t1 in troop:  # selecting a troop as a target
                if t1.x < mx - cr < t1.x + t1.x_hit and t1.y < my - cu < t1.y + t1.y_hit:
                    t.target = t1
