import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, bird_image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = pos
        self.image = bird_image
        self.rect = self.image.get_rect()
        self.rect.midbottom = pos
        self.gravity = 5
        self.vy = 0

    def update_image(self, bird_image):
        self.image = bird_image

    def update(self):
        self.y += self.vy
        self.vy += self.gravity * 0.2
        self.rect.midbottom = (self.x, self.y)

    def jump(self):
        self.vy = -10
        self.rect.midbottom = (self.x, self.y)