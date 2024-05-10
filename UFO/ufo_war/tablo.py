#!/usr/bin/env python3
# coding:utf-8
from pgbase import PGBase
import pygame as pg
from const import *


class Tablo(PGBase):
    def __init__(self, *groups):
        super().__init__(60, 30, 10, *groups)
        self.font = pg.font.SysFont(None, 50)

    def create(self):
        scr = pg.image.load('tablo.png')
        scr.set_colorkey('white')
        return scr

    def write(self, text, color='red'):
        self.image = self.create()
        data = self.font.render(text, False, color)
        self.image.blit(data, (6, 8))
