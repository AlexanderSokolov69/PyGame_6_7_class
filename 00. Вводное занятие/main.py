import pygame as pg


FPS = 50
end_game = False
size = width, height = 300, 600
pg.init()
clock = pg.Clock()
screen = pg.display.set_mode(size)

x = 50
y = 50
dx = 0
dy = 0
k_width = 200
k_height = 200

while not end_game:
    # Анализ управления =================================
    for event in pg.event.get():
        # print(event)
        if event.type == pg.QUIT:
            end_game = True
        elif event.type == pg.MOUSEMOTION:
            pg.display.set_caption(str(event.pos))
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                dy = 1
            elif event.key == pg.K_UP:
                dy = -1
            elif event.key == pg.K_LEFT:
                dx = -1
            elif event.key == pg.K_RIGHT:
                dx = 1
        elif event.type == pg.KEYUP:
            if event.key == pg.K_DOWN:
                dy = 0
            elif event.key == pg.K_UP:
                dy = 0
            elif event.key == pg.K_LEFT:
                dx = 0
            elif event.key == pg.K_RIGHT:
                dx = 0

    # Расчёты ===========================================
    x += dx
    if x > width:
        x = -k_width
    elif x < -k_width:
        x = width
    y += dy
    if y > height:
        y = -k_height
    elif y < -k_height:
        y = height

    # Отрисовка =========================================
    screen.fill('pink')
    pg.draw.ellipse(screen, 'green', (x, y, k_width, k_height))
    pg.draw.rect(screen, 'red', (x, y, k_width // 2, k_height // 2), 4)


    pg.display.update()
    # Пауза==============================================
    clock.tick(FPS)

pg.quit()