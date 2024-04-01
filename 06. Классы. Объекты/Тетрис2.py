#!/usr/bin/env python3
# coding:utf-8
from random import choice
from copy import deepcopy
import pygame as pg
import pygame.locals as lc
from PIL import Image


def load_pic(pic):
    im = Image.open(pic)
    im = im.resize((SIZE, SIZE))
    im.save('__tmp.png')
    return pg.image.load('__tmp.png')


F_WIDTH = 10
F_HEIGHT = 15
SIZE = 50
BRICK_TYPE = [
    (load_pic('L.png'),
     [
         [(0, -1), (0, 0), (0, 1), (1, 1)],
         [(-1, 1), (-1, 0), (0, 0), (1, 0)],
         [(-1, -1), (0, -1), (0, 0), (0, 1)],
         [(-1, 0), (0, 0), (1, 0), (1, -1)]
     ]),
    (load_pic('i.png'),
     [
         [(-1, 1), (0, 1), (0, 0), (0, -1)],
         [(-1, -1), (-1, 0), (0, 0), (1, 0)],
         [(1, -1), (0, -1), (0, 0), (0, 1)],
         [(-1, 0), (0, 0), (1, 0), (1, 1)]
     ]),
    (load_pic('C.png'),
     [
         [(-1, -1), (0, -1), (-1, 0), (0, 0)],
         [(-1, -1), (0, -1), (-1, 0), (0, 0)],
         [(-1, -1), (0, -1), (-1, 0), (0, 0)],
         [(-1, -1), (0, -1), (-1, 0), (0, 0)]
     ]),
    (load_pic('T.png'),
     [
         [(-1, 0), (0, 0), (1, 0), (0, -1)],
         [(0, -1), (0, 0), (0, 1), (1, 0)],
         [(-1, 0), (0, 0), (1, 0), (0, 1)],
         [(-1, 0), (0, 0), (0, -1), (0, 1)]
     ]),
    (load_pic('J.png'),
     [
         [(0, -2), (0, -1), (0, 0), (0, 1)],
         [(-1, 0), (0, 0), (1, 0), (2, 0)],
         [(0, -2), (0, -1), (0, 0), (0, 1)],
         [(-1, 0), (0, 0), (1, 0), (2, 0)]
     ])

]


class Brick:
    def __init__(self):
        brick = choice(BRICK_TYPE)
        self.x = F_WIDTH // 2
        self.y = 2
        self.state = 0
        self.image = brick[0]
        self.body = deepcopy(brick[1])
        self.rect = self.image.get_rect()
        self.center = self.rect.center

    def draw(self, scr):
        for x, y in self.body[self.state]:
            scr.blit(self.image, ((self.x + x) * SIZE, (self.y + y) * SIZE))

    def rotate(self, data: set, side=1):
        old_state = self.state
        self.state = (self.state + side) % 4
        if self.test_shift(data):
            return self.get_min_max()
        self.state = old_state
        return 0, 0

    def down(self):
        if self.y + max([c[1] for c in self.body[self.state]]) <= F_HEIGHT:
            self.y += 1
        else:
            return True

    def slide(self, data, dx=0):
        if self.test_shift(data, dx=dx):
            self.x += dx

    def get_area(self):
        return [(x + self.x, y + self.y) for x, y in self.body[self.state]]

    def test_shift(self, data: set, dx=0, dy=0):
        for x, y in self.get_area():
            if (x + dx, y + dy) in data:
                return False
        return True

    def get_min_max(self):
        x_pos = [x for x, y in self.get_area()]
        return min(x_pos), max(x_pos)

    def get_min_max_y(self):
        y_pos = [y for x, y in self.get_area()]
        return min(y_pos), max(y_pos)


class Bricks:
    def __init__(self):
        self.data = set()
        self.image = None

    def add(self, brick: Brick):
        self.image = brick.image
        for pos in brick.get_area():
            self.data.add(pos)

    def draw(self, scr):
        for x, y in self.data:
            scr.blit(self.image, ((x) * SIZE, (y) * SIZE))

    def get_data(self):
        return self.data

    def check_lines(self):
        ok = []
        for y in range(F_HEIGHT + 2):
            for x in range(F_WIDTH):
                if (x, y) not in self.data:
                    break
            else:
                ok.append(y)
        return ok

    def remove_lines(self, lines):
        counter = 0
        for y in lines:
            for x in range(F_WIDTH):
                self.data.remove((x, y))
                counter += 1
        for row in lines:
            new_data = set()
            for x, y in self.data:
                if y < row:
                    y += 1
                new_data.add((x, y))
            self.data = new_data
        return counter

def run():
    clock = pg.time.Clock()
    FPS = 30
    time_step = 0.5
    score = 0
    screen = pg.display.set_mode((F_WIDTH * SIZE, (F_HEIGHT + 2) * SIZE))
    stop_game = False
    obj_moved = Brick()
    obj_static = Bricks()
    step_count = 0
    while not stop_game:
        pg.display.set_caption(f"Счет: {score}")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                stop_game = True
            elif event.type == lc.KEYDOWN:
                if event.key == lc.K_DOWN:
                    step_count += FPS * time_step
                elif event.key == lc.K_UP:
                    xl, xr = obj_moved.rotate(obj_static.get_data())
                    if xl < 0 or xr >= F_WIDTH:
                        obj_moved.rotate(obj_static.get_data(), -1)
                elif event.key == lc.K_LEFT and obj_moved.get_min_max()[0] > 0:
                    obj_moved.slide(obj_static.get_data(), -1)
                elif event.key == lc.K_RIGHT and obj_moved.get_min_max()[1] < F_WIDTH - 1:
                    obj_moved.slide(obj_static.get_data(), 1)

        if step_count > FPS * time_step:
            if obj_moved.test_shift(obj_static.get_data(), dy=1) and obj_moved.get_min_max_y()[1] < F_HEIGHT + 1:
                obj_moved.down()
            else:
                obj_static.add(obj_moved)
                obj_moved = Brick()
                if not obj_moved.test_shift(obj_static.get_data()):
                    stop_game = True
            step_count = 0
            count = obj_static.remove_lines(obj_static.check_lines())
            score += F_WIDTH * 16 * (count // (4 * F_WIDTH)) + count % (4 * F_WIDTH)

        screen.fill('black')
        obj_moved.draw(screen)
        obj_static.draw(screen)
        pg.display.flip()
        clock.tick(FPS)
        step_count += 1


if __name__ == "__main__":
    pg.init()
    run()
    stop_game = False

    while not stop_game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                stop_game = True
    pg.quit()
