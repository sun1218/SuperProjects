import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x, y
        self.speed = 12
        self.disappear = False

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.disappear = True