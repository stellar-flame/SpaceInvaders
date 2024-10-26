from game.sprite import SpriteNode
import pygame
from pygame import Vector2
from game.bullet import Bullet
import game.utils


class SpaceShip(SpriteNode):
    def __init__(self):
        super().__init__(Vector2(0, 8))
        self.set_texture("assets/ship.png")
        self.move_command = Vector2(0, 0)

    def process_input(self, event):
        if event.key == pygame.K_RIGHT:
            self.move_command.x = 1
        elif event.key == pygame.K_LEFT:
            self.move_command.x = -1

    def update(self, boundaries, delta):
        self.grid_pos += self.move_command

        if self.grid_pos.x < 0:
            self.grid_pos.x = 0
        elif self.grid_pos.x >= boundaries.x:
            self.grid_pos.x = boundaries.x - 1
        self.update_pixel_pos()
        self.move_command = Vector2(0, 0)

    def shoot(self):
        return Bullet.create_space_ship_bullet(game.utils.pixel_to_grid(self.rect.center))
