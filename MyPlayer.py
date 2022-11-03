import pygame
#import time
from constants import *
import Projective
from pygame.sprite import Sprite, collide_rect

class Player(Sprite):
    def __init__(self, game, name: str):
        self.game = game
        self.image = pygame.image.load('data/hpframe.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.state = ALIVE
        #self.x = START_X
        #self.y = START_Y
        self.size = 60
        self.direction = RIGHT
        self.name = name
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.score = 0
        self.spell_casted = 0
        self.mooving = [0, 0, 0, 0]
        self.blocked = [0, 0, 0, 0]
        #self.image_pack = ['data/archerr.png','data/archerd.png'        , 'data/archerl.png', 'data/archeru.png']
        # self.images = []
        # for image in self.image_pack:
        #     temp = pygame.image.load(image).convert_alpha()
        #     i=[]
        #     i.append(temp.subsurface(0,0,64,64))
        #     i.append(temp.subsurface(64, 0, 64, 64))
        #     i.append(temp.subsurface(128, 0, 64, 64))
        #     self.images.append(i)

        self.hpframe = pygame.image.load('data/hpframe.png').convert_alpha()
        self.hpframe5 = pygame.image.load('data/hpframe5.png').convert_alpha()
        self.mpframe = pygame.image.load('data/mpframe.png').convert_alpha()
        self.mpframe5 = pygame.image.load('data/mpframe5.png').convert_alpha()

        temp = pygame.image.load('data/wizard.png').convert_alpha()
        i = []
        i.append(temp.subsurface(240, 186, 60, 88)) # право
        i.append(temp.subsurface(0, 0, 60, 88))  # низ
        i.append(temp.subsurface(0, 363, 59, 87))  # лево
        i.append(temp.subsurface(300, 0, 60, 88))  # верх
        i.append(temp.subsurface(60, 0, 60, 88))  # умер
        self.image = i





    def moove(self):
        self.block_check()
        if self.blocked==[1,1,1,1]:
            print('Aaaaaaarrrrrgggghhhhh')
        if self.mooving[RIGHT] == 1 and self.blocked[RIGHT] == 0:
            self.rect.x+=PLAYER_SPEED
            self.direction = RIGHT
        if self.mooving[DOWN] and self.blocked[DOWN] == 0:
            self.rect.y+=PLAYER_SPEED
            self.direction = DOWN
        if self.mooving[LEFT] and self.blocked[LEFT] == 0:
            self.rect.x-=PLAYER_SPEED
            self.direction = LEFT
        if self.mooving[UP] and self.blocked[UP] == 0:
            self.rect.y-=PLAYER_SPEED
            self.direction = UP

        if self.rect.x <= 0: self.rect.x = 0
        if self.rect.y <= 0: self.rect.y = 0
        if self.rect.x >= SCREEN_WIDTH-35: self.rect.x = SCREEN_WIDTH-35
        if self.rect.y >= SCREEN_HEIGHT-75: self.rect.y = SCREEN_HEIGHT-75

        # check if we can move

    def block_check(self):
        self.blocked = [0, 0, 0, 0]
      #  self.collisions(self.ref.npc[0])
        if self.rect.x >= SCREEN_WIDTH - 50:    self.blocked[RIGHT] = 1
        elif self.rect.x <= 0:                 self.blocked[LEFT] = 1
        elif self.rect.y <= 0:                 self.blocked[UP] = 1
        elif self.rect.y >= SCREEN_HEIGHT - 50: self.blocked[DOWN] = 1
        #for j in self.game.mobs:
        #    self.contact_check(j)
    # check for collisions
    def contact_check(self, obj):
        if self.rect.x >= obj.x - self.size and self.rect.y <= obj.y + obj.size - 15 and self.rect.y >= obj.y - obj.size + 15 and self.rect.x <= obj.x + obj.size / 2:
            self.blocked[RIGHT] = 1
        if self.rect.x <= obj.x + obj.size and self.rect.y <= obj.y + obj.size - 15 and self.rect.y >= obj.y - obj.size + 15 and self.rect.x >= obj.x:
            self.blocked[LEFT] = 1
        if self.rect.y <= obj.y - obj.size and self.rect.x <= obj.x + obj.size - 15 and self.rect.x >= obj.x - obj.size + 15 and self.rect.y >= obj.y:
            self.blocked[UP] = 1
        if self.rect.y >= obj.y - self.size and self.rect.x <= obj.x + obj.size - 15 and self.rect.x >= obj.x - obj.size + 15 and self.rect.y <= obj.y + obj.size / 2:
            self.blocked[DOWN] = 1


    def render(self, screen):
        # screen.blit(self.images[self.direction][self.state], (self.x, self.y))
        screen.blit(self.image[self.direction], (self.rect.x, self.rect.y))
        self.render_ui(screen)
    def render_ui(self, screen):
        screen.blit(self.hpframe, (self.rect.x-4, self.rect.y-5))
        m = 1
        z = self.hp // 5
        while m<= z:
            screen.blit(self.hpframe5, (self.rect.x-3+m*3, self.rect.y-4))
            m+=1

        screen.blit(self.mpframe, (self.rect.x - 4, self.rect.y - 1))
        m = 1
        z = self.mp // 5
        while m <= z:
            screen.blit(self.mpframe5, (self.rect.x - 3 + m * 3, self.rect.y) )
            m += 1


    def tick(self):
        print(1)
        if self.mp <= MAX_MP: self.mp+=MP_REG
        if self.hp <= MAX_HP: self.hp+=HP_REG
        if pygame.time.get_ticks() > self.spell_casted +TIME2SHOT:
            self.state = ALIVE





