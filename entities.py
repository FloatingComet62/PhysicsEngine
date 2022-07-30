from pygame import Surface, transform
from consts import screen


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
        self.rotation = 0

        # the rectangle is a surface itself
        self.surface = Surface((width, height))
        self.surface.set_colorkey((0, 0, 0))
        self.surface.fill(color)
        self.rect = self.surface.get_rect()

    def display(self, angle=None):
        # updating values
        self.surface.fill(
            self.color
        )  # refill the surface color if you change it somewhere in the program
        self.rect = self.surface.get_rect()
        self.rect.center = (self.x, self.y)

        # renderer
        if angle is not None:
            self.rotation = angle

        old_center = self.rect.center
        new = transform.rotate(self.surface, self.rotation)
        self.rect = new.get_rect()
        self.rect.center = old_center
        screen.blit(new, self.rect)

    def isTouching(self, other):
        return (
            self.x < other.x + other.width
            and self.x + self.width > other.x
            and self.y < other.y + other.height
            and self.y + self.height > other.y
        )
