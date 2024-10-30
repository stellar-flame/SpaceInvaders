from abc import ABC, abstractmethod
from game.game_manager import GameManager


class BaseScene(ABC):
    def __init__(self, game_manager):
        self.game_manager: GameManager = game_manager

    @abstractmethod
    def process_input(self, event):
        pass

    @abstractmethod
    def update(self, delta, boundaries = None):
        pass

    @abstractmethod
    def render(self, window):
        pass
