import pygame
import math
import os
from settings import en_PATH, hero_BASE
from color_settings import *
from settings import IMAGE_PATH,SOUND_PATH
import random

pygame.init()
ENEMY_IMAGE_1 = pygame.image.load(os.path.join(IMAGE_PATH, "Crocodile-0.png"))
ENEMY_IMAGE_2 = pygame.image.load(os.path.join(IMAGE_PATH, "pirate-0.png"))
ENEMY_IMAGE_3 = pygame.image.load(os.path.join(IMAGE_PATH, "wood.png"))


class Enemy:
    def __init__(self, checkpoint):
        self.point = checkpoint
        self.en_type = self.type_en(self.point)                             
        self.image = self.enemy_image(self.en_type)
        self.health = self.enemy_hp_maxhp(self.en_type, self.point)
        self.max_health = self.health
        self.power = self.enemy_power(self.en_type, self.point)
        self.stride = self.move_speed(self.en_type, self.point)
        self.path = random.choice(en_PATH)
        self.move_count = 0
        self.path_index = 0
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.attack_count = 0
        self.attack_max_count = self.attack_max_cd(self.en_type)
        self.range = self.attack_range(self.en_type)
        self.attack_music = pygame.mixer.Sound(os.path.join(SOUND_PATH,"short_punch1.mp3"))
        self.attack_light = 0
        
        
    def type_en(self, point):
        #if point == 1 or point == 2:
        return random.randint(1, 3)
        # elif point == 3:
        #     return 5

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
            self.path_index += 1
            self.rect.center = self.path[self.path_index]
            
    # 不同敵人的圖片
    def enemy_image(self, entype):
        if(entype == 1):
            return pygame.transform.scale(ENEMY_IMAGE_1, (80, 80))
        elif(entype == 2):
            return pygame.transform.scale(ENEMY_IMAGE_2, (120, 120))
        elif(entype == 3):
            return pygame.transform.scale(ENEMY_IMAGE_3, (120, 120))
        # elif(entype == 4):
        #     return pygame.transform.scale(ENEMY_IMAGE_4, (120, 120))
        # elif(entype == 5):
        #     return pygame.transform.scale(ENEMY_IMAGE_5, (250, 250))
        
    # 最大血量
    def enemy_hp_maxhp(self, entype, point):     
        if(entype == 1):
            entype_one_hp = [15, 20]
            if(point == 1):
                return entype_one_hp[0]
            elif(point == 2):
                return entype_one_hp[1]
        elif(entype == 2):
            entype_two_hp = [15, 15]
            if(point == 1):
                return entype_two_hp[0]
            elif(point == 2):
                return entype_two_hp[1]
        elif(entype == 3):
            entype_three_hp = [10, 18]
            if(point == 1):
                return entype_three_hp[0]
            elif(point == 2):
                return entype_three_hp[1]
        # elif(entype == 4):
        #     return 50
        # elif(entype == 5):
        #     return 250
        
    # 攻擊力    
    def enemy_power(self, entype, point):
        if(entype == 1):
            entype_one_power = [10, 5]
            if(point == 1):
                return entype_one_power[0]
            elif(point == 2):
                return entype_one_power[1]
        elif(entype == 2):
            entype_two_power = [12, 8]
            if(point == 1):
                return entype_two_power[0]
            elif(point == 2):
                return entype_two_power[1]
        elif(entype == 3):
            entype_three_power = [8, 4]
            if(point == 1):
                return entype_three_power[0]
            elif(point == 2):
                return entype_three_power[1]
        # elif(entype == 4):
        #     return 50
        # elif(entype == 5):
        #     return 999
        
    # 移動速度    
    def move_speed(self, entype, point):
        if(entype == 1):
            entype_one_speed = [2, 1.2]
            if(point == 1):
                return entype_one_speed[0]
            elif(point == 2):
                return entype_one_speed[1]
        elif(entype == 2):
            entype_two_speed = [1.5, 0.8]
            if(point == 1):
                return entype_two_speed[0]
            elif(point == 2):
                return entype_two_speed[1]
        elif(entype == 3):
            entype_three_speed = [2.2, 1.8]
            if(point == 1):
                return entype_three_speed[0]
            elif(point == 2):
                return entype_three_speed[1]
        # elif(entype == 4):
        #     return 0.2
        # elif(entype == 5):
        #     return 0.15
        
    # 攻擊最大冷卻    
    def attack_max_cd(self, entype):
        if(entype == 1):
            return 100
        elif(entype == 2):
            return 170
        elif(entype == 3):
            return 70
        # elif(entype == 4):
        #     return 600
        # elif(entype == 5):
        #     return 150
        
    # 要不要攻擊
    def attack(self,model):
        if(self.attack_count < self.attack_max_count):
            self.attack_count += 1
            return False
        else:
            if model.mytower_hp > 0 and model.entower_hp > 0:
                self.attack_count = 0
                self.attack_music.set_volume(0.5)
                pygame.mixer.Channel(1).play(self.attack_music)
                return True
   
    # 攻擊範圍
    def attack_range(self, entype):
        if(entype == 1):
            return 60
        elif(entype == 2):
            return 150
        elif(entype == 3):
            return 90
        elif(entype == 4):
            return 60
        elif(entype == 5):
            return 60
        
        
class EnemyGroup:
    def __init__(self, checkpoint):
        self.campaign_count = 0
        self.campaign_max_count = 60   
        self.__reserved_members = []
        self.expedition = []
        self.point = checkpoint
    
    # 判斷英雄有沒有在敵人的攻擊範圍裡
    def en_to_hero_range(self, hero, enemy):
        x1, y1 = enemy.rect.center
        x2, y2 = hero.rect.center
        distance = math.sqrt((x2 - x1) ** 2 )
        if distance <= enemy.range:
            return True
        return False
    
    def en_to_base_range(self, enemy):
        x1, y1 = enemy.rect.center
        x2, y2 = hero_BASE.center
        distance = math.sqrt((x2 - x1) ** 2)
        if distance <= enemy.range:
            return True
        return False
    

    def advance(self, model):
        self.campaign()
        self.sort_list()
        for en in self.expedition:
            if en.health <= 0:
                model.money += 25
                self.retreat(en)
            if self.en_to_base_range(en):
                if en.attack(model) and model.mytower_hp > 0:
                    model.mytower_hp -= en.power
                    en.attack_light = 0
                elif model.mytower_hp <= 0:
                    model.entower_hp = 0
                    en.attack_light = 0
                else:
                    en.attack_light = 0
            elif model.he.expedition:
                for he in model.he.expedition:
                    if self.en_to_hero_range(he, en):
                        if(en.attack(model)):
                            he.health -= en.power
                            en.attack_light = 0
                            break
                        else:
                            en.attack_light = 0
                            break
                    else:
                        en.move()
                        en.attack_light = 0
                        break
            else:
                en.attack_light = 0
                en.move()

    def campaign(self):
        if self.campaign_count > self.campaign_max_count and self.__reserved_members:
            self.expedition.append(self.__reserved_members.pop())
            self.campaign_count = 0
        else:
            self.campaign_count += 1

    def add(self, num, model):
        if model.entower_hp > 0 and model.entower_hp > 0:
            self.__reserved_members = [Enemy(self.point) for _ in range(num)]

    def get(self):
        return self.expedition
    
    def sort_list(self):
        for i in range(1, len(self.expedition)):
            if(self.expedition[i].rect.centerx > self.expedition[0].rect.centerx):
                temp = self.expedition[0]
                self.expedition[0] = self.expedition[i] 
                self.expedition[i] = temp
        

    def retreat(self, enemy):
        self.expedition.remove(enemy)
