import pygame as pg
from pgbase import PGBase
from ufo import UFO
from goroshki import Goroh
from const import *
from platforma import Platforma

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))
end_game = False
obj_ufo = []
obj = Platforma()
obj_goroshki = []

while not end_game:
    # Анализ управления=======================================
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end_game = True
    # Расчеты=================================================
    if len(obj_ufo) < 3:
        obj_ufo.append(UFO())
    # Отрисовка===============================================
    screen.fill('blue')
    temp = []
    for g in obj_goroshki:
        g.move()
        g.draw(screen)
        if g.get_pos()[1] < HEIGHT:
            temp.append(g)
    obj_goroshki = temp.copy()

    temp = []
    for d in obj_ufo:
        if d.shot():
            obj_goroshki.append(Goroh(*d.get_pos()))
        d.move()
        if d.get_pos()[0] < WIDTH:
            temp.append(d)
        d.draw(screen)
    obj_ufo = temp.copy()

    obj.draw(screen)
    pg.display.flip()
    # Пауза===================================================
    clock.tick(FPS)
pg.quit()
