import pygame, sys
from pygame.math import Vector2 as vector

# settings
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
TILE_SIZE = 64
ANIMATION_SPEED = 6

# colors
SKY_COLOR = '#DDC6A1'
CLOUD_COLOR = '#92A9CE'
HORIZON_COLOR = '#F5F1DE'

# layers 
Z_LAYERS = {
	'bg': 0,
	'clouds': 1,
	'bg tiles': 2,
	'path': 3,
	'bg details': 4,
	'main': 5,
	'water': 6,
	'fg': 7
}