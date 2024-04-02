import pygame as pg
from hero import Hero


FPS = 50  # Скорость обновления экрана
end_game = False  # Флаг окончания игры

size = width, height = 800, 600  # Размер поля игры

i = 0
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode(size)
hero = Hero()
while not end_game:
    # Анализ управления =======================================
    for event in pg.event.get():
        # print(event)
        if event.type == pg.QUIT:
            end_game = True

    # Расчёты ===============================================
    i += 1
    hero.set_angle(i)
    # Отрисовка ===============================================
    pg.display.set_caption(
        f'{FPS}')
    screen.fill('brown')
    hero.draw(screen)
    pg.display.flip()
    # Пауза ===================================================
    clock.tick(FPS)

end_game = False
pg.quit()
