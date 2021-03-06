import os
import pygame as pg
from . import tools
#from .components import players

SCREEN_SIZE = (1080, 740)
ORIGINAL_CAPTION = "Spell Pop"

pg.init()
os.environ['SDL_VIDEO_CENTERED'] = "TRUE"
pg.display.set_caption(ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

WORDS = tools.load_words(os.path.join("resources", "words"))
FONTS = tools.load_all_fonts(os.path.join("resources", "fonts"))
#MUSIC = tools.load_all_music(os.path.join("resources", "music"))
SFX   = tools.load_all_sfx(os.path.join("resources", "sound"))
#GFX   = tools.load_all_gfx(os.path.join("resources", "graphics"))
#PLAYER = players.Player()
