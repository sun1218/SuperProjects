import pygame as pg
import sys
import random


class Actor:

    def __init__(self,name,filename,x,y):
        self.name = name
        self.actor = pg.image.load(filename)
        self.position = self.actor.get_rect()
        self.position[0] = x
        self.position[0] = y

    def move(self, position):
        position[0] *= 50
        position[1] *= 50

        if self.position[0] + position[0] <= 0 or self.position[0] + position[0] >= width:
            position[0] -= (position[0] * 2)

        if self.position[1] + position[1] <= 0 or self.position[1] + position[1] >= height:
            position[1] -= (position[1] * 2)
        if self.turn in [8, 4, 7, 5, 3, 6]:
            self.actor = pg.transform.flip(self.actor, True, False)

        print(' %s 当前位置: x = %s, y = %s' % (self.name, self.position[0], self.position[1]), end=' ')
        self.position = self.position.move(position)
        screen.blit(self.actor, self.position)

    def selfTurn(self,stepLength):
        self.turn = random.randint(1, 8)

        if self.turn == 1:
            move = [0, -stepLength]
        elif self.turn == 2:
            move = [stepLength, 0]
        elif self.turn == 3:
            move = [0, stepLength]
        elif self.turn == 4:
            move = [-stepLength, 0]
        elif self.turn == 5:
            move = [stepLength, -stepLength]
        elif self.turn == 6:
            move = [stepLength, stepLength]
        elif self.turn == 7:
            move = [-stepLength, stepLength]
        elif self.turn == 8:
            move = [-stepLength, -stepLength]

        return move




class Fish(Actor):

    def __init__(self,name,filename,x,y):
        print('\n')
        super().__init__(name,filename,x,y)

    def move(self,position):
        super().move(position)
        print('移动位置: x = %s, y = %s' % (self.position[0], self.position[1]))



class Turtle(Actor):

    def __init__(self,name,filename,x,y):
        self.heath = 100
        super().__init__(name,filename,x,y)

    def move(self,position):
        if self.heath != 0:
            super().move(position)
            self.heath -= 1
            print('移动位置: x = %s, y = %s 生命 = %s' % (self.position[0], self.position[1],self.heath))




def drawLines():
    for i in range(1,11):
        pg.draw.aaline(screen,black,(i*block_size,0),(i*block_size,10*block_size), 2)
        pg.draw.aaline(screen,black,(0,i*block_size),(10*block_size,i*block_size), 2)


pg.init()

clock = pg.time.Clock()

#初始化画布
block_size = 50
bg_size = width, height = 10* block_size, 10 * block_size
bg_color = (225, 225,225)

screen = pg.display.set_mode(bg_size)
pg.display.set_caption("龟和鱼")
black = (0,0,0)

screen.fill(bg_color)

#创建乌龟
x = random.randint(1, 10) * block_size
y = random.randint(1, 10) * block_size
turtle = Turtle('乌龟','turtle.png',x,y)
turtle.actor = pg.transform.scale(turtle.actor,(block_size,block_size))

#创建鱼
fish = dict()
for i in range(0,10):
    x = random.randint(1,10)*block_size
    y = random.randint(1,10)*block_size
    fish[i] = Fish('fish %d'%i,'fish.png',x,y)
    fish[i].actor = pg.transform.scale(fish[i].actor, (block_size, block_size))



while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            print('exits...^_^')
            sys.exit()

    if turtle.heath == 0:
        sys.exit()


    drawLines()

    print('====================================================')

    for i in range(len(fish)):
        move = fish[i].selfTurn(1)
        fish[i].move(move)

    move = turtle.selfTurn(1)
    turtle.move(move)

    print('====================================================')
    
    #刷新画布
    pg.display.flip()
    screen.fill(bg_color)
    pg.time.delay(1000)




