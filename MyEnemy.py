import pygame
#import time
from constants import *
import random as rnd
import Projective
from pygame.sprite import Sprite, collide_rect


#class Mob(pygame.sprite.Sprite):
class Mob():
    def __init__(self, game, START_Y, START_X, dir):
        super().__init__()
    #    self.image = pygame.image.load('data/hpframe.png').convert_alpha()
     #   self.rect = self.image.get_rect(center=(START_X, START_Y))
     #   self.rect = self.image.get_rect()
        self.state = ALIVE
        self.x = START_X
        self.y = START_Y
        self.size = 40
#        self.rect.x = self.x
     #   self.rect.y = self.y
        self.dir = dir
        self.hp = orge_HP
        self.mp = orge_MP
        self.spell_casted = 0
        self.mooving = [0, 0, 0, 0]
        self.stright = 0

    def render(self, screen):
        # screen.blit(self.images[self.direction][self.state], (self.x, self.y))
        if self.dir>=4: print(self.dir)
        else:
            screen.blit(self.images[self.dir][0], (self.x, self.y))

    def block_check(self):
        self.blocked = [0, 0, 0, 0]
        if self.x >= SCREEN_WIDTH - 50:    self.blocked[RIGHT] = 1
        elif self.x <= 0:                 self.blocked[LEFT] = 1
        elif self.y <= 0:                 self.blocked[UP] = 1
        elif self.y >= SCREEN_HEIGHT - 50: self.blocked[DOWN] = 1

        for j in self.game.mobs:
            if self.x != j.x and self.y != j.y:
                self.contact_check(j)
        self.contact_check(self.game.player)
    def contact_check(self, obj):
        if self.x >= obj.x - self.size and self.y <= obj.y + obj.size - 15 and self.y >= obj.y - obj.size + 15 and self.x <= obj.x + obj.size / 2:
            self.blocked[RIGHT] = 1
        if self.x <= obj.x + obj.size and self.y <= obj.y + obj.size - 15 and self.y >= obj.y - obj.size + 15 and self.x >= obj.x:
            self.blocked[LEFT] = 1
        if self.y <= obj.y - obj.size and self.x <= obj.x + obj.size - 15 and self.x >= obj.x - obj.size + 15 and self.y >= obj.y:
            self.blocked[UP] = 1
        if self.y >= obj.y - self.size and self.x <= obj.x + obj.size - 15 and self.x >= obj.x - obj.size + 15 and self.y <= obj.y + obj.size / 2:
            self.blocked[DOWN] = 1

    def random_moove(self):
        self.mooving = [0,0,0,0]
        self.mooving[rnd.randint(0,3)] = 1

class Orge(Mob):
    def __init__(self, game, START_X, START_Y, dir):
        self.image_pack = ['data/orge_left.png', 'data/orge_down.png', 'data/orge_right.png', 'data/orge_up.png']
        self.speed = 5
        self.game = game
        self.images = []
        Mob.__init__(self, game, START_X, START_Y, dir)
        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            temp.set_colorkey((255, 255, 255))
            i=[]
            i.append(temp.subsurface(0,0,90,90))
            i.append(temp.subsurface(90,0,90,90))
            i.append(temp.subsurface(180,0,90,90))
            self.images.append(i)

    def moove(self):
        self.block_check()
        if self.mooving[RIGHT] == 1 and self.blocked[RIGHT] == 0:
            self.x += self.speed
            self.direction = RIGHT
        if self.mooving[DOWN] and self.blocked[DOWN] == 0:
            self.y += self.speed
            self.direction = DOWN
        if self.mooving[LEFT] and self.blocked[LEFT] == 0:
            self.x -= self.speed
            self.direction = LEFT
        if self.mooving[UP] and self.blocked[UP] == 0:
            self.y -= self.speed
            self.direction = UP

        if self.x <= 0: self.x = 0
        if self.y <= 0: self.y = 0
        if self.x >= SCREEN_WIDTH-35: self.x = SCREEN_WIDTH-35
        if self.y >= SCREEN_HEIGHT-75: self.y = SCREEN_HEIGHT-75
    def __str__(self):
        Mob.__str__(self)

    def tick(self):
        if self.mp <= orge_MP: self.mp += mp_reg_ogr
        if self.hp <= orge_HP: self.hp += HP_REG
        if pygame.time.get_ticks() > self.spell_casted + TIME2SHOT:
            self.state = ALIVE

            #организуем развороты  нашим ограм
        self.stright+=1
        if self.stright >= STEPS_STRIGHT:
            self.stright = 0
            ddir=rnd.randint(0,3)
            self.dir = ddir
            self.mooving[ddir] = 1




