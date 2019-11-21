

import pygame

from env import *
from snake import Snake
from random import randint

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.sgroup = pygame.sprite.Group()
        self.snake = Snake(self.sgroup, screen)
        self.new_food()

    def draw_gird(self):
        for i in range(HEIGHT+1):
            pygame.draw.line(self.screen, COLOR_GIRD, (0, i*BLOCK_SIZE), (WIDTH*BLOCK_SIZE, i*BLOCK_SIZE), GIRD_WIDTH)
        for j in range(WIDTH+1):
            pygame.draw.line(self.screen, COLOR_GIRD, (j*BLOCK_SIZE, 0), (j*BLOCK_SIZE, HEIGHT*BLOCK_SIZE), GIRD_WIDTH)

    def draw_back(self):
        self.screen.fill(COLOR_BACK)

    def new_food(self):
        self.food = (randint(0, HEIGHT-1),randint(0, WIDTH-1))
        if self.food in self.snake.body:
            self.new_food()

    def check_die(self):
        if self.snake.head in self.snake.body:
            return True
        if not (0 <= self.snake.head[0] < HEIGHT and 0 <= self.snake.head[1] < WIDTH):
            return True
        return False 

    def draw_food(self):
        pygame.draw.rect(self.screen, COLOR_FOOD, pygame.Rect(self.food[1]*BLOCK_SIZE, self.food[0]*BLOCK_SIZE,
                                                                   BLOCK_SIZE, BLOCK_SIZE))
        

    def update(self):
        if self.snake.head == self.food:
            self.snake.extend = True
            self.new_food()
        if self.check_die():
            del self.snake
            self.snake = Snake(self.sgroup, self.screen)
        self.snake.draw()
        self.draw_food()



