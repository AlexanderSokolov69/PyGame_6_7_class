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
obj_all = pg.sprite.Group()
obj_ufo = pg.sprite.Group()  # тарелки
obj_goroshki = pg.sprite.Group()  # выстрелы тарелок
obj_platforma = pg.sprite.Group()  # выстрелы платформы
bomb_rects = pg.sprite.Group()  # список бомбочек для проверки
booms = pg.sprite.Group()

obj = Platforma(obj_all)  # платформа
# obj_all.add(obj)

while not end_game:
    # Анализ управления=======================================
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end_game = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                Apple(*obj.get_pos(), 10, obj_all, obj_platforma)
                obj.change_move(0, 0)
            elif event.key == pg.K_LEFT:
                obj.change_move(-1, 0)
            elif event.key == pg.K_RIGHT:
                obj.change_move(1, 0)
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            pass
    # Расчеты=================================================
    if len(obj_ufo) < 3:
        UFO(obj_all, obj_ufo)
    for d in obj_ufo:
        if d.shot():
            Goroh(*d.get_pos(), 10, obj_all, obj_goroshki)
            
    for apple in obj_platforma:
        hits = pg.sprite.spritecollide(apple, obj_ufo, True)
        if hits:
            Boom(*apple.get_pos(), 10, obj_all)
            apple.kill()

    hits = pg.sprite.spritecollide(obj, obj_goroshki, True)
    if hits:
        Boom(*obj.get_pos(), 10, obj_all)
    # Отрисовка===============================================
    screen.fill('blue')
    #  отрисовка и движение выстрелов платформы

    obj_all.update()
    obj_all.draw(screen)
    pg.display.flip()
    # Пауза===================================================
    clock.tick(FPS)
pg.quit()
