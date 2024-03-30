#!/usr/bin/env python3
# coding:utf-8
import pygame as pg
from Base_Class import PGObject

pg.init()
clock = pg.time.Clock()
FPS = 30
screen = pg.display.set_mode((800, 600))
stop_game = False
obj = PGObject()

while not stop_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            stop_game = True

    obj.move(screen, 1, 1)
    screen.fill('red')
    obj.draw(screen)
    pg.display.flip()
    clock.tick(FPS)
pg.quit()
