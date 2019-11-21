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

    RUN_EVENT = pygame.USEREVENT+1
    pygame.time.set_timer(RUN_EVENT, RUN_TICK)

    running = True
    while running:
        clock.tick(FPS)

        game.draw_back()
        game.update()
        

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                quit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    game.snake.set_dir(0)
                elif e.key == pygame.K_RIGHT:
                    game.snake.set_dir(1)
                elif e.key == pygame.K_DOWN:
                    game.snake.set_dir(2)
                elif e.key == pygame.K_LEFT:
                    game.snake.set_dir(3)
                elif e.key == pygame.K_SPACE:
                    game.snake.extend = True
            elif e.type == RUN_EVENT:
                game.snake.forward()
            
        game.draw_gird()
        pygame.display.flip()










if __name__ == "__main__":
    main()