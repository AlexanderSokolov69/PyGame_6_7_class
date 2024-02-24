import pygame as pg
from random import choice

from .const import *


class Ball:
    x = WIDTH // 2
    y = HEIGHT // 2
    dx, dy = choice([(2, 3), (-2, 3)])
    color = colors["pong"]
    size = 30

    def draw(self, scr):
        # pg.draw.rect(scr, self.color, (self.x - self.size // 2,
        #                                self.y - self.size // 2,
        #                                self.size, self.size))
        pg.draw.circle(scr, self.color, (self.x, self.y), self.size // 2)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def test(self, walls):
        coll = walls.test(self)
        if coll in 'RL':
            self.dx *= -1
        elif coll in 'UDC':
            self.dy *= -1


class Walls:
    x0 = 10
    x1 = WIDTH - 10
    y0 = 80
    y1 = HEIGHT - 10
    color = colors['wall']
    width = 8

    def test(self, ball: Ball):
        if self.x0 > ball.x - ball.size // 2:
            return 'L'
        if self.x1 < ball.x + ball.size // 2:
            return 'R'
        if self.y0 > ball.y - ball.size // 2:
            return 'U'
        if self.y1 < ball.y + ball.size // 2:
            return 'D'
        return 'F'

    def draw(self, scr):
        pg.draw.rect(scr, self.color, (self.x0 - self.width, self.y0 - self.width,
                                       self.x1 - self.x0 + self.width * 2,
                                       self.y1 - self.y0 + self.width * 2), self.width)


class Racket:
    x = WIDTH // 2
    y = HEIGHT - 20
    width = 300
    height = 20
    color = colors["racket"]

    def draw(self, scr):
        pg.draw.rect(scr, self.color, (self.x - self.width // 2, self.y - self.height // 2,
                                       self.width, self.height))

    def move(self):
        pass

    def test(self, ball: Ball):
        if ball.dy > 0:
            if self.x - self.width // 2 < ball.x < self.x + self.width // 2 and \
                    ball.y > self.y - self.height // 2:
                return 'C'
        return 'F'
