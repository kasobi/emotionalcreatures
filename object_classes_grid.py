import pygame

from CONSTANTS import SCREEN_WIDTH
from CONSTANTS import SCREEN_HEIGHT


center_screen = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

radius1 = 100


class UnitSphube():
    def __init__(self, x, y):
        self.x_pos = x
        self.x_neg = x
        self.y_pos = y
        self.y_neg = y
        self.x_now = x
        self.y_now = y
        self.radius_1 = radius1
        self.color = pygame.Color("blue")

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, pygame.math.Vector2(self.x_now, self.y_now), self.radius_1)

    def update(self, x_pos, x_neg, y_pos, y_neg):
        pass




class VolumeGrid():
    def __init__(self):
        self.grid_cells = {}
        self.origin = None
        self.x = None
        self.y = None

    def create_grid(self, total_x: int, total_y: int):
        self.x = total_x
        self.y = total_y
        
        for x in range(total_x):
            starting_x = SCREEN_WIDTH//2 - (total_x//2 * radius1 * 2)

            for y in range(total_y):
                starting_y = SCREEN_HEIGHT//2 - (total_y//2 * radius1 * 2)
                self.grid_cells[f"x{x}y{y}"] = UnitSphube(starting_x, starting_y)
                starting_y += radius1

            starting_x += radius1


    def modify_grid(self, modifications):
        raise NotImplementedError()

    def do_a_tick(self):
        for x in range(self.x):
            for y in range(self.y):
                pass