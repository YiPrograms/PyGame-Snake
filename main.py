#! /usr/bin/env python3

import pygame
pygame.init()

from game import Game

from env import *

def main():
    screen = pygame.display.set_mode((WIDTH*BLOCK_SIZE+1, HEIGHT*BLOCK_SIZE+1))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    game = Game(screen)

    running = True
    while running:
        clock.tick(FPS)

        game.draw_gird()
        game.update()
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    game.snake.dir = 0
                elif e.key == pygame.K_DOWN:
                    game.snake.dir = 1
                elif e.key == pygame.K_DOWN:
                    game.snake.dir = 2
                elif e.key == pygame.K_DOWN:
                    game.snake.dir = 3









if __name__ == "__main__":
    main()