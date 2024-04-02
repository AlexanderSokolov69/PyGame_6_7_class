import pygame as pg


class Hero:
    test = 10
    def __init__(self):
        self.surface = pg.Surface((100, 100), pg.SRCALPHA, 32)
        self.surface.convert_alpha()
        pg.draw.polygon(self.surface, 'yellow', ((50, 0), (100, 100), (0, 100)))
        pg.draw.circle(self.surface, 'red', (50, 50), 40)
        pg.draw.circle(self.surface, 'black', (50, 50), 10)
        self.angle = 0
        self.out_surf = pg.transform.rotate(self.surface, self.angle)
        self.rect = self.out_surf.get_rect()

    def set_angle(self, angle):
        self.angle = angle
        self.out_surf = pg.transform.rotate(self.surface, self.angle)

    def draw(self, screen: pg.Surface):
        width = self.out_surf.get_width()
        shift = (width - 100) // 2
        screen.blit(self.out_surf, (100 - shift, 100 - shift))
