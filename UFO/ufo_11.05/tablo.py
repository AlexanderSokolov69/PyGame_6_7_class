from pgbase import PGBase
import pygame as pg
import random as rnd
from const import *


class Tablo(PGBase):
    def __init__(self, *groups):
        super().__init__(80, 30, 10, *groups)
        self.font = pg.font.Font(None, 40)

    def create(self):
        scr = pg.image.load('tablo.png')
        scr.set_colorkey('white')
        return scr

    def write(self, count1, count2):
        self.image = self.create()
        text1 = self.font.render(str(count1), True, 'red')
        text2 = self.font.render(str(count2), True, 'red')
        self.image.blit(text1, (45, 5))
        self.image.blit(text2, (50, 30))
                