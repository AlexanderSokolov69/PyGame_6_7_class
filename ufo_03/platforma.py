from pgbase import PGBase
import pygame as pg
from const import *


class Platforma(PGBase):
    def __init__(self):
        super().__init__(WIDTH // 2, HEIGHT - 10)
        
    def create(self):
        scr = pg.Surface((120, 80), pg.SRCALPHA, 32)
        pg.draw.rect(scr, 'yellow', (40, 0, 40, 40))
        pg.draw.ellipse(scr, 'red', (0, 20, 120, 60))
        pg.draw.rect(scr, 'green', (50, 50, 20, 30))
        return scr
        