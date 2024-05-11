import pygame as pg
import random as rnd
from pgbase import PGBase


class Goroh(PGBase):
    def create(self):
        speed = rnd.randint(1, 6)
        radius = rnd.randint(5, 10)
        scr = pg.Surface((20, 20), pg.SRCALPHA, 32)
        pg.draw.circle(scr, 'green', (10, 10), radius)
        self.dx = 0
        self.dy = speed
        return scr