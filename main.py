import pygame
from game.scene import Scene
from game.game_over_scene import GameOverScene
from game.game_manager import GameManager
import settings


class Game:
    def __init__(self):
        pygame.init()
        self.window_size = settings.WORLD_SIZE.elementwise() * settings.CELL_SIZE
        self.window = pygame.display.set_mode((int(self.window_size.x), int(self.window_size.y)))

        self.game_manager = GameManager(3)
        self.scene = Scene(self.game_manager)
        self.game_over_scene = GameOverScene(self.game_manager)

        # Loop properties
        self.clock = pygame.time.Clock()
        self.running = True
        self.pause_count = 0

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif self.game_manager.is_over():
                self.game_over_scene.process_input(event)
            else:
                self.scene.process_input(event)

    def update(self, delta_time):
        if self.game_manager.is_over():
            self.game_over_scene.update(delta_time)
        else:
            if self.game_manager.is_marked_for_reset():
                self.scene = Scene(self.game_manager)
                self.game_manager.reset()
            self.scene.update(delta_time, settings.PLAY_AREA)

    def render(self):
        self.window.fill((0, 0, 0))

        if self.game_manager.is_over():
            self.game_over_scene.render(self.window)
        else:
            self.scene.render(self.window)
            self.game_manager.render(self.window)

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
