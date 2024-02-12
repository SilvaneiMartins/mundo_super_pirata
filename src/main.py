from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join

from support import *

class Game:
    def __init__(self):
        pygame.init()

        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Mundo do Super Pirada - by: Silvanei Martins")
        self.clock = pygame.time.Clock()
        self.import_assets()

        self.tmx_maps = {0: load_pygame(join('src', 'data', 'levels', 'omni.tmx'))}
        self.current_stage = Level(self.tmx_maps[0], self.level_frames)

    def import_assets(self):
        self.level_frames = {
            'flag': import_folder('src', 'graphics', 'level', 'flag'),
			'saw': import_folder('src', 'graphics', 'enemies', 'saw', 'animation'),
			'floor_spike': import_folder('src', 'graphics','enemies', 'floor_spikes'),
			'palms': import_sub_folders('src', 'graphics', 'level', 'palms'),
			'candle': import_folder('src', 'graphics','level', 'candle'),
			'window': import_folder('src', 'graphics','level', 'window'),
			'big_chain': import_folder('src', 'graphics','level', 'big_chains'),
			'small_chain': import_folder('src', 'graphics','level', 'small_chains'),
			'candle_light': import_folder('src', 'graphics','level', 'candle light'),
			'player': import_sub_folders('src', 'graphics','player'),
			'saw': import_folder('src', 'graphics', 'enemies', 'saw', 'animation'),
			'saw_chain': import_image('src',  'graphics', 'enemies', 'saw', 'saw_chain'),
			'helicopter': import_folder('src', 'graphics', 'level', 'helicopter'),
			'boat': import_folder('src',  'graphics', 'objects', 'boat'),
			'spike': import_image('src',  'graphics', 'enemies', 'spike_ball', 'Spiked Ball'),
			'spike_chain': import_image('src',  'graphics', 'enemies', 'spike_ball', 'spiked_chain'),
			'tooth': import_folder('src', 'graphics','enemies', 'tooth', 'run'),
			'shell': import_sub_folders('src', 'graphics','enemies', 'shell'),
			'pearl': import_image('src',  'graphics', 'enemies', 'bullets', 'pearl'),
			'items': import_sub_folders('src', 'graphics', 'items'),
			'particle': import_folder('src', 'graphics', 'effects', 'particle'),
			'water_top': import_folder('src', 'graphics', 'level', 'water', 'top'),
			'water_body': import_image('src', 'graphics', 'level', 'water', 'body'),
			'bg_tiles': import_folder_dict('src', 'graphics', 'level', 'bg', 'tiles'),
			'cloud_small': import_folder('src', 'graphics','level', 'clouds', 'small'),
			'cloud_large': import_image('src', 'graphics','level', 'clouds', 'large_cloud'),
        }

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_stage.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
