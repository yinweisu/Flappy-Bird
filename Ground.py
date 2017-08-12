import pygame

Ground_length = 336
class Ground(pygame.sprite.Sprite):
    def __init__(self, land_image, x):
        pygame.sprite.Sprite.__init__(self)
        self.x = x + (Ground_length / 2)
        self.y = 480
        self.speed = 10
        self.image = land_image
        self.rect = self.image.get_rect()
        self.rect.midbottom = (self.x, self.y)

    def move(self):
        self.x -= self.speed
        if self.rect.right < 0:
            self.x = 640 + Ground_length / 2
        self.rect.midbottom = (self.x, self.y)

