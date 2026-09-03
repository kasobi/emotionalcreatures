import pygame

from CONSTANTS import *
from creatures import RectShape


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0
running = True

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

RectShape.containers = updatable, drawable

rect_size = 10
x_cord = 0
y_cord = 0

num_x = SCREEN_WIDTH//rect_size
num_y = SCREEN_HEIGHT//rect_size


grid = {}

for x in range(num_x):
    for y in range(num_y):
        grid[f"x{x}y{y}"] = RectShape(x * rect_size, y * rect_size, rect_size, rect_size)

for rect in grid:
    cell = grid[rect]
    y = cell.


def main():

    while running:

        screen.fill("black")

        for i in drawable:
            i.draw(screen)

        for i in updatable:
            i.update()



        pygame.display.flip()

        dt = clock.tick(60) / 1000 #sets FPS to 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
