import pygame


class Plane(pygame.sprite.Sprite):
    def __init__(self, image, bg_size, speed):
        pygame.sprite.Sprite.__init__(self)
        self.side = [0, 0]
        self.speed = speed
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = \
            (bg_size[0] - self.rect.width) // 2, bg_size[1] - self.rect.height
        self.bg_size = bg_size

    def move(self, side):
        self.side = side
        self.rect = self.rect.move\
            ([self.side[0] * self.speed, self.side[1] * self.speed])
        if self.rect.right > self.bg_size[0]:
            self.rect.left = self.bg_size[0] - self.rect.width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > self.bg_size[1]:
            self.rect.top = self.bg_size[1] - self.rect.height
        if self.rect.top < 0:
            self.rect.top = 0