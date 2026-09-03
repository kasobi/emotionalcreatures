import pygame

from CONSTANTS import *


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

BLACK = pygame.Color(0,0,0,1)
RED = pygame.Color(255,0,0,1)
GREEN = pygame.Color(0,255,0,1)
BLUE = pygame.Color(0,0,255,1)


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

enemy_pos_15 = pygame.Vector2(screen.get_width() / 1.5, screen.get_height() / 1.5)

def main():

    while running:

        screen.fill("black")

        
        pygame.draw.circle(screen, "red", player_pos, 40)

        pygame.draw.circle(screen, "green", enemy_pos_15, 20)

        chase = enemy_pos_15.smoothstep(player_pos, .1)

        enemy_pos_15.x, enemy_pos_15.y = chase

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        pygame.display.flip()

        dt = clock.tick(60) / 1000 #sets FPS to 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
