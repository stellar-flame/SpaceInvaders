from game.base_scene import BaseScene
import pygame
from pygame import Vector2
from game.utils import Utils


class GameOverScene(BaseScene):

    def __init__(self, game_manager):
        super().__init__(game_manager)

    def process_input(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            self.game_manager.mark_for_reset()

    def update(self, delta, boundaries=None):
        pass

    def render(self, window):
        font = pygame.font.Font(None, 72)
        small_font = pygame.font.Font(None, 36)

        window.fill((0, 0, 0))
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        center_x = window.get_width() // 2
        center_y = window.get_height() // 2
        text_rect = game_over_text.get_rect(center=(center_x, center_y))
        window.blit(game_over_text, text_rect)

        # Display restart message
        restart_text = small_font.render("Press R to Restart", True, (255, 255, 255))
        text_rect = restart_text.get_rect(center=(center_x, center_y+50))

        window.blit(restart_text, text_rect)

        pygame.display.flip()
