class Ogr(p.sprite.Sprite):
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









def draw_game():
    global background_img
    screen.blit(background_img, (0, 0))
    laser_group.draw(screen)
    ship.draw(screen)

class Meteor(p.sprite.Sprite):
    def _init_(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.speed_x = rnd.randint(-3, 3)
        self.speed_y = rnd.randint(3, 9)

        self.original_image = image
        self.angle = 0
        self.rotation_speed = rnd.randint(-5, 5)

    def update(self):
        self.rotate()
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()

    def rotate(self):
        self.angle += self.rotation_speed
        self.image = p.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

