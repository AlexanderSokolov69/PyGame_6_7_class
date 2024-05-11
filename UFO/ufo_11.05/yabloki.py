import pygame as pg
from pgbase import PGBase


class Apple(PGBase):
    def create(self):
        speed = 5
        scr = pg.image.load('apple.png')
        scr.set_colorkey('white')
        self.dx = 0
        self.dy = -speed
        self.sound = pg.mixer.Sound('kidaet.wav')
        self.sound.play()
        return scr

    def move(self):
        super().move()
        if self.y < 0:
            self.kill()    