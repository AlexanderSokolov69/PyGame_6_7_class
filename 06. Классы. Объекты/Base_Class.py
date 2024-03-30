#!/usr/bin/env python3
# coding:utf-8
import pygame as pg


class PGObject:
    def __init__(self, place=(100, 100), radius=10):
        self.place = place
        self.radius = radius
        self.image = self.create()
        self.rect = self.image.get_rect()

    def create(self):
        # scr = pg.Surface((200, 200), pg.SRCALPHA, 32)
        # scr = scr.convert_alpha()
        # pg.draw.circle(scr, 'white', (100, 100), self.radius)
        scr = pg.image.load('bird.png')
        scr.convert()
        scr.set_colorkey((150, 150, 150))
        return scr

    def draw(self, screen: pg.Surface):
        x, y = self.place
        width, height = self.rect.size
        screen.blit(self.image, (x - width // 2, y - height // 2))

    def move(self, screen: pg.Surface, dx=0, dy=0):
        # self.radius += 1
        # self.image = self.create()
        # self.rect = self.image.get_rect()
        x, y = self.place
        width, height = screen.get_size()
        if 0 < x < width and 0 < y < height:
            self.place = x + dx, y + dy
