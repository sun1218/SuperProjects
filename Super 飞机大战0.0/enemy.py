import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image, speed, bg_size, music):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        if self.rect.w > x:
            self.rect.left, self.rect.top = self.rect.w, y - self.rect.height
        if x > bg_size[0] - self.rect.w:
            self.rect.left, self.rect.top = x - self.rect.w, y - self.rect.height
        else:
            self.rect.left, self.rect.top = x, y - self.rect.height
        self.speed = speed
        self.disappear = False
        self.bg_size = bg_size
        self.music = music

    def move(self):
        self.rect.top += self.speed

        if self.bg_size[1] + self.rect.height < self.rect.bottom:
            self.disappear = True

    def dead(self):
        self.dead = pygame.mixer.Sound(self.music)
        self.dead.play()