import pygame


pygame.init()
WIDTH = 800
HEIGHT = 600
SCREEN_COLOR = (90, 150, 70)
FPS = 60
RUNNING = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Engine")
clock = pygame.time.Clock()

if __name__ == "__main__":
    from entities import Rectangle

    while RUNNING:
        pygame.display.update()
        screen.fill(SCREEN_COLOR)
        clock.tick(FPS)

        (mouseX, mouseY) = pygame.mouse.get_pos()
        player = Rectangle(mouseX - 50, mouseY - 50, 100, 100, (15, 15, 15))
        static = Rectangle(300, 300, 100, 100, (20, 20, 20))


        static.display()
        player.display()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                RUNNING = False
