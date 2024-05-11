import pygame as pg
from pgbase import PGBase
from ufo import UFO
from goroshki import Goroh
from const import *
from platforma import Platforma
from yabloki import Apple
from boom import Boom


pg.init()
cnt = 0
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))
end_game = False
obj_ufo = []  # тарелки
obj = Platforma()  # платформа
obj_goroshki = []  # выстрелы тарелок
obj_platforma = []  # выстрелы платформы
bomb_rects = []  # список бомбочек для проверки
booms = []

while not end_game:
    # Анализ управления=======================================
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end_game = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                obj_platforma.append(Apple(*obj.get_pos()))
                obj.change_move(0, 0)
            elif event.key == pg.K_LEFT:
                obj.change_move(-1, 0)
            elif event.key == pg.K_RIGHT:
                obj.change_move(1, 0)
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            booms.append(Boom(x, y))
    # Расчеты=================================================
    if len(obj_ufo) < 3:
        obj_ufo.append(UFO())
    # Отрисовка===============================================
    screen.fill('blue')
    #  отрисовка и движение выстрелов платформы
    temp = []
    for g in obj_platforma:
        g.move()
        g.draw(screen)
        if g.get_pos()[1] > 0:
            temp.append(g)
    obj_platforma = temp.copy()

    #  отрисовка и движение выстрелов тарелок
    temp = []
    bomb_rects = []
    for g in obj_goroshki:
        g.move()
        g.draw(screen)
        if g.get_pos()[1] < HEIGHT:
            temp.append(g)
            bomb_rects.append(g.get_rect())
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
    
    #  отрисовка Взрывов
    temp = []
    for g in booms:
        if not g.draw(screen):
            temp.append(g)
    booms = temp.copy()

    obj.move()
    obj.draw(screen)
    pg.display.flip()
    # Пауза===================================================
    clock.tick(FPS)
pg.quit()
