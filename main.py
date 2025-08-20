
import pygame as pg
import math
import random

from snake import Snake
from apple import Apple
from constants import *


def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Snake")
    clock = pg.time.Clock()
    #dt = 0

    drawable = pg.sprite.Group()
    updatable = pg.sprite.Group()
    Snake.containers = drawable, updatable
    Apple.containers = drawable

    snake = Snake(START_POS, SIZE_SNAKE, START_LENGTH, COLOR_SNAKE)
    pos = (random.randint(0, BOARD_SIZE[0] - 1), random.randint(0, BOARD_SIZE[1] - 1))
    while snake.pos == pos or snake.collision(pos):
        pos = (random.randint(0, BOARD_SIZE[0] - 1), random.randint(0, BOARD_SIZE[1] - 1))
    apple = Apple(pos, SIZE_APPLE, COLOR_APPLE)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        screen.fill((0, 0, 0))  # Fill the screen with black
        for i in range(BOARD_SIZE[0] + 1):
            pg.draw.line(screen, (100, 100, 100), (0, i * (SIZE_SQUARE + 1)), (SCREEN_WIDTH, i * (SIZE_SQUARE + 1)))
        for i in range(BOARD_SIZE[1] + 1):
            pg.draw.line(screen, (100, 100, 100), (i * (SIZE_SQUARE + 1), 0), (i * (SIZE_SQUARE + 1), SCREEN_HEIGHT))

        updatable.update()
        
        if snake.collision(snake.pos):
            print("OUCH!")
            return
        if snake.out_of_board():
            print("OUCH!")
            return
        if snake.eat(apple.pos):
            apple.kill()
            pos = (random.randint(0, BOARD_SIZE[0] - 1), random.randint(0, BOARD_SIZE[1] - 1))
            while snake.pos == pos or snake.collision(pos):
                pos = (random.randint(0, BOARD_SIZE[0] - 1), random.randint(0, BOARD_SIZE[1] - 1))
            apple = Apple(pos, SIZE_APPLE, COLOR_APPLE)

        for sprite in drawable:
            sprite.draw(screen)
        
        pg.display.flip()  # Update the display
        clock.tick(GAME_SPEED)

    pg.quit()

if __name__ == "__main__":
    main()