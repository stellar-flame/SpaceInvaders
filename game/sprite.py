import pygame
from pygame.sprite import Sprite
import game.utils

class SpriteNode(Sprite):
    def __init__(self, grid_pos, texture=None):
        super().__init__()
        self.grid_pos = grid_pos
        self.set_texture(texture)
        self.rect = self.image.get_rect()
        self.update_pixel_pos()

    def set_texture(self, texture):
        self.image = pygame.image.load(texture).convert_alpha()

    def update_pixel_pos(self):
        self.rect.topleft = game.utils.grid_to_pixel(self.grid_pos)

    def process_input(self, event):
        pass


class AnimatedSprite(SpriteNode):
    def __init__(self, grid_pos, texture, frame_rate, frame_width, frame_height, num_frames, loop=True):
        self.images = self.load_sprite_sheet(texture, frame_width, frame_height, num_frames)
        self.frame_rate = frame_rate  # How many frames to wait before switching frames
        self.timer = 0
        self.current_frame = 0
        self.loop = loop
        super().__init__(grid_pos)

    def set_texture(self, texture):
        self.image = self.images[self.current_frame]  # Set the initial image

    def load_sprite_sheet(self, texture, frame_width, frame_height, num_frames):
        sprite_sheet = pygame.image.load(texture).convert_alpha()
        frames = []
        for i in range(num_frames):
            # Extract each frame from the sprite sheet
            frame = sprite_sheet.subsurface((i * frame_width, 0, frame_width, frame_height))
            frames.append(frame)
        return frames

    def update(self, boundaries, delta):
        self.timer += 1
        if self.timer >= self.frame_rate:
            if not self.loop and self.current_frame == len(self.images) - 1:
                self.kill()
            else:
                # Reset the timer and move to the next frame
                self.timer = 0
                self.current_frame = (self.current_frame + 1) % len(self.images)
                self.image = self.images[self.current_frame]
