import pygame as pg
from random import choice
from pygame.locals import *
from data.const import *


count = [0]
pong_x = WIDTH // 2
pong_y = HEIGHT // 2
pong_step_x, pong_step_y = choice([(3, 3), (-3, 3), (3, 6), (-3, 6)])
pong_size = 20

racket_w, racket_h = 200, 25
racket_x = (WIDTH - racket_w) // 2
racket_y = HEIGHT - racket_h
racket_step = 3
racket_mv = 0


def result_out(inc=0):
    count[0] += inc
    print(count)


def pong_move():
    global pong_x, pong_y, pong_step_x, pong_step_y
    pong_x += pong_step_x
    pong_y += pong_step_y
    if racket_x < pong_x < racket_x + racket_w and\
        pong_y > HEIGHT - racket_h - pong_size // 2 and\
            pong_step_y > 0:
        result_out(1)
        place = pong_x - racket_x
        if place - 0.25 * racket_w < 0:  # or place + 0.25 * racket_w > racket_w:
            if pong_step_x > 0:
                pong_step_x //= 2
                pong_step_y *= 2
            else:
                pong_step_x *= 2
                pong_step_y //= 2
        if place + 0.25 * racket_w > racket_w:  # or place + 0.25 * racket_w > racket_w:
            if pong_step_x < 0:
                pong_step_x //= 2
                pong_step_y *= 2
            else:
                pong_step_x *= 2
                pong_step_y //= 2
        pong_step_y *= -1
        if pong_step_y > 0:
            pong_step_y = min(3, pong_step_y)
        else:
            pong_step_y = max(-3, pong_step_y)
    if not (0 + pong_size // 2 < pong_x < WIDTH - pong_size // 2):
        pong_step_x *= -1
    if not (0 + pong_size // 2 < pong_y < HEIGHT - pong_size // 2):
        pong_step_y *= -1
        if pong_y >= HEIGHT - pong_size // 2:
            result_out(-1)


def pong_draw():
    pg.draw.rect(screen, colors['pong'], (pong_x - pong_size // 2,
                                          pong_y - pong_size // 2,
                                          pong_size, pong_size))


def racket_move():
    global racket_x, racket_mv
    racket_x += racket_mv


def racket_draw():
    pg.draw.rect(screen, colors['racket'], (racket_x, racket_y, racket_w, racket_h))


while not end_game:
    for event in pg.event.get():
        if event.type == QUIT:
            end_game = True
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                racket_mv -= racket_step
            elif event.key == K_RIGHT:
                racket_mv += racket_step
            elif event.key == K_SPACE:
                racket_mv = 0

    pong_move()
    racket_move()
    screen.fill(colors['screen'])
    pong_draw()
    racket_draw()
    pg.display.flip()
    clock.tick(FPS)
pg.quit()
