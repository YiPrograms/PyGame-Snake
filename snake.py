
import pygame
from random import randint
from collections import deque

from env import *

class Snake(pygame.sprite.Sprite):
    def __init__(self, sgroup, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.length = 2
        self.head = (randint(1, HEIGHT-2), randint(1, WIDTH-2))
        self.dir = DIR[randint(0, 4)]
        self.blocks = deque([self.head, self.get_next_pos((self.dir[0]*-1, self.dir[1]*-1))])

    def get_next_pos(self, d):
        return (self.head[0]+d[0], self.head[1]+d[1])

    def draw(self):
        for blk in self.blocks:
            pygame.draw.rect(self.screen, COLOR_SNAKE, pygame.Rect(blk[1]*BLOCK_SIZE, blk[0]*BLOCK_SIZE,
                                                                   BLOCK_SIZE, BLOCK_SIZE))

    def update(self):
        pass