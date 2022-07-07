from pygame import Surface, draw, SRCALPHA, transform, display
from consts import HEIGHT, WIDTH


class BaseEntity:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        screen = display.set_mode((800, 600))
        screen_rect = screen.get_rect()  # A rect with the size of the screen.
        surface = Surface((50, 50), SRCALPHA)
        self.screen = Surface([WIDTH, HEIGHT], SRCALPHA, 32)


class Rectangle(BaseEntity):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.color = color
        self.rotatation = 0

    def display(self, angle=None):
        if angle is not None:
            self.rotatation = angle
        transform.rotate(self.screen, self.rotatation)
        draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def isTouching(self, other):
        return (
            self.x < other.x + other.width
            and self.x + self.width > other.x
            and self.y < other.y + other.height
            and self.y + self.height > other.y
        )
