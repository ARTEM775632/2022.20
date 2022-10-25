import random as rnd
import pygame
from constants import *
class Ogr(pygame.sprite.Sprite):
    def __init__(self, pos, image, life):
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

        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0

        if self.rect.x < ship.x:
            self.speed_x += 1
        if self.rect.x > ship.x:
            self.speed_x -= 1

        if self.rect.y < ship.y:
            self.speed_y += 1
        if self.rect.y > ship.y:
            self.speed_y -= 1

        if self.speed_x > OGR_SPEED:  self.speed_x = OGR_SPEED
        if self.speed_x < -OGR_SPEED: self.speed_x = -OGR_SPEED

        if self.speed_y > OGR_SPEED:  self.speed_y = OGR_SPEED
        if self.speed_y < -OGR_SPEED: self.speed_y=-OGR_SPEED







