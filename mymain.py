import pygame
from pygame import *
from constants import *
from MyPlayer import Player

from pudge import Ogr
import random as rnd

from Projective import *

class Main():
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(self,'Grut')
        self.projective = []
        self.background = pygame.image.load('data/background.jpg')
        self.running = True
        self.ogr_group = pygame.sprite.Group()
        self.pr_group = pygame.sprite.Group()



        self.main_loop()


    def make_ogr(self):
        ogr_image = rnd.choice(ogr_images)
        ogr = Ogr((rnd.randint(0, SCREEN_HEIGHT), 400), ogr_image, rnd.randint(3, 5))
        self.ogr_group.add(ogr)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == SPAWN_OGR:
                self.make_ogr()

            if event.type == MOVE_PUDGE:
                self.ogr_group.update(self.player)
            if event.type == SPELL_REST:
                self.player.tick()

            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.player.walk=True
                    self.player.direction = RIGHT
                    self.player.mooving = [1,0,0,0]
                if event.key == K_DOWN:
                    self.player.walk = True
                    self.player.direction = DOWN
                    self.player.mooving = [0,1,0,0]
                if event.key == K_LEFT:
                    self.player.walk = True
                    self.player.direction = LEFT
                    self.player.mooving = [0,0,1,0]
                if event.key == K_UP:
                    self.player.walk = True
                    self.player.direction = UP
                    self.player.mooving = [0,0,0,1]

                if event.key == K_SPACE:
                    if self.player.state != DEAD:
                        self.player.state = DEAD
                    else:
                        self.player.state = ALIVE

                if event.key == K_z:
                    if self.player.mp >= SKILL1_COST and self.player.state != SHOOT and self.player.state != DEAD:
                        self.player.mp -= SKILL1_COST
                        #self.player.state = SHOOT
                        self.player.spell_casted = pygame.time.get_ticks()

                        self.pr_group.add(Arrow(self.player.rect.x, self.player.rect.y, self.player.direction))

                      #  if self.player.direction == RIGHT:
                       #     self.projective.append(Arrow(self.player.x+12, self.player.y, self.player.direction))
                     #   elif self.player.direction == DOWN:
                      #      self.projective.append(Arrow(self.player.x, self.player.y+12, self.player.direction))
                     #   elif self.player.direction == LEFT:
                     #       self.projective.append(Arrow(self.player.x-12, self.player.y, self.player.direction))
                     #   else:
                      #      self.projective.append(Arrow(self.player.x, self.player.y-12, self.player.direction))
                if event.key == K_x:
                    if self.player.mp >= SKILL2_COST and self.player.state != SHOOT and self.player.state != DEAD:
                        self.player.mp -= SKILL2_COST
                     #   self.player.state = SHOOT
                        self.player.spell_casted = pygame.time.get_ticks()

                        self.pr_group.add(Firearrow(self.player.rect.x, self.player.rect.y, self.player.direction))

                if event.key == K_c:
                    print(self.player.rect.x, self.player.rect.y)
                    if self.player.mp >= SKILL3_COST and self.player.state != SHOOT and self.player.state != DEAD:
                        self.player.mp -= SKILL3_COST
                     #   self.player.state = SHOOT
                        self.player.spell_casted = pygame.time.get_ticks()

                        self.pr_group.add(Fireball(self.player.rect.x, self.player.rect.y, self.player.direction))



            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    self.player.walk = False
                    self.player.mooving[RIGHT] = 0
                if event.key == K_DOWN:
                    self.player.walk = False
                    self.player.mooving[DOWN] = 0
                if event.key == K_LEFT:
                    self.player.walk = False
                    self.player.mooving[LEFT] = 0
                if event.key == K_UP:
                    self.player.walk = False
                    self.player.mooving[UP] = 0


    def render(self):

        self.screen.blit(self.background,(0,0))
        self.player.render(screen)
        self.ogr_group.draw(screen)

        self.pr_group.draw(screen)

       # for i in self.projective:
        #    i.render(screen)

        pygame.display.flip()
    def fired_a(self):
        hits = sprite.groupcollide(self.ogr_group, self.pr_group, True, True)
        if hits:
            self.player.score += 1

    def ogr_player_collide(self):
        # Проверка, не ударил ли моб игрока
        hits = pygame.sprite.spritecollide(self.player, self.ogr_group, True)
        for hit in hits:
            self.player.hp -= 30

    def main_loop(self):
        while self.running == True:
            pygame.display.set_caption(f'Ogres= {len(self.ogr_group)}   Score = {self.player.score}')
            if self.player.state != DEAD:
                self.player.moove()
            #for i in self.projective:
             #   i.moove()
            self.pr_group.update()
            self.render()
            self.fired_a()
            self.handle_events()
            self.ogr_player_collide()
            clock.tick(60)






pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

SPAWN_OGR = pygame.USEREVENT+1
pygame.time.set_timer(SPAWN_OGR, 1000)

MOVE_PUDGE = pygame.USEREVENT+2
pygame.time.set_timer(MOVE_PUDGE, 250)

SPELL_REST = USEREVENT+3
pygame.time.set_timer(SPELL_REST, 100)

temp = pygame.image.load('data/ogre.png').convert_alpha()
i = []
for f in range(5):
    i.append(temp.subsurface(f * 71, 0, 71, 71))
ogr_images = i
# Making groups

game = Main(screen)