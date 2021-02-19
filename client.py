import pygame
import numpy as np
from network import Network
import graphics as gr

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


def main():
    run = True
    n = Network()
    p1 = n.getP()
    #clock = pygame.time.Clock()

    cam_right, cam_up, cam_right_move, cam_up_move = 0, 0, 0, 0  # initialises camera

    while run:
        #clock.tick(100)

        p2 = n.send(p1)

        gr.draw_screen(screen)

        cam_pos = cam_right, cam_up = gr.cam(cam_right, cam_up, cam_right_move, cam_up_move)  # cam position
        gr.draw_backgroud((cam_right, cam_up), screen)

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:  # closes the window if the delete key is pressed
                    run = False

                cam_right_move, cam_up_move = gr.cam_move(event, True)  # camera movement

            if event.type == pygame.KEYUP:
                cam_right_move, cam_up_move = gr.cam_move(event, False)

            mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    p1.select_troop(np.array(mouse_pos) - np.array(cam_pos))
                    for button in p1.buttons.values():
                        button.click(mouse_pos, p1)

                if event.button == 3:

                    p1.select_build(np.array(mouse_pos) - np.array(cam_pos))

                    for troop in p1.troops + p2.troops:  # target positions of troops
                        if troop.selected:
                            troop.targ(np.array(mouse_pos) - np.array(cam_pos),
                                       p1.troops + p2.troops + p1.buildings + p2.buildings)

        p1.update(p2.troops)
        p1.draw_all(cam_pos, screen)
        p2.draw_all(cam_pos, screen)
        p1.update_window(screen)

        pygame.display.update()


main()
