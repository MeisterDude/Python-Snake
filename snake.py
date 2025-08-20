
import pygame as pg

#from square import Square
from constants import BOARD_SIZE, GROWTH, SIZE_SQUARE
from board import board_to_screen


class Snake(pg.sprite.Sprite):
    def __init__(self, pos, size, length, color):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.pos = pos
        self.size = size
        self.length = length
        self.color = color
        self.direction = (0, -1)  # Initial direction (up)
        
    def start_pos(self):
        for i in range(1, self.length):
            pass

    def draw(self, screen):
        # Draw the snake as a rectangle
        x, y = board_to_screen(self.pos)
        x += (SIZE_SQUARE - self.size) / 2
        y += (SIZE_SQUARE - self.size) / 2
        pg.draw.rect(screen, self.color, (x, y, self.size, self.size))
        # Optionally, draw the snake's body segments if needed
        # for pos in self.positions:
        #     pg.draw.rect(surface, self.color, (pos[0], pos[1], self.size, self.size))


    def move(self):
        self.pos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])

    def eat(self, pos):
        if self.pos == pos:
            self.length += GROWTH
            return True
        return False

    def out_of_board(self):
        if self.pos[0] < 0:
            return True
        if self.pos[0] > BOARD_SIZE[0]:
            return True
        if self.pos[1] < 0:
            return True
        if self.pos[1] > BOARD_SIZE[1]:
            return True
        return False

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.direction = (-1, 0)
        if keys[pg.K_d]:
            self.direction = (1, 0)
        if keys[pg.K_w]:
            self.direction = (0, -1)
        if keys[pg.K_s]:
            self.direction = (0, 1)
        self.move()

