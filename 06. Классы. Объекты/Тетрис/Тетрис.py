#!/usr/bin/env python3
# coding:utf-8
import random
import sys
from copy import deepcopy

import pygame
from pygame.locals import *


FPS = 40
CELL_SIZE = 32
TILE_TYPES = [(pygame.image.load('I.png'), 'I'),
              (pygame.image.load('J.png'), 'J'),
              (pygame.image.load('L.png'), 'L')
              ]


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((CELL_SIZE * 10, CELL_SIZE * 20))
        pygame.display.set_caption("Тетрис")
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        # Создание и добавление тетримино
        self.__create_and_add_tetrominos()

    def run(self):
        while True:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == QUIT:
                    sys.exit()
            self.__update_screen()
            pygame.display.flip()
            self.clock.tick(FPS)

    def __create_and_add_tetrominos(self):
        tetromino_list = TILE_TYPES  # list(map(deepcopy, [TILE_TYPES]))
        random.shuffle(tetromino_list)
        for shape, image in TILE_TYPES:
            position = [shape[i] for i in range(len(shape))]
            new_sprite = Tetromino(image, position)
            self.all_sprites.add(new_sprite)

    def __update_screen(self):
        clear_space_y = 0

        if self.all_sprites:
            for sprite in self.all_sprites:
                pos = sprite.rect.topleft
                if pos[1] > clear_space_y:
                    clear_space_y = pos[1]

                # Если тетримино касается нижней части экрана
                if pos[1] + sprite.height > CELL_SIZE * 20:
                    self.__clear_line(clear_space_y - pos[1])
                    break

                # Если все линии очищены, перемещаем все тетримино вниз
                if all([row == 0 for row in clear_space_y]):
                    for sprite in reversed(self.all_sprites):
                        sprite.rect.y += 1
                        if sprite.is_clear:
                            # Если новое положение тетримино является чистым
                            if pygame.sprite.collide_rect(sprite, sprite):
                                sprite.rect.x = random.randint(0, self.screen.get_width() // 5)
                                # Если тетримино находится в нижней части экрана, оно сбрасывается
                                if sprite.rect.bottom >= self.screen.get_height():
                                    sprite.change_direction()

                # Сбрасываем тетримино если оно касается верхней части
                elif clear_space_y < 4 * CELL_SIZE:
                    self.__reset_tetrominoes()

            # Отображаем все тетримино и фон на экране
            for sprite in sorted(self.all_sprites, key=lambda x: x.rect.topleft):
                self.screen.blit(sprite.image, sprite.rect)
            pygame.draw.rect(self.screen, (0, 0, 0), (0, clear_space_y, self.screen.get_width(), CELL_SIZE))

    # Функция для очистки одной линии
    def __clear_line(self, y):
        global clear_space_y
        clear_space_y -= y
        if clear_space_y <= 0:
            clear_space_y = 0
        return clear_space_y


    # Функция для сброса всех тетримино
    def __reset_tetrominoes(self):
        for sprite in self.all_sprites[:]:
            sprite.reset()
            if not sprite.is_on_ground():
                sprite.change_direction()
                break


class Tetromino:
    def __init__(self, image, position):
        self.image = image
        self.position = position
        self.rect = self.image.get_rect()


    def reset(self):
        self.direction = "down"
        self.is_clear = True
        self.update_position()


    def change_direction(self):
        direction = {
            "down": "up",
            "up": "down",
            "left": "right",
            "right": "left",
        }
        self.direction = direction[self.direction]
        self.is_clear = False


    def update_position(self):
        if self.direction == "down":
            self.rect.centerx = random.randint(-5, 5) * CELL_SIZE
            self.rect.centery += 5 * CELL_SIZE
        elif self.direction == "up":
            self.rect.centerx = random.randint(-5, 5) * CELL_SIZE
            self.rect.centery -= 5 * CELL_SIZE
        else:
            self.rect.centery = random.randint(-5, 5) * CELL_SIZE + 5
        if self.direction == "right":
            self.rect.right = self.screen.get_width()
        else:
            self.rect.left = 0
    def is_on_ground(self):
        return self.rect.top >= 0


if __name__ == "__main__":
    game = Game()
    game.run()
