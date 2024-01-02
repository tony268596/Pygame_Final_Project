import pygame
import math
import os
from settings import hero_PATH, en_BASE, IMAGE_PATH, SOUND_PATH
from color_settings import *
import random

# pygame.init()
DOG_IMAGE = [pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "dog-1.png")), (60, 90)),
                pygame.transform.scale(pygame.image.load(
                    os.path.join(IMAGE_PATH, "dog-2.png")), (60, 90)),
                pygame.transform.scale(pygame.image.load(
                    os.path.join(IMAGE_PATH, "dog-3.png")), (60, 90)),
                pygame.transform.scale(pygame.image.load(
                    os.path.join(IMAGE_PATH, "dog-4.png")), (60, 90)),
                pygame.transform.scale(pygame.image.load(
                    os.path.join(IMAGE_PATH, "dog-5.png")), (60, 90)),
                pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "dog-6.png")), (60, 90))]


CREW_IMAGE = [pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "crew-1.png")), (100, 150)),
                 pygame.transform.scale(pygame.image.load(
                     os.path.join(IMAGE_PATH, "crew-2.png")), (100, 150)),
                 pygame.transform.scale(pygame.image.load(
                     os.path.join(IMAGE_PATH, "crew-3.png")), (100, 150)),
                 pygame.transform.scale(pygame.image.load(
                     os.path.join(IMAGE_PATH, "crew-4.png")), (100, 150)),
                 pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "crew-5.png")), (100, 150))]

SHIP_IMAGE = [pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "ship-1.png")), (70, 120)),
           pygame.transform.scale(pygame.image.load(
               os.path.join(IMAGE_PATH, "ship-2.png")), (70, 120)),
           pygame.transform.scale(pygame.image.load(
               os.path.join(IMAGE_PATH, "ship-3.png")), (70, 120)),
           pygame.transform.scale(pygame.image.load(
               os.path.join(IMAGE_PATH, "ship-4.png")), (70, 120)),
           pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_PATH, "ship-5.png")), (70, 120))]


DOG_PUNCH_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "paw.png")), (50, 50))
CREW_PUNCH_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "hit.png")), (60, 60))
SHIP_PUNCH_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "collision.png")), (80, 80))
BRIAN_PUNCH_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "explosion.png")), (50, 50))


class Hero:
    def __init__(self, herotype, herolevel):
        self.hero_type = herotype
        self.herolevel = herolevel
        self.path = random.choice(hero_PATH)
        self.path_index = 0
        self.move_count = 0
        self.upgrade = [1, 1.3, 1.5, 1.5]
        self.stride = self.move_speed(self.hero_type)
        if self.hero_type == 'dog':
            self.image = self.hero_image(self.hero_type)[0]
        elif self.hero_type == 'crew':
            self.image = self.hero_image(self.hero_type)[0]
        elif self.hero_type == 'ship':
            self.image = self.hero_image(self.hero_type)[0]
        elif self.hero_type == 'brian':
            self.image = self.hero_image(self.hero_type)[0]
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.health = self.hero_hp_maxhp(self.hero_type) * self.upgrade[self.herolevel]
        self.max_health = self.hero_hp_maxhp(
            self.hero_type) * self.upgrade[self.herolevel]
        self.attack_count = 0
        self.attack_max_count = self.attack_max_cd(self.hero_type)
        self.power = self.hero_power(
            self.hero_type) * self.upgrade[self.herolevel]
        self.range = self.attack_range(self.hero_type)
        self.attack_music = self.hero_attacksound(self.hero_type)
        self.attack_light = 0
        self.attack_image = self.hero_attack_image(self.hero_type)
        self.attack_location_x = self.hero_attack_loactionx(self.hero_type)
        self.draw_atk_counter = 100

    def move(self):
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
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
            self.rect.center = self.path[self.path_index]

        if self.hero_type == 'dog':
            self.image = self.hero_image(self.hero_type)[
                self.move_count//6 % 6]
        elif self.hero_type == 'crew':
            self.image = self.hero_image(self.hero_type)[
                self.move_count//8 % 5]
        elif self.hero_type == 'ship':
            self.image = self.hero_image(self.hero_type)[
                self.move_count//8 % 5]
        elif self.hero_type == 'brian':
            self.image = self.hero_image(self.hero_type)[
                self.move_count//6 % 6]

    def attack(self):
        if(self.attack_count < self.attack_max_count):
            self.attack_count += 1
            return False
        else:
            self.attack_count = 0
            self.attack_music.set_volume(0.8)
            pygame.mixer.Channel(1).play(self.attack_music)
            return True

    # 不同英雄的圖片
    def hero_image(self, herotype):
        if(herotype == 'dog'):
            return DOG_IMAGE
        elif(herotype == 'crew'):
            return CREW_IMAGE
        elif(herotype == 'ship'):
            return SHIP_IMAGE

    # 攻擊圖

    def hero_attack_image(self, herotype):
        if(herotype == 'dog'):
            return DOG_PUNCH_IMAGE
        elif(herotype == 'crew'):
            return CREW_PUNCH_IMAGE
        elif(herotype == 'ship'):
            return SHIP_PUNCH_IMAGE


    # 攻擊圖的x偏差
    def hero_attack_loactionx(self, herotype):
        if(herotype == 'dog'):
            return 75
        elif(herotype == 'crew'):
            return 75
        elif(herotype == 'ship'):
            return 195
        elif(herotype == 'brian'):
            return 75

    # 攻擊聲音
    def hero_attacksound(self, herotype):
        if(herotype == 'dog'):
            return pygame.mixer.Sound(os.path.join(SOUND_PATH, "DogWolfBark.mp3"))
        elif(herotype == 'crew'):
            return pygame.mixer.Sound(os.path.join(SOUND_PATH, "PlayerSweepAttack.mp3"))
        elif(herotype == 'ship'):
            return pygame.mixer.Sound(os.path.join(SOUND_PATH, "longshot.mp3"))
        elif(herotype == 'brian'):
            return pygame.mixer.Sound(os.path.join(SOUND_PATH, "briansound.wav"))

    # 最大血量
    def hero_hp_maxhp(self, herotype):
        if(herotype == 'dog'):
            return 15
        elif(herotype == 'crew'):
            return 35
        elif(herotype == 'ship'):
            return 40


    # 攻擊力

    def hero_power(self, herotype):
        if(herotype == 'dog'):
            return 4
        elif(herotype == 'crew'):
            return 5
        elif(herotype == 'ship'):
            return 8


    # 移動速度

    def move_speed(self, herotype):
        if(herotype == 'dog'):
            return 3
        elif(herotype == 'crew'):
            return 2.5
        elif(herotype == 'ship'):
            return 2


    # 攻擊最大冷卻

    def attack_max_cd(self, herotype):
        if(herotype == 'dog'):
            return 65
        elif(herotype == 'crew'):
            return 80
        elif(herotype == 'ship'):
            return 100


    # 要不要攻擊
    def attack(self, model):
        if(self.attack_count < self.attack_max_count):
            self.attack_count += 1
            return False
        else:
            if model.score <= 1000 and model.mytower_hp > 0:
                self.attack_count = 0
                self.attack_music.set_volume(0.5)
                pygame.mixer.Channel(1).play(self.attack_music)
                return True

    # 攻擊距離
    def attack_range(self, herotype):
        if(herotype == 'dog'):
            return 60
        elif(herotype == 'crew'):
            return 40
        elif(herotype == 'ship'):
            return 180

    
    def arrive(self):
        x, y = self.rect.center
        en_tower_x, en_tower_y = (130, 410)
        distance = math.sqrt((x - en_tower_x) ** 2 + (y - en_tower_y) ** 2)
        # print(distance)

        if distance <= self.range:
            return True
        else:
            return False


class HeroGroup:
    def __init__(self):
        self.__reserved_members = []
        self.expedition = []

    def he_to_en_range(self, hero, enemy):
        x1, y1 = enemy.rect.center
        x2, y2 = hero.rect.center
        distance = math.sqrt((x2 - x1) ** 2)
        if distance <= hero.range:
            return True
        return False

    def he_to_base_range(self, hero):
        x1, y1 = hero.rect.center
        x2, y2 = en_BASE.center
        distance = math.sqrt((x2 - x1) ** 2)
        if distance <= hero.range:
            return True
        return False

    def advance(self, model):
        self.sort_list()
        for hero in self.expedition:
            if hero.health <= 0:
                self.retreat(hero)

            if self.he_to_base_range(hero):
                if hero.arrive() and model.entower_hp > 0:
                    model.score+=100
                    self.retreat(hero)
                    if hero.hero_type == "brian":
                        self.retreat(hero)
                elif model.entower_hp <= 0:
                    model.entower_hp = 0
                    hero.attack_light = 0
                else:
                    hero.attack_light = 0
                if hero.hero_type == "brian":
                    self.retreat(hero)

            elif model.en.expedition:
                for en in model.en.expedition:
                    # 自爆範圍攻擊
                    if self.he_to_en_range(hero, en) and hero.hero_type == "brian":
                        if(hero.attack(model)):
                            self.retreat(hero)
                            en.health -= hero.power
                            hero.attack_light = 1
                        else:
                            hero.attack_light = 0
                            break
                    # 單體攻擊
                    elif self.he_to_en_range(hero, en):
                        if(hero.attack(model)):
                            en.health -= hero.power
                            hero.attack_light = 1
                            break
                        else:
                            hero.attack_light = 0
                            break
                    else:
                        hero.attack_light = 0
                        hero.move()
                        break
            else:
                hero.attack_light = 0
                hero.move()

    def sort_list(self):
        for i in range(1, len(self.expedition)):
            if(self.expedition[i].rect.centerx < self.expedition[0].rect.centerx):
                temp = self.expedition[0]
                self.expedition[0] = self.expedition[i]
                self.expedition[i] = temp

    def add(self, herotype, herolevel):
        new_hero = None
        if herotype == 'dog':
            new_hero = Hero('dog', herolevel)
        elif herotype == 'crew':
            new_hero = Hero('crew', herolevel)
        elif herotype == 'ship':
            new_hero = Hero('ship', herolevel)
        if new_hero:
            self.expedition.append(new_hero)

    def get(self):
        """Get the enemy list"""
        return self.expedition

    def is_empty(self):
        """Return whether the enemy is empty (so that we can move on to next wave)"""
        return False if self.__reserved_members or self.expedition else True

    def retreat(self, hero):
        """Remove the enemy from the expedition"""
        self.expedition.remove(hero)
