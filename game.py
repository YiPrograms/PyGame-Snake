

import pygame

from env import *
from snake import Snake


class Game():
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.food_pos = (-1, -1)
        self.sgroup = pygame.sprite.Group()
        self.snake = Snake(self.sgroup, screen)

    def draw_gird(self):
        self.screen.fill(COLOR_BACK)
        for i in range(HEIGHT+1):
            pygame.draw.line(self.screen, COLOR_GIRD, (0, i*BLOCK_SIZE), (WIDTH*BLOCK_SIZE, i*BLOCK_SIZE), GIRD_WIDTH)
        for j in range(WIDTH+1):
            pygame.draw.line(self.screen, COLOR_GIRD, (j*BLOCK_SIZE, 0), (j*BLOCK_SIZE, HEIGHT*BLOCK_SIZE), GIRD_WIDTH)

    def update(self):
        self.snake.draw()



