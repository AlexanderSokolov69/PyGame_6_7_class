# Константы проекта
import pygame as pg
import pygame.locals as lc


size = WIDTH, HEIGHT = 800, 600
FPS = 50
colors = {"screen": "blue",
          "pong": "white",
          "racket": "gray"}


pg.init()
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
end_game = False
