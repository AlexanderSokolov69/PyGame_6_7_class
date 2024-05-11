import pygame as pg
import random as rnd
from const import *
from pgbase import PGBase


class Final(PGBase):
    def __init__(self, *groups):
        super().__init__(WIDTH, HEIGHT // 2, 10, *groups)
        self.font = pg.font.Font(None, 80)

    def create(self):
        scr = pg.image.load('final.png')
        scr.set_colorkey('white')
        return scr

    def write(self, count):
        self.image = self.create()
        text = self.font.render(str(count), True, 'red')
        self.image.blit(text, (200, 120))
        self.rect.x = WIDTH // 4
        self.rect.y = HEIGHT // 4
  