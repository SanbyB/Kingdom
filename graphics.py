import pygame
import random
import numpy as np
from PIL import Image

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

map_width, map_height = 3000, 2000


def img(im):
    return pygame.image.load(r'C:\Users\bensa\PycharmProjects\Kingdom\graphics\\' + str(im) + '.png')


def img_size(im):
    image = Image.open(r'C:\Users\bensa\PycharmProjects\Kingdom\graphics\\' + str(im) + '.png')
    return image.size


def rand_pos():
    gr = []
    for i in range(10):
        for j in range(10):
            gr.append((i * 350 + random.randint(-150, 150), j * 250 - 200 + random.randint(-100, 100)))
    return gr


castle = img('Castle')
tree = img('Trees')
rock = img('Rocks')
grass = img('Grass')
flower = img('Flowers')
window = img('Window')
window_box = img('Window_box')
pg_rarrow = img('Page_arrow')
pg_larrow = pygame.transform.flip(pg_rarrow, True, False)
grass = pygame.transform.scale(grass, (30, 33))
flower = pygame.transform.scale(flower, (30, 33))

tree_positions = ((1500, 100), (500, 300), (900, 0), (2000, -150), (1400, 700), (200, 800), (100, 1800), (-100, 100),
                  (1800, 1000), (2400, 1700), (2100, 2000), (1400, 1600), (2300, 1200), (2800, 1200), (2800, 200),
                  (2950, 1850))
rock_positions = ((1200, 400), (600, 100), (1200, -150), (1700, 200), (800, 700), (0, 600), (300, 1400), (200, -200),
                  (2100, 1000), (2600, 1400), (1200, 1900), (1900, 1500), (2500, 2000), (2900, 700), (3000, -100),
                  (1150, 1150))
grass_position = rand_pos()
flower_position = rand_pos()


def draw_screen():
    screen.fill((20, 150, 60))


def river():
    x = np.arange(-1300, 1300, 5)
    y = -0.000001 * x ** 3
    return x + 1500, y + 1000


def draw_river(cam_pos):
    cam_r, cam_u = cam_pos
    riv = river()
    for i in range(len(riv[0])):
        pygame.draw.circle(screen, (5, 179, 237), (int(riv[0][i]) + cam_r, int(riv[1][i]) + cam_u),
                           random.randint(38, 40), 0)


def draw_object(screen, pos, cam_pos, object):
    for p in pos:
        screen.blit(object, np.array(p) + np.array(cam_pos))


def cam(event, move, cam_right_move=0, cam_up_move=0):
    if move:
        m = 40
    else:
        m = 0
    if event.key == pygame.K_a:
        cam_right_move = m

    if event.key == pygame.K_d:
        cam_right_move = -m

    if event.key == pygame.K_w:
        cam_up_move = m

    if event.key == pygame.K_s:
        cam_up_move = -m

    return cam_right_move, cam_up_move



