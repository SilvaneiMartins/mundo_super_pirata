from settings import *

class UI:
    def __init__(self, font, frames):
        self.display_surface = pygame.display.get_surface()
        self.sprites = pygame.sprite.Group()
        self.font = font

        # health / healths
        self.heart_frames = frames['heart']

        # coins / coins