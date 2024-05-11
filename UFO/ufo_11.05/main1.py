import time
import pygame as pg
from pgbase import PGBase
from ufo import UFO
from goroshki import Goroh
from const import *
from platforma import Platforma
from yabloki import Apple
from boom import Boom
from tablo import Tablo
from final import Final


pg.init()
clock = pg.time.Clock()
timer = time.time()
screen = pg.display.set_mode((WIDTH, HEIGHT))
end_game = False
obj_all = pg.sprite.Group()
obj_ufo = pg.sprite.Group()  # тарелки
obj_goroshki = pg.sprite.Group()  # выстрелы тарелок
obj_platforma = pg.sprite.Group()  # выстрелы платформы
bomb_rects = pg.sprite.Group()  # список бомбочек
booms = pg.sprite.Group()
score_apple = APPLE_START
score_ufo = 0

obj = Platforma(obj_all)  # платформа
tablo = Tablo(obj_all)

while not end_game:
    # Анализ управления=======================================
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end_game = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                Apple(*obj.get_pos(), 10, obj_all, obj_platforma)
                obj.change_move(0, 0)
                score_apple -= 1
            elif event.key == pg.K_UP:
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
        if timer + UFO_TIMER < time.time():
            UFO(obj_all, obj_ufo)
            timer = time.time()
    for d in obj_ufo:
        if d.shot():
            Goroh(*d.get_pos(), 10, obj_all, obj_goroshki)
            
    for apple in obj_platforma:
        hits = pg.sprite.spritecollide(apple, obj_ufo, True)
        if hits:
            Boom(*apple.get_pos(), 10, obj_all)
            apple.kill()
            score_apple += APPLE_PRICE
            score_ufo += 1

    hits = pg.sprite.spritecollide(obj, obj_goroshki, True)
    if hits:
        Boom(*obj.get_pos(), 10, obj_all)
        score_apple -= APPLE_PRICE

    if score_apple < 0:
        end_game = True
    tablo.write(score_apple, score_ufo)
    # Отрисовка===============================================
    screen.fill('blue')
    #  отрисовка и движение выстрелов платформы

    obj_all.update()
    obj_all.draw(screen)
    pg.display.flip()
    # Пауза===================================================
    clock.tick(FPS)

end_game = False
final = Final(obj_all)
final.write(score_ufo)
while not end_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end_game = True

    obj_all.draw(screen)
    pg.display.flip()
    
pg.quit()
