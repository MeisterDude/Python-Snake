
import pygame as pg

from snake import Snake

SCREEN_WIDTH = 801
SCREEN_HEIGHT = 801
SQUARE_SIZE = 20

def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Snake")
    clock = pg.time.Clock()
    dt = 0

    drawable = pg.sprite.Group()
    updatable = pg.sprite.Group()
    Snake.containers = drawable, updatable

    snake = Snake(100, 100, SQUARE_SIZE + 1)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        screen.fill((0, 0, 0))  # Fill the screen with black
        for i in range(41):
            pg.draw.line(screen, (100, 100, 100), (0, i * SQUARE_SIZE), (SCREEN_HEIGHT, i * SQUARE_SIZE))
            pg.draw.line(screen, (100, 100, 100), (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, SCREEN_WIDTH))
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        pg.display.flip()  # Update the display
        dt = clock.tick(60) / 1000
    pg.quit()

if __name__ == "__main__":
    main()