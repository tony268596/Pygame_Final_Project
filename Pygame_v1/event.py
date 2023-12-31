import pygame
import math
import os
from settings import en_PATH, hero_BASE
from color_settings import *
from settings import IMAGE_PATH,SOUND_PATH
import random

# event images
tsunami_wave_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "tsunami_2.png")), (1024, 600))
tsunami_sound = pygame.mixer.Sound(os.path.join(SOUND_PATH, "tsunami-wave.mp3"))


class Event:
    def __init__(self):
        self.image = tsunami_wave_image
        self.rect = self.image.get_rect()
        self.stride = 10
        self.move_count = 0
        self.enable = False
        self.X =  (-1000,320)#(-10000,320) about 30s
        self.Y = (2000,320)
    def move(self):
        x1, y1 = self.X
        x2, y2 = self.Y
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        max_count = int(distance / self.stride)
        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance
        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count
        # update the position and counter
        if self.move_count <= max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.move_count = 0
            self.X = (random.randint(-3000, -2000),320)
            self.Y = (2000,320)
            # print(self.X, " ", self.Y)
            #self.rect = (-600,0)
    def advance(self, model):
        self.move()
        waveX, waveY = self.rect.center
        # print(waveX)
        for en in model.en.expedition:
            enX, enY = en.rect.center
            # print(enX)
            if(waveX - enX > 10 and waveX - enX < 20):
                if(bool(random.getrandbits(1))):
                #     en.health -= 99999
                # else:
                    en.health /= 2
        for he in model.he.expedition:
            heX, heY = he.rect.center
            if(waveX - heX > 10 and waveX - heX < 20):
                if(bool(random.getrandbits(1))):
                    he.health -= 99999
                else:
                    he.health /= 2
        if(waveX - -100 >= 0 and waveX - -100 <= 10):
            pygame.mixer.Channel(3).play(tsunami_sound)
            