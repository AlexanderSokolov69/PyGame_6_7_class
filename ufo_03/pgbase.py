import pygame as pg


class PGBase:
    def __init__(self, x=100, y=100, speed=10):
        '''координаты x,y и скорость (speed)'''
        self.x = x
        self.y = y
        self.speed = speed
        self.dx = 0
        self.dy = 0
        self.image = self.create()
        self.rect = self.image.get_rect()

    def create(self):
        '''создание изображения спрайта'''
        scr = pg.Surface((100, 100), pg.SRCALPHA, 32)
        pg.draw.circle(scr, 'red', (50, 50), 50)
        pg.draw.circle(scr, 'white', (50, 50), 30)
        pg.draw.rect(scr, 'yellow', (25, 25, 50, 50))
        return scr

    def move(self):
        '''вычисление координат x, y'''
        self.x += self.dx
        self.y += self.dy
    
    def draw(self, screen: pg.Surface):
        '''перенос изображения на экран (screen)'''
        screen.blit(self.image, (self.x - self.rect.width // 2,
                                 self.y - self.rect.height // 2))

    def change_move(self, dx, dy):
        '''изменение направления движения (dx, dy)'''
        self.dx = self.speed * dx
        self.dy = self.speed * dy

    def set_speed(self, speed):
        '''установка скорости (speed)'''
        self.dx = speed * self.dx / self.speed
        self.dy = speed * self.dy / self.speed
        self.speed = speed

    def get_pos(self):
        '''возращение координат обьекта (x, y)'''
        return self.x, self.y