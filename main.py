import pygame

from CONSTANTS import SCREEN_WIDTH
from CONSTANTS import SCREEN_HEIGHT


pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True






def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True


    while True:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
