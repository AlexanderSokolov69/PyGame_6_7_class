from pgbase import PGBase
import pygame as pg
import random as rnd


class UFO(PGBase):
    TEMPO = 0.01
    
    def __init__(self):
        super().__init__(0, rnd.randint(50, 200), rnd.randint(1, 5))
        self.change_move(1, 0)

    def create(self):
        scr = pg.Surface((120, 80), pg.SRCALPHA, 32)
        pg.draw.rect(scr, 'yellow', (40, 0, 40, 40))
        pg.draw.ellipse(scr, 'red', (0, 20, 120, 60))
        pg.draw.rect(scr, 'green', (50, 50, 20, 30))
        return scr

    def shot(self):
        return UFO.TEMPO > rnd.random()

