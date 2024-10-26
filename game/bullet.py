from game.sprite import SpriteNode
import pygame


class Bullet(SpriteNode):
    def __init__(self, grid_pos):
        super().__init__(grid_pos)

    def update(self, boundaries, delta):
        self.grid_pos.y += self.direction * self.speed * delta
        if self.grid_pos.y < 0:
            self.kill()
        self.update_pixel_pos()

    def create_sprite(self, color, triangle_points):
        self.image = pygame.Surface((16, 16), pygame.SRCALPHA)  # Use SRCALPHA for transparency
        self.image.fill((0, 0, 0, 0))  # Fill with transparent background
        pygame.draw.polygon(self.image, color, triangle_points)


class SpaceShipBullet(Bullet):
    def __init__(self, grid_pos):
        self.speed = 5
        self.direction = -1
        super().__init__(grid_pos)

    def set_texture(self, texture):
        self.create_sprite((255, 165, 0), triangle_points=[(0, 16), (8, 0), (16, 16)])


class AlienBullet(Bullet):
    def __init__(self, grid_pos):
        self.speed = 5
        self.direction = 1
        super().__init__(grid_pos)

    def set_texture(self, texture):
        self.create_sprite((255, 0, 0), triangle_points=[(0, 0), (16, 0), (8, 16)])
