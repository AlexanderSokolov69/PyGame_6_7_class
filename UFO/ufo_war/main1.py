import pygame as pg
from pgbase import PGBase
from ufo import UFO
from goroshki import Goroh
from const import *
from platforma import Platforma
from yabloki import Apple
from boom import Boom
from tablo import Tablo

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))
end_game = False
obj_all = pg.sprite.Group()
obj_ufo = pg.sprite.Group()  # тарелки
obj_goroshki = pg.sprite.Group()  # выстрелы тарелок
obj_platforma = pg.sprite.Group()  # выстрелы платформы
bomb_rects = pg.sprite.Group()  # список бомбочек
booms = pg.sprite.Group()

tablo = Tablo(obj_all)
obj = Platforma(obj_all)  # платформа

count = 0
while not end_game:
    # Анализ управления=======================================
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end_game = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                Apple(*obj.get_pos(), 10, obj_all, obj_platforma)
                count -= 1
            elif event.key == pg.K_SPACE:
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
            count += 3

    hits = pg.sprite.spritecollide(obj, obj_goroshki, True)
    if hits:
        Boom(*obj.get_pos(), 10, obj_all)
        count -= 1

    tablo.write(f'{count:04}', 'green')
    # Отрисовка===============================================
    screen.fill('blue')
    #  отрисовка и движение выстрелов платформы

    obj_all.update()
    obj_all.draw(screen)
    pg.display.flip()
    # Пауза===================================================
    clock.tick(FPS)
pg.quit()
