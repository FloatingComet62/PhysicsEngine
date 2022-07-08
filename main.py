from pygame import init, display, quit, event, time, mouse, QUIT
from entities import Rectangle
from consts import FPS, RUNNING, SCREEN_COLOR, screen


init()
display.set_caption("Physics Engine")
clock = time.Clock()

player = Rectangle(0, 0, 100, 100, (15, 15, 15))
static = Rectangle(200, 200, 100, 100, (30, 30, 30))

rotation = 0
rotation_speed = 5

while RUNNING:
    # display
    display.update()
    screen.fill(SCREEN_COLOR)
    clock.tick(FPS)

    # mouse stick
    (mouseX, mouseY) = mouse.get_pos()
    player.x = mouseX
    player.y = mouseY

    # touching
    static.color = (255, 0, 0) if player.isTouching(static) else (30, 30, 30)

    # display sprites
    rotation += rotation_speed
    static.display(24)
    player.display(rotation)

    # events
    for e in event.get():
        if e.type == QUIT:
            quit()
            RUNNING = False
