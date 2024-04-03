import pygame as pg
from pgbase import PGBase


FPS = 30
WIDTH, HEIGHT = 800, 600

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))

stop_game = False
obj = PGBase(speed=1)
while not stop_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            stop_game = True
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            ox, oy = obj.get_pos()
            if x > ox:
                dx = 1
            elif x < ox:
                dx = -1
            else:
                dx = 0
            if y > oy:
                dy = 1
            elif y < oy:
                dy = -1
            else:
                dy = 0
            obj.change_move(dx, dy)

    obj.move()
    screen.fill('blue')
    # #################
    obj.draw(screen)
    # #################
    pg.display.flip()
    clock.tick(FPS)
pg.quit()
