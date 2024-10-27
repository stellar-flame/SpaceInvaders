import pygame
from pygame import Vector2
from game.utils import Utils


class GameManager:

    def __init__(self, max_lives):
        self.max_lives = max_lives
        self.lives_left = max_lives
        self.score = 0

    def update_lives_left(self):
        self.lives_left -= 1

    def update_score(self):
        self.score += 50

    def render(self, window):
        font = pygame.font.Font(None, 36)  # 36 is the font size
        score_text = font.render(f"{self.score:07}", True, (255, 255, 255))
        window.blit(score_text, tuple(Utils.grid_to_pixel(Vector2(14, 9.3))))

        for i in range(self.lives_left-1):
            texture = pygame.image.load("assets/ship.png").convert_alpha()  # Use convert_alpha() for transparency
            window.blit(texture, tuple(Utils.grid_to_pixel(Vector2(i, 9))))