import pygame
from constants import *

class Projective(pygame.sprite.Sprite):
    def __init__(self,  x_start, y_start, dir, image_pack):
        super().__init__()
        self.x = x_start
        self.y = y_start
        self.direction = dir
        self.image = pygame.image.load(image_pack).convert_alpha()

        self.images = []
        self.images.append(self.image.subsurface(0, 0, 64, 64))
        self.images.append(self.image.subsurface(64, 0, 64, 64))
        self.images.append(self.image.subsurface(128, 0, 64, 64))
        self.images.append(self.image.subsurface(192, 0, 64, 64))
        self.image=self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y

    #def render(self, screen):
     #   screen.blit(self.images[self.direction], (self.rect.x, self.rect.y))

  #  def moove(self):
     #   print(self.speed)
    #    if self.direction == RIGHT:
     #       self.rect.x += self.speed
     #   elif self.direction == DOWN:
     #       self.rect.y += self.speed
     #   elif self.direction == LEFT:
     #       self.rect.x -= self.speed
     #   else:
      #      self.rect.y -= self.speed

    #    if self.rect.x > SCREEN_WIDTH or self.rect.x < -60 or self.rect.y > SCREEN_HEIGHT or self.rect.y < -60:
     #       self.kill()

    def update(self):
        if self.direction == RIGHT:
            self.rect.x += self.speed
        elif self.direction == DOWN:
            self.rect.y += self.speed
        elif self.direction == LEFT:
            self.rect.x -= self.speed
        else:
            self.rect.y -= self.speed
        if self.rect.x > SCREEN_WIDTH or self.rect.x < -60 or self.rect.y > SCREEN_HEIGHT or self.rect.y < -60:
            self.kill()


class Arrow(Projective):
    def __init__(self,  x_start, y_start, dir):
        self.imagef = 'data/arrows.png'
        self.speed = 16
        super().__init__(x_start, y_start, dir, self.imagef)

class Firearrow(Projective):
    def __init__(self, x_start, y_start, dir):
        self.imagef = 'data/firearrows.png'
        self.speed = 5
        super().__init__( x_start, y_start, dir, self.imagef)

class Fireball(Projective):
    def __init__(self, x_start, y_start, dir):
        self.imagef = 'data/fireball.png'
        self.speed = 20
        print('Fireball', x_start, y_start)
        super().__init__(x_start, y_start, dir, self.imagef)

    def __str__(self):
        super().__str__(self)
