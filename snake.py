
import pygame as pg

#from square import Square
from constants import BOARD_SIZE, GROWTH, SIZE_SQUARE
from board import board_to_screen
#from snakepart import SnakePart


class SnakePart():
    def __init__(self, pos):
        self.pos = pos
        self.next = None


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
        self.next = None
        self.start_pos()
        
    def start_pos(self):
        next_pos = (self.pos[0] - self.direction[0], self.pos[1] - self.direction[1])
        self.next = SnakePart(next_pos)
        next_part = self.next
        for i in range(2, self.length):
            #print(i)
            next_pos = (next_part.pos[0] - self.direction[0], next_part.pos[1] - self.direction[1])
            next_part.next = SnakePart(next_pos)
            next_part = next_part.next

    def draw(self, screen):
        # Draw the snake as a rectangle
        x, y = board_to_screen(self.pos, self.size)
        pg.draw.rect(screen, self.color, (x, y, self.size, self.size))
        next_part = self.next
        while next_part:
            if next_part.next:
                x, y = board_to_screen(next_part.pos, self.size)
                pg.draw.rect(screen, self.color, (x, y, self.size, self.size))
            else:
                x, y = board_to_screen(next_part.pos, self.size / 2)
                pg.draw.rect(screen, self.color, (x, y, self.size / 2, self.size / 2))
            next_part = next_part.next


    def move(self, growing = 0):
        old_pos = self.pos
        self.pos = (self.pos[0] + self.direction[0], self.pos[1] + self.direction[1])
        next_part = self.next
        while next_part:
            tmp = next_part.pos
            next_part.pos = old_pos
            old_pos = tmp
            next_part = next_part.next

    def collision(self):
        next_part = self.next
        while next_part:
            if next_part.pos == self.pos:
                return True
            next_part = next_part.next
        return False

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
            if self.direction != (1, 0):
                self.direction = (-1, 0)
        if keys[pg.K_d]:
            if self.direction != (-1, 0):
                self.direction = (1, 0)
        if keys[pg.K_w]:
            if self.direction != (0, 1):
                self.direction = (0, -1)
        if keys[pg.K_s]:
            if self.direction != (0, -1):
                self.direction = (0, 1)
        self.move()

