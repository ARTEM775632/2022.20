import pygame
from pygame import *
from constants import *
from MyPlayer import Player

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
        pygame.display.flip()

    def main_loop(self):
        while self.running == True:
            if self.player.state != DEAD:
                self.player.moove()
            self.render()
            self.handle_events()
            clock.tick(200)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
game = Main(screen)