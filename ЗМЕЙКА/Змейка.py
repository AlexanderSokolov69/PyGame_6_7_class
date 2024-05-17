#!/usr/bin/env python3
# coding:utf-8
import pygame as pg


SIZE = 30
STEP = 4
WIDTH, HEIGHT = 800, 600


class Segment(pg.sprite.Sprite):
    def __init__(self, x=0, y=0, *groups):
        super().__init__(*groups)
        self.image = pg.surface.Surface((SIZE, SIZE))
        pg.draw.rect(self.image, 'green', (0, 0, SIZE, SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.arrow = 0

    def __call__(self, dx=0, dy=0):
        self.rect.move(dx, dy)

    def set_arrow(self, arrow):
        self.arrow = arrow

    def update(self):
        if self.arrow == pg.K_LEFT:
            self.rect.x -= STEP
        elif self.arrow == pg.K_RIGHT:
            self.rect.x += STEP
        elif self.arrow == pg.K_UP:
            self.rect.y -= STEP
        elif self.arrow == pg.K_DOWN:
            self.rect.y += STEP


pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))

togame = True

all_sprites = pg.sprite.Group()
snake = Segment(20, 20, all_sprites)
while togame:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            togame = False
        elif event.type == pg.KEYDOWN:
            if event.key in (pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_SPACE):
                snake.set_arrow(event.key)

    screen.fill('black')

    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.flip()
    clock.tick(40)

pg.quit()

