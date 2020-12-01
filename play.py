import graphics as gr


def move(troop):
    for t in troop:
        # movement of the troops
        if abs(t.pos_targetx) > 1 and abs(t.pos_targety) > 1:
            v_x, v_y = t.velocity()
            t.x += v_x
            t.y += v_y
            t.pos_targetx -= v_x
            t.pos_targety -= v_y
        else:
            t.pos_targetx = t.pos_targety = 0


def collision(troop):
    # troop collision
    for t in troop:
        for t1 in troop:
            if t != t1 and (
                    abs(t.x + t.x_hit/2 - t1.x - t1.x_hit/2) <= (t.x_hit + t1.x_hit) / 2 and abs(t.y + t.y_hit/2 - t1.y - t1.y_hit/2) <= (t.y_hit + t1.y_hit) / 2):
                if t.x > t1.x:
                    t.x += 1
                else:
                    t.x -= 1
                if t.y > t1.y:
                    t.y += 1
                else:
                    t.y -= 1


def attack(troop):
    # troop attack
    for t in troop:
        if t.target is not None and t.team != t.target.team:
            if abs(t.x - t.target.x) <= (t.x_hit + t.target.x_hit) / 2 + t.attack_range and abs(
                    t.y - t.target.y) <= (
                    t.y_hit + t.target.y_hit) / 2 + t.attack_range:
                t.target.hp -= t.damage / t.attack_speed
                t.pos_targetx = t.pos_targety = 0

            else:  # follows the troop its attacking
                t.pos_targetx, t.pos_targety = t.target.x - t.x, t.target.y - t.y


def die(troop):
    for t in troop:
        if t.hp <= 0:
            troop.remove(t)


def troop_select(troop):
    tr = []
    for t in troop:
        if t.selected:
            tr.append(1)
    if len(tr) == 0:
        return False
    else:
        return True


def add_troop(troop, type, team, bx, by, mouse_pos):
    if 650 < mouse_pos[0] < 650 + bx and 350 < mouse_pos[1] < 350 + by:
        troop.append(type(team, 100, 0))


def turn_pg(pg, mouse_pos):
    mx, my = mouse_pos
    if 1110 < mx < 1186 and 740 < my < 783:  # page turning for buying troops
        pg += 1
    if 650 < mx < 726 and 740 < my < 783:
        pg -= 1
    if pg < 0:
        pg = 0
    return pg
