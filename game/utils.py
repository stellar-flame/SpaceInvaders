import pygame
from pygame import Vector2
from settings import CELL_SIZE


class Utils:
    event_counter =  pygame.USEREVENT

    @staticmethod
    def grid_to_pixel(grid_pos: Vector2):
        return grid_pos.elementwise() * CELL_SIZE


    @staticmethod
    def pixel_to_grid(pixel_pos: Vector2):
        return Vector2(pixel_pos).elementwise() / CELL_SIZE

    @staticmethod
    def next_event():
        Utils.event_counter += 1
        return Utils.event_counter