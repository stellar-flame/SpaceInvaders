from pygame import Vector2

CELL_SIZE = Vector2(64, 64)
WORLD_SIZE = Vector2(16, 10)
PLAY_AREA = WORLD_SIZE.elementwise() - Vector2(0, 1)
