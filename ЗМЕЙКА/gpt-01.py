#!/usr/bin/env python3
# coding:utf-8
import pygame
import random

pygame.init()

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Размеры экрана
width = 800
height = 600

# Размер клетки
block_size = 20

# Инициализация окна игры
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)


# Класс спрайта для змейки
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((block_size, block_size))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.speed_x = 0
        self.speed_y = 0

        self.snake_list = []
        self.snake_length = 1

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        self.snake_list.append([self.rect.x, self.rect.y])
        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]

        for segment in self.snake_list[:-1]:
            if segment == [self.rect.x, self.rect.y]:
                game_exit = True


# Класс спрайта для еды
class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((block_size, block_size))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, width - block_size)
        self.rect.y = random.randrange(0, height - block_size)


# Группы спрайтов
all_sprites = pygame.sprite.Group()
snake_group = pygame.sprite.Group()
food_group = pygame.sprite.Group()

player = Snake()
all_sprites.add(player)
snake_group.add(player)

food = Food()
all_sprites.add(food)
food_group.add(food)


# Главная функция игры
def gameLoop():
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speed_x = -block_size
                    player.speed_y = 0
                elif event.key == pygame.K_RIGHT:
                    player.speed_x = block_size
                    player.speed_y = 0
                elif event.key == pygame.K_UP:
                    player.speed_y = -block_size
                    player.speed_x = 0
                elif event.key == pygame.K_DOWN:
                    player.speed_y = block_size
                    player.speed_x = 0

        hits = pygame.sprite.spritecollide(player, food_group, True)
        if hits:
            player.snake_length += 1
            food = Food()
            all_sprites.add(food)
            food_group.add(food)

        all_sprites.update()

        game_display.fill(white)

        for segment in player.snake_list:
            pygame.draw.rect(game_display, green, [segment[0], segment[1], block_size, block_size])

        all_sprites.draw(game_display)

        pygame.display.update()

        clock.tick(15)

    pygame.quit()
    quit()


gameLoop()
