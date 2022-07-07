from pygame import init, display, transform, quit, event, time, mouse, QUIT
from entities import Rectangle


init()
WIDTH = 800
HEIGHT = 600
SCREEN_COLOR = (90, 150, 70)
FPS = 60
RUNNING = True
screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Physics Engine")
clock = time.Clock()
transform.rotate(screen, 45)

while RUNNING:
    display.update()
    screen.fill(SCREEN_COLOR)
    clock.tick(FPS)

    (mouseX, mouseY) = mouse.get_pos()
    player = Rectangle(screen, mouseX - 50, mouseY - 50, 100, 100, (15, 15, 15))
    static = Rectangle(screen, 300, 300, 100, 100, (20, 20, 20))

    if player.isTouching(static):
        static.color = (255, 0, 0)
    else:
        static.color = (20, 20, 20)

    static.display()
    player.display()
    for e in event.get():
        if e.type == QUIT:
            quit()
            RUNNING = False
