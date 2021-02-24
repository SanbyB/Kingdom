import pygame
import numpy as np
import random
from PIL import Image

map_width, map_height = 3000, 2000


def draw_screen(screen):
    screen.fill((20, 150, 60))



def img(im):
    image = pygame.image.load(str(im) + '.png')
    return image


def img_size(im):
    im_size = Image.open(str(im) + '.png')
    return im_size.size



def rand_pos():
    '''
    function for generating the random positions of the flowers and grass
    '''
    pos = []
    for i in range(10):
        for j in range(10):
            pos.append((i * 350 + random.randint(-150, 150), j * 250 - 200 + random.randint(-100, 100)))
    return pos


def draw_object(pos, cam_pos, obj, screen):
    screen.blit(obj, np.array(pos) + np.array(cam_pos))


def draw_objects(pos, cam_pos, obj, screen):
    '''
    takes an array of positions (x, y)
    and draws the given object onto the screen
    at the given positions
    '''
    for p in pos:
        screen.blit(obj, np.array(p) + np.array(cam_pos))


grass_position = rand_pos()
flower_position = rand_pos()


def draw_backgroud(cam_pos, screen):
    cam_r, cam_u = cam_pos

    draw_objects(flower_position, cam_pos, pygame.transform.scale(img('Flowers'), (30, 33)),
                 screen)  # draws the flowers
    draw_objects(grass_position, cam_pos, pygame.transform.scale(img('Grass'), (30, 33)), screen)  # draws the grass

    x = np.arange(-1300, 1300, 5)  # defining the shape of the river
    y = -0.000001 * x ** 3

    for i in range(len(x)):
        # drawing the river as continuous circles which change size slightly to imitate flowing water
        pygame.draw.circle(screen, (5, 179, 237), (int(x[i]) + 1500 + cam_r, int(y[i]) + 1000 + cam_u),
                           random.randint(38, 40), 0)


def cam_move(event, move):
    '''
    when pressed the wasd keys set the movement speed of the camera to the value m
    '''
    cam_right_move, cam_up_move = 0, 0

    if move:
        m = 80
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


def cam(cam_right, cam_up, crm, cum):
    '''
    returns the position of the camera given the inputs of where the camera
    currently is, and the movement speed of it, also restricts the cameras frame
    '''
    cam_right += crm  # cam_right_move
    cam_up += cum  # cam_up_move

    if cam_up > 400:
        cam_up = 400

    if cam_up < -map_height + 800:
        cam_up = -map_height + 800

    if cam_right > 400:
        cam_right = 400

    if cam_right < -map_height + 400:
        cam_right = -map_height + 400

    return cam_right, cam_up


tree_positionsN = ((1500, 100), (500, 300), (900, 0), (2000, -150), (1400, 700), (200, 800), (100, 1800), (-100, 100))
tree_positionsS = ((1800, 1000), (2400, 1700), (2100, 2000), (1400, 1600), (2300, 1200), (2800, 1200), (2800, 200),
                   (2950, 1850))
tree_positions = tree_positionsN + tree_positionsS
rock_positionsN = ((1200, 400), (600, 100), (1200, -150), (1700, 200), (800, 700), (0, 600), (300, 1400), (200, -200))
rock_positionsS = ((2100, 1000), (2600, 1400), (1200, 1900), (1900, 1500), (2500, 2000), (2900, 700), (3000, -100),
                   (1150, 1150))
rock_positions = rock_positionsN + rock_positionsS

