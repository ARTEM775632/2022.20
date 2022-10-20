import random as rnd
import pygame
from constants import *
class Ogr(pygame.sprite.Sprite):
    def _init_(self, pos, image, life):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.speed_x = rnd.randint(-8, 8)
        self.speed_y = rnd.randint(3, 9)
        self.original_image = image
        self.life = life


    def update(self, ship):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y > SCREEN_HEIGHT:
            self.speed_y = -self.speed_y







