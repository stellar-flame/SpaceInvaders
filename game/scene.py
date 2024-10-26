import pygame
import random
from pygame.sprite import Group
from game.space_ship import SpaceShip
from game.alien_ship import AlienShip
from game.sprite import AnimatedSprite

class Scene:
    def __init__(self):
        self.player_sprites = Group()
        self.alien_sprites = Group()
        self.bullet_sprites = Group()
        self.alien_bullet_sprites = Group()

        self.explosion_sprites = Group()

        self.space_ship = SpaceShip()
        self.player_sprites.add(self.space_ship)

        pygame.time.set_timer(AlienShip.ALIEN_SPAWN_EVENT, 1000)

    def process_input(self, event):
        if event.type == AlienShip.ALIEN_SPAWN_EVENT:
            alien_ship = AlienShip()
            self.alien_sprites.add(alien_ship)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.bullet_sprites.add(self.space_ship.shoot())
            else:
                self.space_ship.process_input(event)


    def update(self, boundaries, delta):

        collisions = pygame.sprite.groupcollide(self.bullet_sprites, self.alien_sprites, True, True)

        for bullet, alien in collisions.items():
            explosion = AnimatedSprite(alien[0].grid_pos, "assets/Explosion.png", 10,
                                       64, 64, 3, False)
            self.explosion_sprites.add(explosion)

        if len(self.alien_sprites) > 0:
            self.alien_firing_mechanism()

        self.alien_sprites.update(boundaries, delta)
        self.player_sprites.update(boundaries, delta)
        self.bullet_sprites.update(boundaries, delta)
        self.explosion_sprites.update(boundaries, delta)
        self.alien_bullet_sprites.update(boundaries, delta)

    def render(self, window):
        self.alien_sprites.draw(window)
        self.player_sprites.draw(window)
        self.bullet_sprites.draw(window)
        self.explosion_sprites.draw(window)
        self.alien_bullet_sprites.draw(window)

    def alien_firing_mechanism(self):
        # Choose a random alien to fire with some probability
        if random.random() < 0.01:  # 1% chance per frame that an alien fires
            alien = random.choice(self.alien_sprites.sprites())
            self.alien_bullet_sprites.add(alien.fire())
