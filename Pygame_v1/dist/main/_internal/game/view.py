import pygame
from settings import WIN_WIDTH, WIN_HEIGHT, BACKGROUND_IMAGE, BACKGROUND_IMAGE_two, BACKGROUND_IMAGE_three, BLACK, HEALTH_WIDTH, HEALTH_HEIGHT, FPS, IMAGE_PATH, skill_PATH
from color_settings import *
import os
import math
import random

arial = pygame.font.match_font('arial')

# background images
bg_one = pygame.transform.scale(
    BACKGROUND_IMAGE, (WIN_WIDTH, WIN_HEIGHT))
bg_two = pygame.transform.scale(
    BACKGROUND_IMAGE_two, (WIN_WIDTH, WIN_HEIGHT))
bg_three = pygame.transform.scale(
    BACKGROUND_IMAGE_three, (WIN_WIDTH, WIN_HEIGHT))

# hero images
ship_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "ship_btn.png")), (80, 80))
crew_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "crew_btn.png")), (80, 80))
dog_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "dog_btn.png")), (80, 80))
locked_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "locked.png")), (80, 80))

# Update new hero images
dog_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "dog_btn.png")), (80, 80))
ship_button_image_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "ship_btn.png")), (80, 80))
crew_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "crew_btn.png")), (80, 80))


# tower base images
en_base_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "en_tower.png")), (200, 200))
hero_base_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "home_tower.png")), (200, 200))

# skills button images
UPGRADE_BTN_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "upgrade_btn.png")), (80, 80))
# SPECIAL_SKILL_BTN_IMAGE = pygame.transform.scale(
#     pygame.image.load(os.path.join(IMAGE_PATH, "skill.png")), (160, 50))
SCORE_LOG_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "score.png")), (160, 50))

# event images
tsunami_sea_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "sea_0.png")), (1024, 600))
tsunami_wave_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "tsunami_2.png")), (1024, 600))

# in-game status images
MONEY_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join(IMAGE_PATH, "coin.png")), (220, 80))
game_loss_image = pygame.transform.scale(pygame.image.load(
    os.path.join(IMAGE_PATH, "game_over_ground.png")), (1024, 600))
game_win_image = pygame.transform.scale(pygame.image.load(
    os.path.join(IMAGE_PATH, "win_background.png")), (1024, 600))


# Clock status image
clock_status_image = pygame.transform.scale(pygame.image.load(
    os.path.join(IMAGE_PATH, "hourglass.png")), (220, 80))

####
en_attack_image = pygame.transform.scale(
                    pygame.image.load(os.path.join(IMAGE_PATH, "broken-heart.png")), (60, 60))

class GameView:
    def __init__(self, checkpoint):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.point = checkpoint
        # use for skill animation
        # self.skill_move_path = skill_PATH
        self.path_index = 0
        self.move_count = 0
        self.stride = 5
        # self.rect = self.skillimage.get_rect()
        # self.rect.center = self.skill_move_path[self.path_index]

    def draw_bg(self):
        '''draw background & and all needed images according to checkpoint'''
        if(self.point == 1):
            self.win.blit(bg_one, (0, 0))
        elif(self.point == 2):
            self.win.blit(bg_two, (0, 0))
        elif(self.point == 3):
            self.win.blit(bg_three, (0, 0))
        heromenu_background = pygame.Surface((WIN_WIDTH, 100), pygame.SRCALPHA)
        heromenu_background.fill((0, 0, 0, 64))
        self.win.blit(heromenu_background, (0, WIN_HEIGHT - 100))
        self.win.blit(ship_button_image, (315, 510))
        self.win.blit(crew_button_image, (435, 510))
        self.win.blit(dog_button_image, (555, 510))
        self.win.blit(SCORE_LOG_IMAGE,(WIN_WIDTH/2 - 80, 0))
        self.win.blit(en_base_image, (0, 280))
        self.win.blit(hero_base_image, (875, 300))
        

        ''' btn of upgrade '''
        self.win.blit(UPGRADE_BTN_IMAGE, (675, 510))

    def draw_enemies(self, enemies):
        for en in enemies.get():
            if(en.en_type == 1):
                # 改敵人大小的話，記得改敵人blit的位置(y)
                self.win.blit(en.image, (en.rect.x, en.rect.y - 25))
                # draw health bar
                bar_width = en.rect.w * (en.health / en.max_health)
                max_bar_width = en.rect.w
                bar_height = 5
                # 改敵人大小的話，記得改血條blit的位置(y)
                ##
                pygame.draw.rect(
                    self.win, BLACK, [en.rect.x-1, en.rect.y - 35-1, max_bar_width+2, bar_height+2])
                ##
                pygame.draw.rect(
                    self.win, WHITE, [en.rect.x, en.rect.y - 35, max_bar_width, bar_height])
                pygame.draw.rect(self.win, RED, [
                                 en.rect.x, en.rect.y - 35, bar_width, bar_height])

            elif(en.en_type == 2):
                # 改敵人大小的話，記得改敵人blit的位置(y)
                self.win.blit(en.image, (en.rect.x, en.rect.y - 25))
                # draw health bar
                bar_width = en.rect.w * (en.health / en.max_health)
                max_bar_width = en.rect.w
                bar_height = 5
                # 改敵人大小的話，記得改血條blit的位置(y)
                ##
                pygame.draw.rect(
                    self.win, BLACK, [en.rect.x-1, en.rect.y - 35-1, max_bar_width+2, bar_height+2])
                ##
                pygame.draw.rect(
                    self.win, WHITE, [en.rect.x, en.rect.y - 35, max_bar_width, bar_height])
                pygame.draw.rect(self.win, RED, [
                                 en.rect.x, en.rect.y - 35, bar_width, bar_height])

            elif(en.en_type == 3):
                # 改敵人大小的話，記得改敵人blit的位置(y)
                self.win.blit(en.image, (en.rect.x, en.rect.y - 50))
                # draw health bar
                bar_width = en.rect.w * (en.health / en.max_health)
                max_bar_width = en.rect.w
                bar_height = 5
                # 改敵人大小的話，記得改血條blit的位置(y)
                ##
                pygame.draw.rect(
                    self.win, BLACK, [en.rect.x-1, en.rect.y - 45-1, max_bar_width+2, bar_height+2])
                ##
                pygame.draw.rect(
                    self.win, WHITE, [en.rect.x, en.rect.y - 45, max_bar_width, bar_height])
                pygame.draw.rect(self.win, RED, [
                                 en.rect.x, en.rect.y - 45, bar_width, bar_height])

            elif(en.en_type == 4):
                # 改敵人大小的話，記得改敵人blit的位置(y)
                self.win.blit(en.image, (en.rect.x, en.rect.y - 45))
                # draw health bar
                bar_width = en.rect.w * (en.health / en.max_health)
                max_bar_width = en.rect.w
                bar_height = 5
                # 改敵人大小的話，記得改血條blit的位置(y)
                ##
                pygame.draw.rect(
                    self.win, BLACK, [en.rect.x-1, en.rect.y - 55-1, max_bar_width+2, bar_height+2])
                ##
                pygame.draw.rect(
                    self.win, RED, [en.rect.x, en.rect.y - 55, max_bar_width, bar_height])
                pygame.draw.rect(self.win, GREEN, [
                                 en.rect.x, en.rect.y - 55, bar_width, bar_height])

            elif(en.en_type == 5):
                # 改敵人大小的話，記得改敵人blit的位置(y)
                self.win.blit(en.image, (en.rect.x, en.rect.y - 100))
                # draw health bar
                bar_width = en.rect.w * (en.health / en.max_health)
                max_bar_width = en.rect.w
                bar_height = 5
                # 改敵人大小的話，記得改血條blit的位置(y)
                ##
                pygame.draw.rect(
                    self.win, BLACK, [en.rect.x-1, en.rect.y - 100-1, max_bar_width+2, bar_height+2])
                ##
                pygame.draw.rect(
                    self.win, RED, [en.rect.x, en.rect.y - 100, max_bar_width, bar_height])
                pygame.draw.rect(self.win, GREEN, [
                                 en.rect.x, en.rect.y - 100, bar_width, bar_height])

    def draw_heros(self, heros):
        for hero in heros.get():
            self.win.blit(hero.image, hero.rect)
            # draw health bar
            bar_width = hero.rect.w * (hero.health / hero.max_health)
            max_bar_width = hero.rect.w
            bar_height = 5
            ##
            pygame.draw.rect(self.win, BLACK, [
                             hero.rect.x-1, hero.rect.y - 10-1, bar_width+2, bar_height+2])
            ##
            pygame.draw.rect(
                self.win, WHITE, [hero.rect.x, hero.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(self.win, BLUE, [
                             hero.rect.x, hero.rect.y - 10, bar_width, bar_height])

    def draw_event(self, ev):
        self.win.blit(ev.image, ev.rect)   
        #print("draw ev")

    def draw_data_ship(self):
        x, y = pygame.mouse.get_pos()
        ship_btn_rect = ship_button_image.get_rect()
        ship_btn_rect.center = (355, 550)
        if(ship_btn_rect.collidepoint(x, y)):
            ship_data = pygame.Surface((130, 105), pygame.SRCALPHA)
            ship_data.fill((0, 0, 0, 170))
            self.win.blit(ship_data, (310, 390))

            Topic = pygame.font.Font(arial, 22)
            Topic_text = Topic.render("Initial ability", True, WHITE)
            self.win.blit(Topic_text, (315, 390))

            HP = pygame.font.Font(arial, 20)
            HP_text = HP.render(" HP = 40", True, WHITE)
            self.win.blit(HP_text, (310, 410))

            Power = pygame.font.Font(arial, 20)
            Power_text = Power.render(" Power = 8", True, WHITE)
            self.win.blit(Power_text, (310, 430))

            Attack_range = pygame.font.Font(arial, 20)
            Attack_range_text = Attack_range.render(
                " Range = 180", True, WHITE)
            self.win.blit(Attack_range_text, (310, 450))

            Cost = pygame.font.Font(arial, 20)
            Cost_text = Cost.render(" Cost = 40", True, WHITE)
            self.win.blit(Cost_text, (310, 470))

    def draw_data_dog(self):
        x, y = pygame.mouse.get_pos()
        dog_btn_rect = dog_button_image.get_rect()
        dog_btn_rect.center = (595, 550)
        if(dog_btn_rect.collidepoint(x, y)):
            dog_data = pygame.Surface((130, 105), pygame.SRCALPHA)
            dog_data.fill((0, 0, 0, 170))
            self.win.blit(dog_data, (550, 390))

            Topic = pygame.font.Font(arial, 22)
            Topic_text = Topic.render("Initial ability", True, WHITE)
            self.win.blit(Topic_text, (555, 390))

            HP = pygame.font.Font(arial, 20)
            HP_text = HP.render(" HP = 15", True, WHITE)
            self.win.blit(HP_text, (550, 410))

            Power = pygame.font.Font(arial, 20)
            Power_text = Power.render(" Power = 4", True, WHITE)
            self.win.blit(Power_text, (550, 430))

            Attack_range = pygame.font.Font(arial, 20)
            Attack_range_text = Attack_range.render(" Range = 60", True, WHITE)
            self.win.blit(Attack_range_text, (550, 450))

            Cost = pygame.font.Font(arial, 20)
            Cost_text = Cost.render(" Cost = 25", True, WHITE)
            self.win.blit(Cost_text, (550, 470))

    def draw_data_crew(self):
        x, y = pygame.mouse.get_pos()
        crew_btn_rect = crew_button_image.get_rect()
        crew_btn_rect.center = (475, 550)
        if(crew_btn_rect.collidepoint(x, y)):
            crew_data = pygame.Surface((130, 105), pygame.SRCALPHA)
            crew_data.fill((0, 0, 0, 170))
            self.win.blit(crew_data, (430, 390))

            Topic = pygame.font.Font(arial, 22)
            Topic_text = Topic.render("Initial ability", True, WHITE)
            self.win.blit(Topic_text, (433, 390))

            HP = pygame.font.Font(arial, 20)
            HP_text = HP.render(" HP = 35", True, WHITE)
            self.win.blit(HP_text, (433, 410))

            Power = pygame.font.Font(arial, 20)
            Power_text = Power.render(" Power = 5", True, WHITE)
            self.win.blit(Power_text, (433, 430))

            Attack_range = pygame.font.Font(arial, 20)
            Attack_range_text = Attack_range.render(" Range = 40", True, WHITE)
            self.win.blit(Attack_range_text, (433, 450))

            Cost = pygame.font.Font(arial, 20)
            Cost_text = Cost.render(" Cost = 30", True, WHITE)
            self.win.blit(Cost_text, (433, 470))

            # Topic_2 = pygame.font.Font(arial, 30)
            # Topic_2_text = Topic_2.render("  Toyz's   ", True, RED)
            # self.win.blit(Topic_2_text, (435, 420))

            # Topic_3 = pygame.font.Font(arial, 30)
            # Topic_3_text = Topic_3.render("    dog   ", True, WHITE)
            # self.win.blit(Topic_3_text, (435, 455))

            """
            Topic = pygame.font.Font(arial, 22)
            Topic_text = Topic.render("Initial ability", True, WHITE)
            self.win.blit(Topic_text, (435, 395))
            
            HP = pygame.font.Font(arial, 20)        
            HP_text = HP.render(" HP = 30", True, WHITE)
            self.win.blit(HP_text, (430, 415))
            
            Power = pygame.font.Font(arial, 20)        
            Power_text = Power.render(" Power = 2", True, WHITE)
            self.win.blit(Power_text, (430, 435))
           
            Attack_range = pygame.font.Font(arial, 20)        
            Attack_range_text = Attack_range.render(" Range = 60", True, WHITE)
            self.win.blit(Attack_range_text, (430, 455))
            
            Cost = pygame.font.Font(arial, 20)        
            Cost_text = Cost.render(" Cost = 50", True, WHITE)
            self.win.blit(Cost_text, (550, 475))
            """

    # def draw_data_brian(self):
    #     x, y = pygame.mouse.get_pos()
    #     brian_btn_rect = brian_button_image.get_rect()
    #     brian_btn_rect.center = (235, 550)
    #     if(brian_btn_rect.collidepoint(x, y)):
    #         brian_data = pygame.Surface((220, 100), pygame.SRCALPHA)
    #         brian_data.fill((0, 0, 0, 64))
    #         self.win.blit(brian_data, (190, 390))

    #         Topic = pygame.font.Font(arial, 22)
    #         Topic_text = Topic.render(
    #             " Unlock after checkpoint 1", True, WHITE)
    #         self.win.blit(Topic_text, (195, 390))

    #         HP = pygame.font.Font(arial, 20)
    #         HP_text = HP.render(" HP = 1, attack then die", True, WHITE)
    #         self.win.blit(HP_text, (195, 410))

    #         Power = pygame.font.Font(arial, 20)
    #         Power_text = Power.render(" Power = 7, AOE", True, WHITE)
    #         self.win.blit(Power_text, (195, 430))

    #         Attack_range = pygame.font.Font(arial, 20)
    #         Attack_range_text = Attack_range.render(" Range = 60", True, WHITE)
    #         self.win.blit(Attack_range_text, (195, 450))

    #         Cost = pygame.font.Font(arial, 20)
    #         Cost_text = Cost.render(" Cost = 70", True, WHITE)
    #         self.win.blit(Cost_text, (195, 470))

    def draw_locked_brian(self):
        # x, y = pygame.mouse.get_pos()
        # locked_btn_rect = locked_button_image.get_rect()
        # locked_btn_rect.center = (235, 550)
        # if (locked_btn_rect.collidepoint(x, y)):
        #     brian_data = pygame.Surface((155, 100), pygame.SRCALPHA)
        #     brian_data.fill((0, 0, 0, 64))
        #     self.win.blit(brian_data, (190, 390))

        #     Topic_1 = pygame.font.Font(arial, 20)
        #     Topic_1_text = Topic_1.render(" This hero will", True, WHITE)
        #     self.win.blit(Topic_1_text, (190, 395))

        #     Topic_2 = pygame.font.Font(arial, 20)
        #     Topic_2_text = Topic_2.render(" be unclocked", True, WHITE)
        #     self.win.blit(Topic_2_text, (190, 430))

        #     Topic_3 = pygame.font.Font(arial, 20)
        #     Topic_3_text = Topic_3.render(
        #         " in further checkpoint", True, WHITE)
        #     self.win.blit(Topic_3_text, (190, 465))
        pass

    def draw_skill_data(self):
        # x, y = pygame.mouse.get_pos()
        # skill_btn_rect = SPECIAL_SKILL_BTN_IMAGE.get_rect()
        # skill_btn_rect.center = (755, 575)
        # if(skill_btn_rect.collidepoint(x, y)):
        #     skill_data = pygame.Surface((185, 50), pygame.SRCALPHA)
        #     skill_data.fill((0, 0, 0, 128))
        #     self.win.blit(skill_data, (835, 500))

        #     Cost = pygame.font.Font(arial, 20)
        #     Cost_text = Cost.render("Cost = 200", True, WHITE)
        #     self.win.blit(Cost_text, (840, 505))

        #     Ability = pygame.font.Font(arial, 20)
        #     Ability_text = Ability.render("Enemy's hp is halved", True, WHITE)
        #     self.win.blit(Ability_text, (840, 525))
        pass

    def draw_upgrade_data(self):
        x, y = pygame.mouse.get_pos()
        upgrade_btn_rect = UPGRADE_BTN_IMAGE.get_rect()
        upgrade_btn_rect.center = (715, 550)
        if(upgrade_btn_rect.collidepoint(x, y)):
            upgrade_data = pygame.Surface((200, 105), pygame.SRCALPHA)
            upgrade_data.fill((0, 0, 0, 170))
            self.win.blit(upgrade_data, (670, 390))

            upgrade = pygame.font.Font(arial, 20)
            upgrade_text = upgrade.render("Upgrade", True, WHITE)
            self.win.blit(upgrade_text, (673, 390))

            Initial = pygame.font.Font(arial, 20)
            Initial_text = Initial.render("Initial level = 0", True, WHITE)
            self.win.blit(Initial_text, (673, 410))

            Max = pygame.font.Font(arial, 20)
            Max_text = Max.render("Max level = 3", True, WHITE)
            self.win.blit(Max_text, (673, 430))

            Cost = pygame.font.Font(arial, 20)
            Cost_text = Cost.render("Cost = 100,150,200", True, WHITE)
            self.win.blit(Cost_text, (673, 450))

            Upgrade_mul = pygame.font.Font(arial, 20)
            Upgrade_mul_text = Upgrade_mul.render(
                "power and hp * 1.3", True, WHITE)
            self.win.blit(Upgrade_mul_text, (673, 470))

    def draw_menu(self, menu):
        self.win.blit(menu.image, menu.rect)
        for btn in menu.buttons:
            self.win.blit(btn.image, btn.rect)

    def draw_attack_en(self, en_group):
        for en in en_group:
            if en.attack_light == 1:
                AL = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
                AL.fill(PINK)
                self.win.blit(AL, (0, 0))
                
                self.win.blit(en_attack_image,
                              (en.rect.x+ en.rect.width+10, en.rect.y))
            if en.attack_light == 2:
                AL = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
                AL.fill(RED)
                self.win.blit(AL, (0, 0))

    def draw_attack_he(self, he_group, en_group, en_tower_hp):
        for he in he_group:
            if he.attack_light == 1:
                he.draw_atk_counter = 0
            if he.draw_atk_counter <= 4 and en_group:
                self.win.blit(he.attack_image,
                              (en_group[0].rect.x+20, en_group[0].rect.y-20))
                he.draw_atk_counter += 1
            elif he.draw_atk_counter <= 4 and en_tower_hp > 0:
                self.win.blit(he.attack_image, (he.rect.centerx -
                                                he.attack_location_x, he.rect.centery))
                he.draw_atk_counter += 1
            else:
                he.draw_atk_counter = 100

    def draw_money(self, money: int):
        self.win.blit(MONEY_IMAGE, (30, 510))
        Money = pygame.font.Font(arial, 40)
        Money_text = Money.render(f"{money}", True, WHITE)
        self.win.blit(Money_text, (120, 530))

    def draw_mytower_hp(self, lives, max_lives):
        # draw_lives
        pygame.draw.rect(
            self.win, SKY_BLUE, [870+(HEALTH_WIDTH/max_lives*lives), 280, HEALTH_WIDTH/max_lives*(max_lives-lives), HEALTH_HEIGHT])
        pygame.draw.rect(
            self.win, NAVY, [870, 280, HEALTH_WIDTH/max_lives*lives, HEALTH_HEIGHT])

    def draw_entower_hp(self, lives, max_lives):
        # draw_lives
        # pygame.draw.rect(
        #     self.win, RED, [5+(HEALTH_WIDTH/max_lives*lives), 280, HEALTH_WIDTH/max_lives*(max_lives-lives), HEALTH_HEIGHT])
        # pygame.draw.rect(
        #     self.win, GREEN, [5, 280, HEALTH_WIDTH/max_lives*lives, HEALTH_HEIGHT])
        pass
    


    def draw_game_over(self):
        transparent_surface = pygame.Surface(
            self.win.get_size(), pygame.SRCALPHA)
        transparency = 180
        pygame.draw.rect(transparent_surface,
                         (0, 0, 0, transparency), [0, 0, 1024, 600], 0)
        over = pygame.font.Font(arial, 30)
        game_over_text = over.render("click to continue...", True, WHITE)
        self.win.blit(transparent_surface, (0, 0))
        self.win.blit(game_loss_image, (0, 0))
        self.win.blit(game_over_text, (830, 560))

    def draw_game_win(self):
        transparent_surface = pygame.Surface(
            self.win.get_size(), pygame.SRCALPHA)
        transparency = 180
        pygame.draw.rect(transparent_surface,
                         (0, 0, 0, transparency), [0, 0, 1024, 600], 0)
        over = pygame.font.Font(arial, 30)
        game_win_text = over.render("click to continue...", True, WHITE)
        self.win.blit(transparent_surface, (0, 0))
        self.win.blit(game_win_image, (0, 0))
        self.win.blit(game_win_text, (830, 560))

    # def draw_skill_animation(self):
    #     x1, y1 = self.skill_move_path[self.path_index]
    #     x2, y2 = self.skill_move_path[self.path_index + 1]
    #     distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    #     max_count = int(distance / self.stride)
    #     # compute the unit vector
    #     unit_vector_x = (x2 - x1) / distance
    #     unit_vector_y = (y2 - y1) / distance
    #     # compute the movement
    #     delta_x = unit_vector_x * self.stride * self.move_count
    #     delta_y = unit_vector_y * self.stride * self.move_count
    #     # update the position and counter
    #     if self.move_count <= max_count:
    #         self.rect.center = (x1 + delta_x, y1 + delta_y)
    #         self.move_count += 1
    #     else:
    #         self.move_count = 0
    #         self.rect.center = self.skill_move_path[self.path_index]

    #     self.win.blit(self.skillimage, self.rect)

    def draw_finish_win(self):
        transparent_surface = pygame.Surface(
            self.win.get_size(), pygame.SRCALPHA)
        transparency = 180
        pygame.draw.rect(transparent_surface, (8, 46, 87,
                                               transparency), [0, 0, 1024, 600], 0)
        over = pygame.font.Font(arial, 30)
        complete = pygame.font.Font(arial, 80)
        text = pygame.font.Font(arial, 40)
        game_win_text = over.render("click to back to menu", True, WHITE)
        # game_finish_text = text.render(
        #     "now you can try to use less time!", True, WHITE)
        congrats = complete.render("CONGRATS", True, WHITE)
        self.win.blit(transparent_surface, (0, 0))
        self.win.blit(congrats, (350, 15))
        #self.win.blit(game_finish_text, (300, 100))
        self.win.blit(game_win_text, (800, 560))
        self.win.blit(game_completed_image, (262, 150))

    def draw_game_time(self, time):
        self.win.blit(clock_status_image, (WIN_WIDTH - 230, WIN_HEIGHT - 90))
        timer = pygame.font.Font(arial, 40)
        time_text = timer.render(f"{time}", True, WHITE)
        self.win.blit(time_text, (WIN_WIDTH-120, WIN_HEIGHT-75))

    def draw_score(self, score):
        score_font = pygame.font.Font(arial, 28)
        self.score = 1000
        score_text = score_font.render(f"{score} / 1000", True, WHITE)
        self.win.blit(score_text, (WIN_WIDTH / 2 - 45, 15))
