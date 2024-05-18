import pygame as pg
from pgbase import PGBase
from const import *


class Field(PGBase):
    def __init__(self, x=0, y=0, width=WIDTH, height=HEIGHT, color='green', *args):
        self.width = width
        self.height = height
        self.color = color
        super().__init__(x, y, 0, *args)
    
    def create(self):
        scr = pg.Surface((self.width, self.height), pg.SRCALPHA, 32)
        pg.draw.rect(scr, self.color, (0, 0, self.width, self.height))
        return scr
