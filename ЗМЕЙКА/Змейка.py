#!/usr/bin/env python3
# coding:utf-8
from math import copysign
import pygame as pg


SIZE = 30
STEP = 4
WIDTH, HEIGHT = 800, 600


class Head(pg.sprite.Sprite):
    def __init__(self, x=0, y=0, *groups):
        super().__init__(*groups)
        self.image = pg.surface.Surface((SIZE, SIZE))
        pg.draw.rect(self.image, 'green', (0, 0, SIZE, SIZE))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = 0
        self.dy = 0
        self.queue = []

    def __call__(self, x=0, y=0):
        self.rect.x = x
        self.rect.y = y

    def set_arrow(self, arrow):
        self.arrow = arrow

    def update(self):
        dx, dy = self.dx, self.dy
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            dx, dy = -STEP, 0
        elif key[pg.K_RIGHT]:
            dx, dy = STEP, 0
        elif key[pg.K_UP]:
            dx, dy = 0, -STEP
        elif key[pg.K_DOWN]:
            dx, dy = 0, STEP
        elif key[pg.K_SPACE]:
            dx, dy = 0, 0
        if (dx, dy) != (self.dx, self.dy):
            self.queue.insert(0, (self.rect.x, self.rect.y))
        self.dx, self.dy = dx, dy
        self.rect.move_ip(self.dx, self.dy)
        self.rect.x = self.rect.x % WIDTH
        self.rect.y = self.rect.y % HEIGHT

    def get_pos(self, x, y):
        print(x, y, self.queue)
        if self.queue:
            if self.queue[-1] == (x, y):
                self.queue.pop()
            if self.queue:
                return self.queue[-1]
        return self.rect.x, self.rect.y



class Segment(pg.sprite.Sprite):
    def __init__(self, head: Head, *groups):
        super().__init__(*groups)
        self.image = pg.surface.Surface((SIZE, SIZE))
        pg.draw.rect(self.image, 'darkgreen', (0, 0, SIZE, SIZE))
        self.rect = self.image.get_rect()
        self.head = head
        self.rect.x, self.rect.y = self.head.get_pos(0, 0)

    def update(self):
        x0, y0 = self.head.get_pos(self.rect.x, self.rect.y)
        dx = x0 - self.rect.x
        dy = y0 - self.rect.y
        lx = abs(dx)
        ly = abs(dy)
        dx = copysign(max(1, lx - SIZE), dx)
        dy = copysign(max(1, ly - SIZE), dy)
        self.rect.move_ip(dx, dy)

    def get_pos(self):
        return self.rect.x, self.rect.y


pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))

togame = True
all_sprites = pg.sprite.Group()
head = Head(WIDTH // 2 - SIZE // 2, HEIGHT // 2 - SIZE // 2, all_sprites)
snake = []
while togame:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            togame = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                if snake:
                    snake.append(Segment(snake[-1], all_sprites))
                else:
                    snake.append(Segment(head, all_sprites))

    screen.fill('black')
    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.flip()
    clock.tick(5)

pg.quit()
