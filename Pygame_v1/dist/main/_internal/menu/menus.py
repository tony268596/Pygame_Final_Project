import pygame
import os
from settings import IMAGE_PATH

pygame.init()


crew_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH,"crew_btn.png")), (80, 80))
dog_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH,"dog_btn.png")), (80, 80))
ship_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH,"ship_btn.png")), (80, 80))

locked_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH,"locked.png")), (80, 80))
UPGRADE_BTN_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "upgrade_btn.png")), (80, 80))
# SPECIAL_SKILL_BTN_IMAGE = pygame.transform.scale(
#     pygame.image.load(os.path.join(IMAGE_PATH, "skill.png")), (160, 50))


class Button:
    def __init__(self, image, name: str, x: int, y: int):
        self.image = image
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x, y):
        return True if self.rect.collidepoint(x, y) else False

    @property
    def response(self):
        return self.name


class MainMenu:
    def __init__(self):
        # self._buttons = [Button(ship_button_image, "ship", 355, 550),
        #                  Button(crew_button_image, "crew", 475, 550),
        #                  Button(dog_button_image, "dog", 595, 550),
        #                  Button(brian_button_image, "brian", 235, 550),
        #                  Button(SPECIAL_SKILL_BTN_IMAGE, 'special', 755, 575),
        #                  Button(UPGRADE_BTN_IMAGE, 'upgrade', 755, 525)]
        self._buttons = [Button(ship_button_image, "ship", 355, 550),
                         Button(crew_button_image, "crew", 475, 550),
                         Button(dog_button_image, "dog", 595, 550),
                         Button(UPGRADE_BTN_IMAGE, 'upgrade', 755, 525)]
    @property
    def buttons(self):
        return self._buttons
