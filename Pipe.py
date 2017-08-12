import pygame


class Pipe(pygame.sprite.Sprite):
    def __init__(self, image, x, height, up_down):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.up_down = up_down
        self.x = x
        if self.up_down:
            self.y = -(420 - height)
            self.image = pygame.transform.flip(image, False, True)
        else:
            self.y = 480 + (420 - height)
            self.image = image
        self.rect = self.image.get_rect()
        if self.up_down:
            self.rect.midtop = [self.x, self.y]
        else:
            self.rect.midbottom = [self.x, self.y]

    def move(self):
        self.x -= self.speed
        if self.up_down:
            self.rect.midtop = [self.x, self.y]
        else:
            self.rect.midbottom = [self.x, self.y]