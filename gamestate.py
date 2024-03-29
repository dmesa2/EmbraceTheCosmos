import os

# DEFINITIONS
WHITE = (200, 200, 200)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
RED = (200, 0, 0)
BLACK = (0,0,0)
GRAY = (128,128,128)
CYAN = (100, 150, 245)
YELLOW = (214, 224, 20)
ORCHIRD = (104,34,139)

BRIGHT_WHITE = (255,255,255)
BRIGHT_GREEN = (0, 255, 0)
BRIGHT_BLUE = (0, 0, 255)
BRIGHT_RED = (255, 0, 0)
BRIGHT_GRAY = (169,169,169)
BRIGHT_YELLOW = (242, 255, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CARD_WIDTH = 140
CARD_HEIGHT = 195
TARGET_SIZE = (36, 36)
ICON_SIZE = 48

MOUSE_ONE = 0
MOUSE_TWO = 1

MAP_DELTA = 15
# PATHS
ASSETS_PATH = os.path.join(os.getcwd(), 'assets')
SHIPS_PATH = os.path.join(ASSETS_PATH, "Spaceships", "spaceships", "parts_spriter_animation")
CARD_PATH = os.path.join(ASSETS_PATH, "Cards")
EXPLOSIONS_PATH = os.path.join(ASSETS_PATH, "Spaceships", "spaceships", "PNG_Animations", "Explosions")
MAP_ICON_PATH = os.path.join(ASSETS_PATH, "map_icons")
ICON_PATH = os.path.join(ASSETS_PATH, "Misc")
BACKGROUND_PATH = os.path.join(ASSETS_PATH, "Background")
