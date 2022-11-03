import random as rnd
import pygame
from constants import *
class Ogr(pygame.sprite.Sprite):
    def __init__(self, pos, image, life):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.speed_x = rnd.randint(-3, 2)
        self.speed_y = rnd.randint(3, 5)
        self.original_image = image
        self.life = life


    def update(self, target):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if (self.rect.y > SCREEN_HEIGHT) and (self.speed_y > 0):
            self.speed_y = -self.speed_y

        # соманаведение

        if self.rect.x<target.rect.x:
            self.speed_x+=1

        if self.rect.x>target.rect.x:
            self.speed_x-=1

        if self.rect.y<target.rect.y:
            self.speed_y+=1

        if self.rect.y>target.rect.y:
            self.speed_y-=1






