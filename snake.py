
import pygame
from random import randint
from collections import deque

from env import *

class Snake(pygame.sprite.Sprite):
    def __init__(self, sgroup, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.length = 2
        self.head = (randint(HEIGHT*1//3, HEIGHT*2//3), randint(WIDTH*1//3, WIDTH*2//3))
        self.dir = randint(0, 3)
        self.body = deque()
        self.body.append(self.head)
        self.head = self.get_next_pos(DIR[self.dir])
        self.extend = False

    def get_next_pos(self, d):
        return (self.head[0]+d[0], self.head[1]+d[1])

    def draw(self):
        for blk in self.body:
            pygame.draw.rect(self.screen, COLOR_SNAKE, pygame.Rect(blk[1]*BLOCK_SIZE, blk[0]*BLOCK_SIZE,
                                                                   BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.screen, COLOR_SNAKE, pygame.Rect(self.head[1]*BLOCK_SIZE, self.head[0]*BLOCK_SIZE,
                                                                   BLOCK_SIZE, BLOCK_SIZE))

    def update(self):
        pass

    def forward(self):
        self.body.appendleft(self.head)
        self.head = self.get_next_pos(DIR[self.dir])
        if self.extend:
            self.extend = False
        else:
            self.body.pop()
    
    def set_dir(self, d):
        if self.dir&1 != d&1:
            self.dir = d