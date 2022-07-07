from pygame import init, display, quit, event, time, mouse, QUIT
from entities import Rectangle
from consts import FPS, HEIGHT, RUNNING, SCREEN_COLOR, WIDTH


init()
screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Physics Engine")
clock = time.Clock()

player = Rectangle(0, 0, 100, 100, (15, 15, 15))
static = Rectangle(200, 200, 100, 100, (20, 20, 20))

while RUNNING:
    # display
    display.update()
    screen.fill(SCREEN_COLOR)
    clock.tick(FPS)

    # mouse stick
    (mouseX, mouseY) = mouse.get_pos()
    player.x = mouseX - 50
    player.y = mouseY - 50

    # touch
    if player.isTouching(static):
        static.color = (255, 0, 0)
    else:
        static.color = (20, 20, 20)

    # display sprites
    static.display(24)
    player.display(56)

    # events
    for e in event.get():
        if e.type == QUIT:
            quit()
            RUNNING = False
