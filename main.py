
import pygame as pg
import math

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

    snake = Snake(START_POS_X, START_POS_Y, SQUARE_SIZE -1, START_LENGTH)
    apple = Apple(103, 103, SQUARE_SIZE - 5)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        screen.fill((0, 0, 0))  # Fill the screen with black
        for i in range(41):
            pg.draw.line(screen, (100, 100, 100), (0, i * SQUARE_SIZE), (SCREEN_WIDTH, i * SQUARE_SIZE))
            pg.draw.line(screen, (100, 100, 100), (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, SCREEN_HEIGHT))
        updatable.update()
        for sprite in drawable:
            sprite.draw(screen)
        if snake.out_of_board():
            print("OUCH!")
            return
        pg.display.flip()  # Update the display
        #dt = clock.tick(60) / 1000
        clock.tick(GAME_SPEED)
    pg.quit()

if __name__ == "__main__":
    main()