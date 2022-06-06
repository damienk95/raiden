import math
import os
import time
import pygame

WIDTH = 100
HEIGHT = 100

def distance(a, b):
    x = a.x - b.x
    y = a.y - b.y
    return math.sqrt(x**2 + y**2)

class RateLimiter:
    def __init__(self):
        self.lastShot = 0

    def shoot(self, cooldown):
        if time.time() - self.lastShot > cooldown:
            self.lastShot = time.time()
            return True
        return False


planeSprite =      pygame.image.load(os.path.join('images', 'plane', 'plane.png'))
planeLeftSprite =  pygame.image.load(os.path.join('images', 'plane', 'planeLeft.png'))
planeRightSprite = pygame.image.load(os.path.join('images', 'plane', 'planeRight.png'))
planeBoomSprite = pygame.image.load(os.path.join('images', 'plane', 'boom.png'))

bushSprite = pygame.image.load(os.path.join('images', 'map', 'bush.png'))

