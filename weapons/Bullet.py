from util import distance
import pygame
import math

class Bullet:
    def __init__(self, x, y, angle=math.pi/2, speed=1):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.size = 4
        self.spent = False
    
    def update(self, targets):
        self.y -= math.sin(self.angle) * self.speed
        self.x += math.cos(self.angle) * self.speed

        if not self.spent:
            for t in targets:
                if distance(self, t) <= (t.size + self.size) / 2:
                    t.takeDamage()
                    self.spent = True

    def draw(self, screen):
        if not self.spent:
            pygame.draw.rect(screen, (180, 80, 80), (self.x - self.size / 2, self.y - self.size / 2, self.size, self.size))