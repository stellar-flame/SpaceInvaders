import pygame
import random
from pygame import Vector2
from pygame.sprite import Group
from pygame.sprite import GroupSingle
from game.space_ship import SpaceShip
from game.alien_ship import AlienShip
from game.sprite import AnimatedSprite
from game.utils import Utils
from game.base_scene import BaseScene


class Scene(BaseScene):

    def __init__(self, game_manager):
        super().__init__(game_manager)
        self.player_sprites = GroupSingle()
        self.alien_sprites = Group()
        self.bullet_sprites = Group()
        self.alien_bullet_sprites = Group()

        self.explosion_sprites = Group()

        self.space_ship = SpaceShip()
        self.player_sprites.add(self.space_ship)
        self.alien_spawn_freq = 1000
        pygame.time.set_timer(AlienShip.ALIEN_SPAWN_EVENT, self.alien_spawn_freq)

    def process_input(self, event):
        if event.type == AlienShip.ALIEN_SPAWN_EVENT:
            alien_ship = AlienShip()
            self.alien_sprites.add(alien_ship)
        elif event.type == AnimatedSprite.ANIMATION_COMPLETE_EVENT and event.sprite == self.space_ship.explosion:
                self.start_next_life()
        elif self.space_ship and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = self.space_ship.shoot()
                if bullet:
                    self.bullet_sprites.add(bullet)
            else:
                self.space_ship.process_input(event)

    def start_next_life(self):
        self.game_manager.update_lives_left()
        if not self.game_manager.is_over():
            self.space_ship = SpaceShip()
            self.player_sprites.add(self.space_ship)

    def update(self, delta, boundaries=None):
        self.alien_hits_space_ship_collision()
        self.bullets_hits_alien_collisions()
        self.bullet_hits_space_ship_collisions()

        self.make_alien_ships_fire()

        self.alien_sprites.update(boundaries, delta)
        self.bullet_sprites.update(boundaries, delta)
        self.alien_bullet_sprites.update(boundaries, delta)
        self.player_sprites.update(boundaries, delta)
        self.explosion_sprites.update(boundaries, delta)

    def make_alien_ships_fire(self):
        if len(self.alien_sprites) > 0:
            self.alien_firing_mechanism()

    def alien_firing_mechanism(self):
        # Choose a random alien to fire with some probability
        if random.random() < 0.02:  # 1% chance per frame that an alien fires
            alien = random.choice(self.alien_sprites.sprites())
            self.alien_bullet_sprites.add(alien.fire())


    def alien_hits_space_ship_collision(self):
        collisions = pygame.sprite.groupcollide(self.player_sprites, self.alien_sprites, True, True)
        for player, alien in collisions.items():
            self.space_ship.explosion = self.create_exploding_sprite(alien[0].grid_pos)

    def bullets_hits_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullet_sprites, self.alien_sprites, True, True)
        for bullet, alien in collisions.items():
            self.create_exploding_sprite(alien[0].grid_pos)
            self.game_manager.update_score()
            if self.game_manager.score > 0 and self.game_manager.score % 500 == 0:
                self.update_alien_spawn_freq()

    def update_alien_spawn_freq(self):
        self.alien_spawn_freq = max(self.alien_spawn_freq - 150, 500)
        pygame.time.set_timer(AlienShip.ALIEN_SPAWN_EVENT, self.alien_spawn_freq)

    def bullet_hits_space_ship_collisions(self):
        collisions = pygame.sprite.groupcollide(self.player_sprites, self.alien_bullet_sprites, True, True)
        if len(collisions) > 0:
            self.space_ship.explosion = self.create_exploding_sprite(self.space_ship.grid_pos)

    def create_exploding_sprite(self, grid_pos):
        explosion = AnimatedSprite(grid_pos, "assets/Explosion.png", 10,
                                   64, 64, 3, False)
        self.explosion_sprites.add(explosion)
        return explosion

    def render(self, window):
        pygame.draw.line(window, (255, 255, 255), Utils.grid_to_pixel(Vector2(0, 9)),
                         Utils.grid_to_pixel(Vector2(16, 9)), width=2)  # Draw a white line, 5 pixels thick

        self.alien_sprites.draw(window)
        self.player_sprites.draw(window)
        self.bullet_sprites.draw(window)
        self.alien_bullet_sprites.draw(window)
        self.explosion_sprites.draw(window)
