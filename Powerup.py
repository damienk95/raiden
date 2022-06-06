from math import dist
from util import WIDTH, HEIGHT, bushSprite, distance

class Powerup:
    def __init__(self, x, y):
        self.sprite = bushSprite
        self.vx = 1
        self.vy = 1
        self.x = x
        self.y = y
        self.size = 8
        self.spent = False
    
    def update(self, player):
        if distance(self, player) < (self.size + player.size) / 2:
            player.spread += 1
            self.spent = True
            
        if self.x >= WIDTH:
            self.vx = -1
        if self.x <= 0:
            self.vx = 1
        if self.y >= HEIGHT:
            self.vy = -1
        if self.y <= 0:
            self.vy = 1
        
        self.x += self.vx
        self.y += self.vy
    
    def draw(self, screen):
        screen.blit(self.sprite, (self.x - self.size/2, self.y - self.size/2))