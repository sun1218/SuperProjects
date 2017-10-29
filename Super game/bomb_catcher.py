import sys, random, time, pygame
from pygame.locals import *

def print_text(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))
    
pygame.init()
screen = pygame.display.set_mode()