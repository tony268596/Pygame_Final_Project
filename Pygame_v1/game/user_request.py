import pygame
from settings import SOUND_PATH, skill_PATH
import os

class RequestSubject:
    def __init__(self, model):
        self.__observers = []
        self.model = model

    def register(self, observer):
        self.__observers.append(observer)

    def notify(self, user_request):
        for o in self.__observers:
            o.update(user_request, self.model)


class EnemyGenerator:
    def __init__(self, subject):
        subject.register(self)
        self.cd = 900
        self.max_cd = 900
        self.boss_generate_flag = 1

    def update(self, user_request: str, model):
        if(self.cd >= self.max_cd and user_request == "start new wave"):
            if model.checkpoint == 1 or model.checkpoint == 2:
                model.enemies.add(self.en_num(model.checkpoint),model)
                self.cd = 0
            elif model.checkpoint == 3 and self.boss_generate_flag == 1:
                model.enemies.add(self.en_num(model.checkpoint),model)
                self.cd = 0
                self.boss_generate_flag = 0
        else:
            self.cd += 1
            
    def en_num(self, checkpoint):
        if checkpoint == 1:
            return 3
        elif checkpoint == 2:
            return 4
        else:
            return 1
        


class Music:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "music":
            pygame.mixer.music.unpause()
            model.sound.play()


class Muse:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        if user_request == "mute":
            pygame.mixer.music.pause()
            model.sound.play()


class Hero_dog:
    def __init__(self, subject):
        subject.register(self)
        self.dog_music = pygame.mixer.Sound(os.path.join(SOUND_PATH,"dog1a.mp3"))
    def update(self, user_request: str, model):
        if user_request == "dog":
            if model.money >= 25:
                model.money -= 25
                model.heros.add('dog', model.hero_level)
                self.dog_music.set_volume(0.4)
                pygame.mixer.Channel(2).play(self.dog_music)
                print('summon dog')

class Hero_crew:
    def __init__(self, subject):
        subject.register(self)
        self.crew_music = pygame.mixer.Sound(os.path.join(SOUND_PATH,"run1.mp3"))
    def update(self, user_request: str, model):
        if user_request == "crew":
            if model.money >= 50:
                model.money -= 50
                model.heros.add("crew", model.hero_level)
                self.crew_music.set_volume(0.3)
                pygame.mixer.Channel(2).play(self.crew_music)
                print('summon crew')


class Hero_ship:
    def __init__(self, subject):
        subject.register(self)
        self.ship_music = pygame.mixer.Sound(os.path.join(SOUND_PATH,"boat_engine.mp3"))
    def update(self, user_request: str, model):
        if user_request == "ship":
            if model.money >= 100:
                model.money -= 100
                model.heros.add("ship", model.hero_level)
                self.ship_music.set_volume(0.8)
                pygame.mixer.Channel(2).play(self.ship_music)
                print('summon ship')

class Hero_brian:
    def __init__(self, subject):
        subject.register(self)
        self.brian_music = pygame.mixer.Sound(os.path.join(SOUND_PATH,"brian_sound.mp3"))
    def update(self, user_request: str, model):
        if user_request == "brian":
            if model.money >= 70:
                model.money -= 70
                model.heros.add("brian", model.hero_level)
                self.brian_music.set_volume(0.4)
                pygame.mixer.Channel(2).play(self.brian_music)
                print('summon brian')




class Special:
    def __init__(self, subject):
        subject.register(self)
        self.skill_music = pygame.mixer.Sound(os.path.join(SOUND_PATH,"rising.mp3"))
    def update(self, user_request: str, model):
        if user_request == "special" and model.en.expedition:
            if model.money >= 200:
                model.money -= 200
                model.skill_animation = True
                self.skill_music.set_volume(0.6)
                pygame.mixer.Channel(3).play(self.skill_music)
                for en in model.en.expedition:
                    en.health = en.health // 2


class Upgrade:
    def __init__(self, subject):
        subject.register(self)
        self.upgrade_music = pygame.mixer.Sound(os.path.join(SOUND_PATH,"upgradesound.wav"))
    def update(self, user_request: str, model):
        hero_update_cost = [100, 150, 200]
        if user_request == "upgrade":
            if model.money >= hero_update_cost[model.hero_level] and model.hero_level < 3:
                model.money -= hero_update_cost[model.hero_level]
                self.upgrade_music.set_volume(0.6)
                pygame.mixer.Channel(3).play(self.upgrade_music)
                                


