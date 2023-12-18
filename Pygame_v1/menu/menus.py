import pygame
import os
from settings import IMAGE_PATH

pygame.init()


godtone_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH,"godtone_btn.jpg")), (80, 80))
howhow_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH,"howhow_btn.jpg")), (80, 80))
p_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH,"p_btn.PNG")), (80, 80))
brian_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH,"brian_btn.jpg")), (80, 80))
locked_button_image = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH,"locked.PNG")), (80, 80))
UPGRADE_BTN_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "upgrade.png")), (160, 50))
SPECIAL_SKILL_BTN_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGE_PATH, "skill.png")), (160, 50))


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
        self._buttons = [Button(p_button_image, "p", 355, 550),
                         Button(godtone_button_image, "godtone", 475, 550),
                         Button(howhow_button_image, "howhow", 595, 550),
                         Button(brian_button_image, "brian", 235, 550),
                         Button(SPECIAL_SKILL_BTN_IMAGE, 'special', 755, 575),
                         Button(UPGRADE_BTN_IMAGE, 'upgrade', 755, 525)]
    @property
    def buttons(self):
        return self._buttons
