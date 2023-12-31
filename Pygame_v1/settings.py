import pygame
import os
import random

# screen size
WIN_WIDTH = 1024
WIN_HEIGHT = 600

HEALTH_WIDTH, HEALTH_HEIGHT = 150, 10

# frame rate
FPS = 60

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (147, 0, 147)

COLOR_INACTIVE = pygame.Color('gray100')
COLOR_ACTIVE = pygame.Color('dodgerblue2')

# skill moving
skill_PATH = [(500, 600), (500, 0)]

# enemy path
en_PATH = [[(100, 460), (1024, 460)],
           [(100, 465), (1024, 465)],
           [(100, 470), (1024, 470)]
           ]

hero_PATH = [[(954, 405), (100, 405)],
             [(954, 415), (100, 415)],
             [(954, 425), (100, 425)],
             [(954, 435), (100, 435)],
             [(954, 445), (100, 445)]
            ]

# base
hero_BASE = pygame.Rect(874, 350, 150, 150)
en_BASE = pygame.Rect(0, 300, 150, 200)

# 絕對路徑
IMAGE_PATH = os.path.join(os.path.dirname(__file__), "images")
SOUND_PATH = os.path.join(os.path.dirname(__file__), "sound")
BACKGROUND_IMAGE = pygame.image.load(os.path.join(IMAGE_PATH, "game_bg.png"))
BACKGROUND_IMAGE_two = pygame.image.load(os.path.join(IMAGE_PATH, "bg_2.png"))
BACKGROUND_IMAGE_three = pygame.image.load(os.path.join(IMAGE_PATH, "bg_3.png"))
RECORD_PATH = os.path.join(os.path.dirname(__file__), "user_record")


game_status: dict = {
    "run": True,
    "go_start_menu": False,
    "go_level_menu": False,
    "go_input_window": False
}

LEVEL_FINISH_TIMES = [0, 0, 0]

user_info: dict = {
    'user_name': '',
    'user_used_time': []
}

music: dict = {
    "mute": False
}
