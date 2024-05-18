import pygame as pg
from const import *
from field import Field

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

end_game = False
s_level0 = pg.sprite.Group()

field = Field(WIDTH // 2, HEIGHT // 2, WIDTH, HEIGHT, 'darkgreen', s_level0)
field_u = Field(WIDTH // 2, 0 + BORT // 2, WIDTH, BORT, 'yellow', s_level0)
field_d = Field(WIDTH // 2, HEIGHT - BORT // 2, WIDTH, BORT, 'yellow', s_level0)
field_l = Field(BORT // 2, HEIGHT // 2, BORT, HEIGHT, 'yellow', s_level0)
field_r = Field(WIDTH - BORT // 2, HEIGHT // 2, BORT, HEIGHT, 'yellow', s_level0)

while not end_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end_game = True

    s_level0.update()
    screen.fill('black')
    s_level0.draw(screen)
    clock.tick(FPS)
    pg.display.flip()

pg.quit()
