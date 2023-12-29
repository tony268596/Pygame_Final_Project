import pygame
import os
from settings import game_status, WIN_WIDTH, WIN_HEIGHT, SOUND_PATH, user_info, LEVEL_FINISH_TIMES



# controller
class GameControl:
    def __init__(self, game_model, game_view):
        self.model = game_model
        self.view = game_view
        self.events = {"game quit": True,
                       "win": False,
                       "mouse position": [0, 0],
                       "keyboard key": 0,
                       }
        self.request = None  # response of user input

        self.animation_max_cd = 120
        self.animation_cd = 0

    def update_model(self):
        """update the model and the view here"""
        self.request = self.model.get_request(self.events)
        self.model.user_request(self.request)
        self.model.enemies_advance()
        self.model.heros_advance()
##
        self.model.event_advance()

    def receive_user_input(self):
        """receive user input from the events"""
        # event initialization
        self.events = {"game quit": True,
                       "win": False,
                       "mouse position": None,
                       "keyboard key": None
                       }
        self.winrect = pygame.Rect(0, 0, WIN_WIDTH, WIN_HEIGHT)
        # update event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events["game quit"] = False
            # player click action
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.events["mouse position"] = [x, y]
                if self.model.mytower_hp <= 0:
                    if self.winrect.collidepoint(x, y):
                        # write data into file once the player clicks,
                        # since there will be only one click for player to click,
                        # or it will keep writing same data into file.
                        # self.model.save_time()
                        print("click!")
                        game_status["go_level_menu"] = True
                        pygame.mixer.music.stop()
                        self.play_music_select()
                elif self.model.entower_hp <= 0 or self.model.score >= 1000:
                    if self.winrect.collidepoint(x, y):
                        print("click!")
                        game_status["go_level_menu"] = True
                        self.events["win"] = True
                        pygame.mixer.music.stop()
                        self.play_music_select()

        self.events["keyboard key"] = pygame.K_n
        if self.model.entower_hp <= 0 and self.model.mytower_hp > 0:
            self.events["win"] = True
            if len(user_info['user_used_time']) <= 10:
                # just in case the list wont be empty
                self.model.get_end_time()

    def money_counter(self):
        if(self.model.money_cd < self.model.money_max_cd):
            self.model.money_cd += 1
        else:
            self.model.money += 1
            self.model.money_cd = 0

    def update_view(self):
        # render background
        self.view.draw_bg()
        self.view.draw_mytower_hp(
            self.model.mytower_hp, self.model.mytower_max_hp)
        self.view.draw_entower_hp(
            self.model.entower_hp, self.model.entower_max_hp)
        self.view.draw_game_time(self.model.game_time())
        
        self.view.draw_event(self.model.ev)
        self.view.draw_enemies(self.model.enemies)
        self.view.draw_heros(self.model.heros)
        
        self.view.draw_money(self.model.money)
        self.view.draw_score(self.model.game_score())
        self.view.draw_data_ship()
        self.view.draw_data_dog()
        self.view.draw_data_crew()
        
        if LEVEL_FINISH_TIMES[0] != 0:
            self.view.draw_data_brian()
        else:
            self.view.draw_locked_brian()

        self.view.draw_skill_data()
        self.view.draw_upgrade_data()

        self.view.draw_attack_en(self.model.en.expedition)
        self.view.draw_attack_he(
            self.model.he.expedition, self.model.en.expedition, self.model.entower_hp)

        if(self.model.skill_animation == True):
            if(self.animation_cd <= self.animation_max_cd):
                self.view.draw_skill_animation()
                self.animation_cd += 1
            else:
                self.model.skill_animation = False
                self.animation_cd = 0

        if self.model.menu is not None:
            self.view.draw_menu(self.model.menu)

        if self.model.mytower_hp <= 0:
            self.view.draw_game_over()
        elif self.model.score >= 1000:
            self.view.draw_game_win()
        # elif self.model.score >= 1000 and self.model.checkpoint != 3:
        #     self.view.draw_game_win()
        # elif self.model.score >= 1000 and self.model.checkpoint == 3:
        #     self.view.draw_finish_win()

    def play_music_select(self):
        pygame.mixer.music.load(os.path.join(SOUND_PATH, "level_select_v0.mp3"))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    @property
    def quit_game(self):
        return self.events["game quit"]

    @property
    def win_or_not(self):
        return self.events["win"]
