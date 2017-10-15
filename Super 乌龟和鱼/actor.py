import pygame as pg

class Actor:

    def __init__(self,name,filename):
        self.name = name
        self.actor = pg.image.load(filename)
        self.position = self.actor.get_rect()

    def move(self, position):

        pass


class Fish(Actor):

    def __init__(self,name,filename):
        super().__init__(name,filename)

    def move(self, position):
        pass



