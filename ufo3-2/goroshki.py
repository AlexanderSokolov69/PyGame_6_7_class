import pygame as pg
import random as rnd
from pgbase import PGBase
from const import *


class Goroh(PGBase):
    def create(self):
        speed = rnd.randint(1, 6)
        radius = rnd.randint(5, 10)
        scr = pg.Surface((20, 20), pg.SRCALPHA, 32)
        scr = pg.image.load('goroh.png')
        scr.set_colorkey('white')
        self.dx = 0
        self.dy = speed
        self.sound = pg.mixer.Sound('vistrel.wav')
        self.sound.play()
        return scr
    
    def move(self):
        super().move()
        if self.y > HEIGHT:
            self.kill()

