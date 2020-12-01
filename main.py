import pygame
import play as pl
import graphics as gr
import troops as trp
import buildings as bld
import objects as ob
import random

import numpy as np

pygame.init()

cam_up, cam_right = 0, 0
cam_right_move, cam_up_move = 0, 0

troop = [trp.Warrior('red', random.randint(100, 1000), random.randint(100, 1000)),
         trp.Archer('green', random.randint(100, 1000), random.randint(100, 600))]
building = [bld.Castle('red', 100, 0, False, None), bld.Castle('green', 2600, 1600, False, None)]
pg = 0


running = True
cam_pos = (0, 0)

while running:
    window = []
    for b in building:  # the window for buying things
        if b.name == 'Castle' and b.selected:
            try:
                window.append(bld.Castle_Window(b.team, 0 + 3 * pg))
            except:
                pass
            try:
                window.append(bld.Castle_Window(b.team, 1 + 3 * pg))
            except:
                pass
            try:
                window.append(bld.Castle_Window(b.team, 2 + 3 * pg))
            except:
                pass

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:  # Del key closes the game
                running = False

            cam_right_move, cam_up_move = gr.cam(event, True)  # camera movement

        if event.type == pygame.KEYUP:
            cam_right_move, cam_up_move = gr.cam(event, False)

        mouse_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                ob.select(troop, mouse_pos, cam_pos, False)
                for b in building:
                    if b.selected:
                        pg = pl.turn_pg(pg, mouse_pos)

                for w in window:
                    if w.x < mouse_pos[0] < w.x + w.x_hit and w.y < mouse_pos[1] < w.y + w.y_hit:  # buying troops
                        troop.append(w.buy(w.team, w.place[0], w.place[1]))

            if event.button == 3:
                pg = 0
                if not pl.troop_select(troop):
                    ob.select(building, mouse_pos, cam_pos, True)
                ob.move_attack(troop, mouse_pos, cam_pos)

    pl.move(troop)
    pl.collision(troop)
    pl.attack(troop)
    pl.die(troop)

    cam_right += cam_right_move
    cam_up += cam_up_move

    if cam_up > 400:
        cam_up = 400

    if cam_up < -gr.map_height + 800:
        cam_up = -gr.map_height + 800

    if cam_right > 400:
        cam_right = 400

    if cam_right < -gr.map_height + 400:
        cam_right = -gr.map_height + 400

    cam_pos = (cam_right, cam_up)

    gr.draw_screen()
    gr.draw_object(gr.screen, gr.grass_position, cam_pos, gr.grass)
    gr.draw_object(gr.screen, gr.flower_position, cam_pos, gr.flower)
    gr.draw_river(cam_pos)
    gr.draw_object(gr.screen, gr.tree_positions, cam_pos, gr.tree)
    gr.draw_object(gr.screen, gr.rock_positions, cam_pos, gr.rock)
    ob.draw(building, cam_pos)
    ob.draw(troop, cam_pos)
    for b in building:  # the window for buying things
        if b.name == 'Castle' and b.selected:
            bld.window_frame(gr.screen)  # draws window frame
            gr.screen.blit(gr.pg_rarrow, (1110, 740))
            gr.screen.blit(gr.pg_larrow, (650, 740))
    for w in window:
        bld.Castle_Window(w.team, w.pos).window_text(gr.screen)  # writes the window text
    pygame.display.update()
