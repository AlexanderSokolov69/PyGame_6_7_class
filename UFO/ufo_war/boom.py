import pygame as pg
from pgbase import PGBase
# 12


LIVE = 3

class Boom(PGBase):
    def create(self):
        self.spisok = []
        self.count = 0
        scr = pg.Surface((60, 60), pg.SRCALPHA, 32)
        scr = pg.image.load('boom3.png')
        scr.set_colorkey('white')
        self.spisok.append(scr)
        scr = pg.Surface((60, 60), pg.SRCALPHA, 32)
        scr = pg.image.load('boom2.png')
        scr.set_colorkey('white')
        self.spisok.append(scr)
        scr = pg.Surface((60, 60), pg.SRCALPHA, 32)
        scr = pg.image.load('boom1.png')
        scr.set_colorkey('white')
        self.spisok.append(scr)
        scr = pg.Surface((60, 60), pg.SRCALPHA, 32)
        scr = pg.image.load('boom0.png')
        scr.set_colorkey('white')
        self.sound = pg.mixer.Sound('vzriv.wav')
        self.sound.play()                    
        return scr

    def draw(self, screen: pg.Surface):
        super().draw(screen)

    def update(self):
        self.count += 1
        if self.count > LIVE:
            if self.spisok:
                self.image = self.spisok.pop()
                self.rect = self.image.get_rect()
                self.count = 0
            else:
                self.kill()
            super().update()