import pygame as pg
import pygame.locals as lc
from random import choice, random
from math import sin, cos

from .const import *


class Ball:
    pg.font.init()

    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        angle = random() * 3.14 * 2
        self.dx, self.dy = 4 * sin(angle), 4 * cos(angle)
        if abs(self.dx) > abs(self.dy):
            self.dx, self.dy = self.dy, self.dx
        self.color = colors["pong"]
        self.size = 30
        self.score = [0, 0]
        self.my_font = pg.font.SysFont('Comic Sans MS', 30)
        self.text_coord = (WIDTH // 2, 10)
        self.level = 1

    def draw(self, scr):
        # pg.draw.rect(scr, self.color, (self.x - self.size // 2,
        #                                self.y - self.size // 2,
        #                                self.size, self.size))
        pg.draw.circle(scr, self.color, (self.x, self.y), self.size // 2)
        out = self.my_font.render(f"{self.score[0]}:{self.score[1]}", True, colors["score"])
        w = out.get_width()
        scr.blit(out, (self.text_coord[0] - w // 2, self.text_coord[1]))

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.score[1] > self.level * 10:
            self.level += 1
            self.dx *= 1.5
            self.dy *= 1.5

    def test(self, walls):
        coll = walls.test(self)
        if coll in 'RL':
            self.dx *= -1
        elif coll in 'UDC':
            if coll == 'D':
                self.score[0] += 1
            elif coll == 'C':
                self.score[1] += 1
            self.dy *= -1


class Walls:
    x0 = 10
    x1 = WIDTH - 10
    y0 = 80
    y1 = HEIGHT - 25
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
    y = HEIGHT - 40
    dx = 0
    speed = 6
    width = 100
    height = 2
    color = colors["racket"]

    def draw(self, scr):
        if any([self.x > WIDTH and self.dx > 0, self.x < 0 and self.dx < 0]):
            self.dx *= -1
        self.x += self.dx
        pg.draw.rect(scr, self.color, (self.x - self.width // 2, self.y - self.height // 2,
                                       self.width, self.height))

    def move(self, event):
        if event.key == lc.K_SPACE:
            self.dx = 0
        elif event.key == lc.K_LEFT:
            self.dx -= self.speed
        elif event.key == lc.K_RIGHT:
            self.dx += self.speed

    def test(self, ball: Ball):
        if ball.dy > 0:
            if (self.x - self.width // 2 < ball.x < self.x + self.width // 2) and \
                    ball.y + ball.size // 2 > self.y - self.height // 2:
                return 'C'
        return 'F'
