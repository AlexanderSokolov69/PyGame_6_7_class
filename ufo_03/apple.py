import pygame as pg
import random as rnd
from pgbase import PGBase


class Apple(PGBase):
    def create(self):
        speed = 5
        radius = rnd.randint(5, 10)
        scr = pg.image.load('apple.png')
        scr.set_colorkey('white')
        self.dx = 0
        self.dy = -speed
        self.sound = pg.mixer.Sound('Выстрел.wav')
        self.sound.play()
        return scr 