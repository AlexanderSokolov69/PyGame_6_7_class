import pygame as pg
import math


class PGBase:
    def __init__(self, x=100, y=100, speed=10):
        self.x = x
        self.y = y
        self.speed = speed
        self.dx = 0
        self.dy = 0
        self.perc = 25
        self.image = self.create()
        self.rect = self.image.get_rect()

    def animate(self):
        self.image = self.create()
        self.rect = self.image.get_rect()

    def create(self):
        scr = pg.Surface((100, 100), pg.SRCALPHA, 32)
        # pg.draw.circle(scr, 'red', (50, 50), 50)
        # pg.draw.circle(scr, 'white', (50, 50), 40)
        # pg.draw.circle(scr, 'yellow', (50, 50), 30)
        angle = self.perc * 2 * math.pi / 100
        pg.draw.arc(scr, 'red', (0, 0, 100, 100), 0, angle, 50)
        return scr

    def check_list(self, rects: list[pg.Rect]):
        return self.rect.collidelist(rects)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.perc = (self.perc + 1) % 100
        self.animate()

    def draw(self, screen: pg.Surface):
        screen.blit(self.image, (self.x - self.rect.width // 2,
                                 self.y - self.rect.height // 2))

    def change_move(self, dx, dy):
        self.dx = self.speed * dx
        self.dy = self.speed * dy

    def set_speed(self, speed):
        self.dx = speed * self.dx / self.speed
        self.dy = speed * self.dy / self.speed
        self.speed = speed

    def get_pos(self):
        return self.x, self.y
