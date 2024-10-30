import pygame
from pygame import Vector2
from game.utils import Utils

from enum import Enum, auto


class GameState(Enum):
    PLAYING = auto()
    GAME_OVER = auto()
    MARK_FOR_RESET = auto()


class GameManager:

    def __init__(self, max_lives):
        self.max_lives = max_lives
        self.reset()

    def update_lives_left(self):
        self.lives_left -= 1
        if self.lives_left == 0:
            self.end_game()

    def end_game(self):
        self.state = GameState.GAME_OVER

    def update_score(self):
        self.score += 50

    def is_over(self):
        return self.state == GameState.GAME_OVER

    def is_marked_for_reset(self):
        return self.state == GameState.MARK_FOR_RESET

    def mark_for_reset(self):
        self.state = GameState.MARK_FOR_RESET

    def reset(self):
        self.lives_left = self.max_lives
        self.score = 0
        self.state = GameState.PLAYING

    def render(self, window):
        font = pygame.font.Font(None, 36)  # 36 is the font size
        score_text = font.render(f"{self.score:07}", True, (255, 255, 255))
        window.blit(score_text, tuple(Utils.grid_to_pixel(Vector2(14, 9.3))))

        for i in range(self.lives_left - 1):
            texture = pygame.image.load("assets/ship.png").convert_alpha()  # Use convert_alpha() for transparency
            window.blit(texture, tuple(Utils.grid_to_pixel(Vector2(i, 9))))
