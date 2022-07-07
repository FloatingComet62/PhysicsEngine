from pygame import Surface, draw


class BaseEntity:
    def __init__(self, x: int, y: int, screen: Surface):
        self.x = x
        self.y = y
        self.screen = screen


class Rectangle(BaseEntity):
    def __init__(
        self, screen: Surface, x: int, y: int, width: int, height: int, color: tuple
    ):
        super().__init__(x, y, screen)
        self.width = width
        self.height = height
        self.color = color

    def display(self):
        draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def isTouching(self, other):
        return (
            self.x < other.x + other.width
            and self.x + self.width > other.x
            and self.y < other.y + other.height
            and self.y + self.height > other.y
        )
