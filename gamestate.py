import os

# DEFINITIONS
WHITE = (200, 200, 200)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
RED = (200, 0, 0)
BLACK = (0,0,0)
GRAY = (128,128,128)
CYAN = (100, 150, 245)

BRIGHT_WHITE = (255,255,255)
BRIGHT_GREEN = (0, 255, 0)
BRIGHT_BLUE = (0, 0, 255)
BRIGHT_RED = (255, 0, 0)
BRIGHT_GRAY = (169,169,169)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CARD_WIDTH = int(93 * 1.5)
CARD_HEIGHT = int(130 * 1.5)

# PATHS
ASSETS_PATH = os.path.join(os.getcwd(), 'assets')
SHIPS_PATH = os.path.join(ASSETS_PATH, "Spaceships", "spaceships", "parts_spriter_animation")
CARD_PATH = os.path.join(ASSETS_PATH, "Cards")
