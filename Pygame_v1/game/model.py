import pygame
import os
from enemy.enemies import EnemyGroup
from hero import HeroGroup
from menu.menus import MainMenu
from game.user_request import RequestSubject, EnemyGenerator, Muse, Music, Hero_howhow, Hero_godtone, Hero_p, Hero_brian, Special, Upgrade
from settings import WIN_WIDTH, WIN_HEIGHT, BACKGROUND_IMAGE, BACKGROUND_IMAGE_two, BACKGROUND_IMAGE_three, user_info, RECORD_PATH, SOUND_PATH
from hero import HeroGroup


class GameModel:
    def __init__(self, checkpoint):
        # data
        self.checkpoint = checkpoint
        self.bg_image = self.bg(self.checkpoint)
        self.hero_level = 0
        self.__enemies = EnemyGroup(self.checkpoint)
        self.en = self.__enemies
        self.__heros = HeroGroup()
        self.he = self.__heros
        self.__menu = None
        self.__main_menu = MainMenu()
        self.selected_button = None
        self.subject = RequestSubject(self)
        self.generator = EnemyGenerator(self.subject)
        self.muse = Muse(self.subject)
        self.music = Music(self.subject)
        self.hero_howhow = Hero_howhow(self.subject)
        self.hero_godtone = Hero_godtone(self.subject)
        self.hero_p = Hero_p(self.subject)
        if self.checkpoint != 1:
            self.hero_brian = Hero_brian(self.subject)
        self.special = Special(self.subject)
        self.upgrade = Upgrade(self.subject)
        self.money = self.initial_money(self.checkpoint)
        self.mytower_max_hp = self.en_and_our_tower_hp(self.checkpoint)
        self.mytower_hp = self.mytower_max_hp
        self.entower_max_hp = self.en_and_our_tower_hp(self.checkpoint)
        self.entower_hp = self.entower_max_hp
        self.sound = pygame.mixer.Sound(
            os.path.join(SOUND_PATH, "start.wav")).set_volume(0.1)
        self.money_cd = 0
        self.money_max_cd = 5
        self.skill_animation = False
        self.user_name = user_info['user_name']
        # whenever game init, there will be a time
        self.start_time = pygame.time.get_ticks()
        self.score = 0

    def game_time(self):
        # time now minus time game start to show time used
        self.time_from_start = pygame.time.get_ticks() - self.start_time
        return round(self.time_from_start/1000, 2)

    def get_end_time(self):
        '''its already under self.model.entower_hp <= 0 condition in game control'''
        self.end_time = (pygame.time.get_ticks() - self.start_time) / 1000
        user_info['user_used_time'].append(self.end_time)

    def save_time(self):
        txt_list = ['records.txt', 'records2.txt', 'records3.txt']
        if len(user_info['user_used_time']) > 0:
            time = user_info['user_used_time'][0]

            if self.entower_hp <= 0:
                # 絕對路徑！
                with open(os.path.join(RECORD_PATH, txt_list[self.checkpoint-1]), 'a') as file:
                    text = f"{self.user_name}--{time}\n"
                    file.write(text)
                # whenever done input to file, clear the list
                user_info['user_used_time'] = []

    def en_and_our_tower_hp(self, checkpoint):
        if checkpoint == 1:
            return 70
        elif checkpoint == 2:
            return 85
        elif checkpoint == 3:
            return 100

    def bg(self, checkpoint):
        if checkpoint == 1:
            return pygame.transform.scale(BACKGROUND_IMAGE, (WIN_WIDTH, WIN_HEIGHT))
        elif checkpoint == 2:
            return pygame.transform.scale(BACKGROUND_IMAGE_two, (WIN_WIDTH, WIN_HEIGHT))
        elif checkpoint == 3:
            return pygame.transform.scale(BACKGROUND_IMAGE_three, (WIN_WIDTH, WIN_HEIGHT))

    def initial_money(self, checkpoint):
        if checkpoint == 1:
            return 100
        elif checkpoint == 2:
            return 150
        elif checkpoint == 3:
            return 200

    def user_request(self, user_request: str):
        """ add tower, sell tower, upgrade tower"""
        self.subject.notify(user_request)

    def get_request(self, events: dict) -> str:
        """get keyboard response or button response"""
        # initial
        self.selected_button = None
        # mouse event
        if events["mouse position"] is not None:
            x, y = events["mouse position"]
            self.select(x, y)
            if self.selected_button is not None:
                return self.selected_button.response
            return "nothing"

        if events["keyboard key"] is not None:
            return "start new wave"
        return "nothing"

    def select(self, mouse_x: int, mouse_y: int) -> None:
        if self.__menu is not None:
            for btn in self.__menu.buttons:
                if btn.clicked(mouse_x, mouse_y):
                    self.selected_button = btn
            if self.selected_button is None:
                self.selected_tower = None
        # menu btn
        for btn in self.__main_menu.buttons:
            if btn.clicked(mouse_x, mouse_y):
                self.selected_button = btn

    def enemies_advance(self):
        self.__enemies.advance(self)

    def heros_advance(self):
        self.__heros.advance(self)
    
    def game_score(self):
        return self.score


    @property
    def enemies(self):
        return self.__enemies

    @property
    def heros(self):
        return self.__heros

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, new_menu):
        self.__menu = new_menu
