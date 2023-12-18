import pygame
import os
from color_settings import *
from settings import WIN_WIDTH, WIN_HEIGHT, IMAGE_PATH, SOUND_PATH, FPS, game_status,LEVEL_FINISH_TIMES,music
from game.game import Game
from button import Buttons


pygame.init()
pygame.mixer.init()


class ChooseMenu:
    def __init__(self):
        # win
        self.menu_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        # background
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join(
            IMAGE_PATH, "level_background.png")), (WIN_WIDTH, WIN_HEIGHT))
        #title and button
        self.title_image = pygame.transform.scale(pygame.image.load(
            os.path.join(IMAGE_PATH, "choose.png")), (220, 80))
        self.level1_image = pygame.transform.scale(pygame.image.load(
            os.path.join(IMAGE_PATH, "level_1.png")), (150, 80))
        self.level2_image = pygame.transform.scale(pygame.image.load(
            os.path.join(IMAGE_PATH, "level_2.png")), (150, 80))
        self.level3_image = pygame.transform.scale(pygame.image.load(
            os.path.join(IMAGE_PATH, "level_3.png")), (150, 80))
        self.back_image = pygame.transform.scale(
            pygame.image.load(os.path.join(IMAGE_PATH, "back.png")), (80, 80))
        self.back_image = pygame.transform.scale(
            pygame.image.load(os.path.join(IMAGE_PATH, "back.png")), (80, 80))
        self.lock_image = pygame.transform.scale(
            pygame.image.load(os.path.join(IMAGE_PATH, "lock.png")), (80, 80))
        # button
        self.level1_btn = Buttons(437, 180, 150, 80)  # x, y, width, height
        self.level2_btn = Buttons(437, 300, 150, 80)
        self.level3_btn = Buttons(437, 420, 150, 80)
        self.back_btn = Buttons(5, 5, 80, 80)
        if LEVEL_FINISH_TIMES[0] == 0:
            self.buttons = [self.level1_btn,
                            self.back_btn]
        elif LEVEL_FINISH_TIMES[0] != 0:
            self.buttons = [self.level1_btn,
                            self.level2_btn,
                            self.back_btn]
        elif LEVEL_FINISH_TIMES[1] != 0:
            self.buttons = [self.level1_btn,
                            self.level2_btn,
                            self.level3_btn,
                            self.back_btn]

    def back_or_not(self, x, y):
        if self.back_btn.clicked(x, y):
            return True
        return False

    def unlock(self, button):
        self.buttons.append(button)

    def play_music(self):
        pygame.mixer.music.load(os.path.join(SOUND_PATH, "menu1.mp3"))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def play_music_one(self):
        pygame.mixer.music.load(os.path.join(SOUND_PATH, "level1_bgm.mp3"))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def play_music_two(self):
        pygame.mixer.music.load(os.path.join(SOUND_PATH, "level2_bgm.mp3"))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def play_music_three(self):
        pygame.mixer.music.load(os.path.join(SOUND_PATH, "boss_bgm.mp3"))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        
    def play_music_select(self):
        pygame.mixer.music.load(os.path.join(SOUND_PATH, "level_select.mp3"))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

    def mute(self):
        if music["mute"]:
            pygame.mixer.music.pause()

    def run(self):
        pygame.mixer.music.stop()
        self.play_music_select()
        clock = pygame.time.Clock()
        while game_status["run"] and not game_status["go_input_window"] and not game_status["go_start_menu"]:
            game_status["go_level_menu"] = False
            self.mute()

            clock.tick(FPS)
            self.menu_win.blit(self.bg, (0, 0))
            self.menu_win.blit(self.title_image, (402, 30))
            self.menu_win.blit(self.level1_image, (437, 180))
            self.menu_win.blit(self.level2_image, (437, 300))
            self.menu_win.blit(self.level3_image, (437, 420))
            game = Game()
            transparent_surface = pygame.Surface(
                self.menu_win.get_size(), pygame.SRCALPHA)  # 製作畫布
            transparency = 180
            # 破關鎖定
            if LEVEL_FINISH_TIMES[0] == 0:
                pygame.draw.rect(transparent_surface, (0, 0, 0, transparency), [
                    437, 300, 150, 80], 0)
                pygame.draw.rect(transparent_surface, (0, 0, 0, transparency), [
                    437, 420, 150, 80], 0)
                self.menu_win.blit(transparent_surface, (0, 0))
                self.menu_win.blit(self.lock_image, (472, 295))
                self.menu_win.blit(self.lock_image, (472, 415))
            elif LEVEL_FINISH_TIMES[0] != 0 and LEVEL_FINISH_TIMES[1] == 0:
                self.unlock(self.level2_btn)
                pygame.draw.rect(transparent_surface, (0, 0, 0, transparency), [
                    437, 420, 150, 80], 0)
                self.menu_win.blit(transparent_surface, (0, 0))
                self.menu_win.blit(self.lock_image, (472, 415))
            elif LEVEL_FINISH_TIMES[1] != 0:
                self.unlock(self.level3_btn)

            self.menu_win.blit(self.back_image, (5, 5))
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                # quit
                if event.type == pygame.QUIT:
                    game_status["run"] = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # check if hit start btn
                    if self.level1_btn.clicked(x, y):
                        pygame.mixer.music.stop()
                        self.play_music_one()
                        self.mute()
                        game.run(1)
                    elif self.level2_btn.clicked(x, y) and LEVEL_FINISH_TIMES[0] != 0:
                        pygame.mixer.music.stop()
                        self.play_music_two()
                        self.mute()
                        game.run(2)
                    elif self.level3_btn.clicked(x, y) and LEVEL_FINISH_TIMES[1] != 0:
                        pygame.mixer.music.stop()
                        self.play_music_three()
                        self.mute()
                        game.run(3)

                    if self.back_or_not(x, y):
                        pygame.mixer.music.stop()
                        self.play_music_select()
                        #self.mute()
                        game_status["go_input_window"] = True
            for bt in self.buttons:
                x, y = pygame.mouse.get_pos()
                bt.create_frame(x, y)
                bt.draw_frame(self.menu_win)

            pygame.display.update()



