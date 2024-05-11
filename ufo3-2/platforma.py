from pgbase import PGBase
import pygame as pg
from const import *


class Platforma(PGBase):
    def __init__(self, *groups):
        super().__init__(WIDTH // 2, HEIGHT - 30, 10, *groups)
        
    def create(self):
        scr = pg.image.load('platforma.png')
        scr.set_colorkey('white')
        return scr
    
    def move(self):
        '''вычисление координат x, y'''
        test = self.x + self.dx
        if 0 < test < WIDTH:
            super().move()
