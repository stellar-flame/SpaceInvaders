import pygame
from game.sprite import SpriteNode
from pygame import Vector2
from game.bullet import AlienBullet
import game.utils


class AlienShip(SpriteNode):
    ALIEN_SPAWN_EVENT = pygame.USEREVENT + 1

    def __init__(self):
        super().__init__(Vector2(16, 0), "assets/alien.png")
        self.speed = 5
        self.direction = -1

    def update(self, boundaries, delta):
        self.grid_pos.x += self.direction * self.speed * delta

        if ((self.grid_pos.x <= 0 and self.direction == -1) or
                (self.grid_pos.x > boundaries.x - 1 and self.direction == 1)):
            self.grid_pos.y += 1
            self.direction *= -1

        self.update_pixel_pos()

    def fire(self):
        return AlienBullet(game.utils.pixel_to_grid(self.rect.center))
