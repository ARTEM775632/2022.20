import pygame
from pygame import *
from constants import *
from MyPlayer import Player
from pudge import Ogr
import random as rnd

class Main():
    def __init__(self, screen):
        self.screen = screen
        self.player = Player('Grut')
        self.background = pygame.image.load('data/background.jpg')
        self.running = True
        self.main_loop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

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
                    if self.player.state != SHOOT:
                        self.player.state = SHOOT
                    else:
                        self.player.state = ALIVE



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
        ogr_group.draw(screen)
        ogr_group.update()
        pygame.display.flip()

    def main_loop(self):
        while self.running == True:
            if self.player.state != DEAD:
                self.player.moove()
            self.render()
            self.handle_events()
            clock.tick(200)

    def make_ogr(self):
        ogr_image = rnd.choice(ogr_images)
        ogr = Ogr((rnd.randint(0, SCREEN_WIDTH), -20), ogr_image, rnd.randint(3, 5))
        ogr_group.add(ogr)




pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
SPAWN_OGR = pygame.USEREVENT+1
pygame.time.set_timer(SPAWN_OGR, 1000)
temp = pygame.image.load('data/ogre.png').convert_alpha()
i = []
for f in range(5):
    i.append(temp.subsurface(f * 71, 0, 71, 71))
ogr_images = i
# Making groups
ogr_group = pygame.sprite.Group()
game = Main(screen)