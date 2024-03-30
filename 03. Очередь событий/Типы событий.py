#!/usr/bin/env python3
# coding:utf-8
import pygame as pg
import pygame.locals as lc
import json


size = width, height = 800, 600
pg.init()
scr = pg.display.set_mode(size)
end_game = False

while not end_game:
    for event in pg.event.get():
        if event.type == lc.QUIT:
            end_game = True
        elif event.type == lc.MOUSEMOTION:
            pg.display.set_caption(f"pos:{event.pos}, rel:{event.rel}")
            continue
        print(f"{event}")

pg.quit()
json.d