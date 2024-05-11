from pgbase import PGBase
import pygame as pg
import random as rnd
from const import *


class UFO(PGBase):
    TEMPO = 0.01
    
    def __init__(self, *groups):
        super().__init__(0, rnd.randint(50, 200), rnd.randint(1, 5), *groups)
        self.change_move(1, 0)

    def create(self):
        scr = pg.image.load('ufo.png')
        scr.set_colorkey('white')
        self.sound = pg.mixer.Sound('ufo.wav')
        self.sound.play()
        return scr

    def shot(self):
        return UFO.TEMPO > rnd.random()

    def move(self):
        super().move()
        if self.x > WIDTH:
            self.kill()

