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


class Hero_howhow:
    def __init__(self, subject):
        subject.register(self)
        self.howhow_music = pygame.mixer.Sound(os.path.join(SOUND_PATH,"dog1a.mp3"))
    def update(self, user_request: str, model):
        if user_request == "howhow":
            if model.money >= 5:
                model.money -= 5
                model.heros.add('howhow', model.hero_level)
                self.howhow_music.set_volume(0.4)
                pygame.mixer.Channel(2).play(self.howhow_music)
                print('summon howhow')

class Hero_godtone:
    def __init__(self, subject):
        subject.register(self)
        self.godtone_music = pygame.mixer.Sound(os.path.join(SOUND_PATH,"run1.mp3"))
    def update(self, user_request: str, model):
        if user_request == "godtone":
            if model.money >= 10:
                model.money -= 10
                model.heros.add("godtone", model.hero_level)
                self.godtone_music.set_volume(0.3)
                pygame.mixer.Channel(2).play(self.godtone_music)
                print('summon godtone')


class Hero_p:
    def __init__(self, subject):
        subject.register(self)
        self.p_music = pygame.mixer.Sound(os.path.join(SOUND_PATH,"boat_engine.mp3"))
    def update(self, user_request: str, model):
        if user_request == "p":
            if model.money >= 20:
                model.money -= 20
                model.heros.add("p", model.hero_level)
                self.p_music.set_volume(0.8)
                pygame.mixer.Channel(2).play(self.p_music)
                print('summon p')

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
                                


