#!/usr/bin/env python3
# coding:utf-8
import sys
from copy import deepcopy

import pygame as pg


pg.init()
scr = pg.display.set_mode((800, 600))
sp = ['I', 'J', 'L']
TILE_TYPES = [(pg.image.load(f'{letter}.png'), letter) for letter in sp]
# TILE_TYPES = [(pg.image.load('I.png'), 'I'),
#               (pg.image.load('J.png'), 'J'),
#               (pg.image.load('L.png'), 'L')
#               ]
print(TILE_TYPES)
tetromino_list = TILE_TYPES
print(tetromino_list)

im1 = pg.image.load('L.png')

end = False
while not end:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = True
    scr.fill('blue')
    scr.blit(im1, (20, 20))
    pg.display.flip()
pg.quit()

