import os
import pygame
from pygame.math import Vector2
from game.scene import Scene
from settings import CELL_SIZE
from settings import WORLD_SIZE


class Game:
    def grid_to_pixel(grid_pos: Vector2):
        return grid_pos.elementwise() * CELL_SIZE

    def pixel_to_grid(pixel_pos: Vector2):
        return Vector2(pixel_pos).elementwise() / CELL_SIZE

    def __init__(self):
        pygame.init()
        self.window_size = WORLD_SIZE.elementwise() * CELL_SIZE
        self.window = pygame.display.set_mode((int(self.window_size.x), int(self.window_size.y)))

        self.scene = Scene()

        # Loop properties
        self.clock = pygame.time.Clock()
        self.running = True

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            else:
                self.scene.process_input(event)

    def update(self, delta_time):
        self.scene.update(WORLD_SIZE, delta_time)

    def render(self):
        self.window.fill((0, 0, 0))
        self.scene.render(self.window)
        pygame.display.update()

    def run(self):
        while self.running:
            """the delta time is the time since the last frame which is
            approx 1000ms/60ms (since there are 60 frames in 1 second i.e. 1000ms) then divided by 
            1000 to get delta time in seconds"""

            delta_time = self.clock.tick(60) / 1000.0
            self.process_input()
            self.update(delta_time)
            self.render()


game = Game()
game.run()
pygame.quit()
