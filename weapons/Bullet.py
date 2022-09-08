import pygame

class Bullet:
    def __init__(self, x, y, down=False, speed=1):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = 4
        self.spent = False
        self.down = down
    
    def update(self, targets):
        if self.down:
            self.y += self.speed
        else:
            self.y -= self.speed

        for t in targets:
            xDistance = abs(self.x - t.x)
            yDistance = abs(self.y - t.y)
            if (xDistance + yDistance) < self.size:
                t.takeDamage()

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x - self.size / 2, self.y - self.size / 2, self.size, self.size))