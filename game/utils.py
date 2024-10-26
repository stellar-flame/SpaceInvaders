from pygame import Vector2
from settings import CELL_SIZE


def grid_to_pixel(grid_pos: Vector2):
    return grid_pos.elementwise() * CELL_SIZE


def pixel_to_grid(pixel_pos: Vector2):
    return Vector2(pixel_pos).elementwise() / CELL_SIZE
