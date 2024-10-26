from game.sprite import SpriteNode
import pygame


class Bullet(SpriteNode):
    def __init__(self, grid_pos):
        super().__init__(grid_pos)
        self.speed = 5
        self.direction = 1
        self.image = None
        self.rect = None  

    def update(self, boundaries, delta):
        self.grid_pos.y += self.direction * self.speed * delta
        if self.grid_pos.y < 0:
            self.kill()
        self.update_pixel_pos()

    def create_sprite(self, color, triangle_points):
        self.image = pygame.Surface((16, 16), pygame.SRCALPHA)  # Use SRCALPHA for transparency
        self.image.fill((0, 0, 0, 0))  # Fill with transparent background
        pygame.draw.polygon(self.image, color, triangle_points)
        self.rect = self.image.get_rect()
        self.update_pixel_pos()

    @staticmethod
    def create_space_ship_bullet(grid_pos):
        bullet = Bullet(grid_pos)
        bullet.direction = -1
        bullet.create_sprite((255, 165, 0), triangle_points=[(0, 16), (8, 0), (16, 16)])
        return bullet

    @staticmethod
    def create_alien_ship_bullet(grid_pos):
        bullet = Bullet(grid_pos)
        bullet.create_sprite((255, 0, 0), triangle_points=[(0, 0), (16, 0), (8, 16)])
        return bullet
