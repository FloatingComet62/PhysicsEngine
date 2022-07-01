import pygame
import main


class BaseEntity:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Rectangle(BaseEntity):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.color = color

    def display(self):
        pygame.draw.rect(
            main.screen, self.color, (self.x, self.y, self.width, self.height)
        )

    def isTouching(self, other):
        return (
            self.x < other.x + other.width
            and self.x + self.width > other.x
            and self.y < other.y + other.height
            and self.y + self.height > other.y
        )
