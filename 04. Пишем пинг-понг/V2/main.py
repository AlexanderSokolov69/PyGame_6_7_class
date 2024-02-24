import pygame as pg
import pygame.locals as lc

from data.const import *
from data.classes import *

pg.init()
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
end_game = False
pong = Ball()
wall = Walls()
racket = Racket()
while not end_game:
    for event in pg.event.get():
        if event.type == lc.QUIT:
            end_game = True

    racket.move()
    pong.move()
    pong.test(racket)  # Двигаем мяч
    pong.test(wall)  # Двигаем мяч

    screen.fill(colors["screen"])
    pong.draw(screen)  # Рисуем мяч
    wall.draw(screen)  # Рисуем стены
    racket.draw(screen)
    pg.display.flip()
    clock.tick(FPS)

pg.quit()