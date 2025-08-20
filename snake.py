
import pygame as pg

from square import Square
from constants import SQUARE_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT


class Snake(Square):
    def __init__(self, x, y, size, length):
        super().__init__(x, y, (0, 255, 0), size)
        self.length = length
        self.direction = (0, -1)  # Initial direction (up)
        #self.color = (0, 255, 0)  # Green color for the snake

    def draw(self, screen):
        # Draw the snake as a rectangle
        pg.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
        # Optionally, draw the snake's body segments if needed
        # for pos in self.positions:
        #     pg.draw.rect(surface, self.color, (pos[0], pos[1], self.size, self.size))

    def set_direction(self, dir):
        self.direction = dir

    def move(self):
        self.x += SQUARE_SIZE * self.direction[0]
        self.y += SQUARE_SIZE * self.direction[1]

    def out_of_board(self):
        if self.x < 0:
            #self.x += SQUARE_SIZE
            return True
        if self.x > SCREEN_WIDTH:
            #self.x -= SQUARE_SIZE
            return True
        if self.y < 0:
            #self.y += SQUARE_SIZE
            return True
        if self.y > SCREEN_HEIGHT:
            #self.y -= SQUARE_SIZE
            return True
        return False

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.set_direction((-1, 0))
        if keys[pg.K_d]:
            self.set_direction((1, 0))
        if keys[pg.K_w]:
            self.set_direction((0, -1))
        if keys[pg.K_s]:
            self.set_direction((0, 1))
        self.move()

