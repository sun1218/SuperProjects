import pygame
import sys
from pygame.locals import *
from random import *

import plane
import bullet
import enemy


def main():
    pygame.init()
    pygame.mixer.init()
    MyPlane_1_image = 'me.png'
    MyBullet_1_image = 'bullet1.png'
    EnemyPlane_1_image = 'enemy1.png'
    EnemyPlane_2_image = 'enemy2.png'
    EnemyPlane_3_image = 'enemy3.png'
    background = "background.png"
    MyBullet_1_music = 'bullet.wav'
    enemy_1_dead_music = 'enemy1_down.wav'
    enemy_2_dead_music = 'enemy2_down.wav'
    enemy_3_dead_music = 'enemy3_down.wav'
    bg_music = 'game_music.ogg'
    MyBullet_1_sound = pygame.mixer.Sound(MyBullet_1_music)
    
    Mybackground = pygame.image.load(background)
    bg_size = 480, 700
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("飞机大战")
    MySpeed = 5
    MyBullet = []
    Enemy = []
    num1 = 0
    num2 = 0
    pygame.key.set_repeat(1, 1)
    clock = pygame.time.Clock()
    bullet_group = pygame.sprite.Group()
    MyPlane = plane.Plane(MyPlane_1_image, bg_size, MySpeed)
    
    bg_music = pygame.mixer.Sound(bg_music)    
    bg_music.play(-1)


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                bg_music.stop()
                pygame.quit()
                sys.exit()
        
            key = pygame.key.get_pressed()

        if key[K_w] or key[K_UP]:
            MyPlane.move([0, -1])
        if key[K_s] or key[K_DOWN]:
            MyPlane.move([0, 1])
        if key[K_a] or key[K_LEFT]:
            MyPlane.move([-1, 0])
        if key[K_d] or key[K_RIGHT]:
            MyPlane.move([1, 0])
        if key[K_j] or key[K_1]:
            if num1 == 5:
                MyBullet_1_sound.play()
                temp = bullet.Bullet(MyPlane.rect.centerx, MyPlane.rect.top, MyBullet_1_image)
                MyBullet.insert(0, temp)
                bullet_group.add(temp)
                num1 = 0
            num1 += 1
        if key[K_RETURN]:
            Enemy.clear()

        screen.blit(Mybackground, (0, 0))

        for each in MyBullet:
            if each.disappear == True:
                MyBullet.remove(each)
            else:
                each.move()
                screen.blit(each.image, each.rect)

        for each in Enemy:
            if each.disappear == True:
                Enemy.remove(each)
            else:
                each.move()
                screen.blit(each.image, each.rect)
        
        for x in MyBullet:
            for y in Enemy:
                if pygame.sprite.collide_rect(x, y):
                    MyBullet.remove(x)
                    Enemy.remove(y)
                    y.dead()
                    break
        

        x = randint(0, bg_size[0])
        if (num2 % 30) == 0 and num2 != 0:
            temp = enemy.Enemy(x, 0, EnemyPlane_1_image, 3, bg_size, enemy_1_dead_music)
            Enemy.insert(0, temp)
        if (num2 % 90) == 0 and num2 != 0:
            temp = enemy.Enemy(x, 0, EnemyPlane_2_image, 2, bg_size, enemy_2_dead_music)
            Enemy.insert(0, temp)
        if (num2 % 250) == 0 and num2 != 0:
            temp = enemy.Enemy(x, 0, EnemyPlane_3_image, 1, bg_size, enemy_3_dead_music)
            Enemy.insert(0, temp)
            num2 = 0

        num2 += 1
        screen.blit(MyPlane.image, MyPlane.rect)
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()