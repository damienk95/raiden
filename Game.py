from planes.Enemy import Enemy
from planes.Player import Plane
from util import WIDTH, HEIGHT
import pygame
import random

class Game:

    def __init__(self):
        self.enemies = []
        self.waveSize = 1
        self.player = Plane(WIDTH / 2, HEIGHT - 20)

    def generateEnemies(self):
        if len(self.enemies) == 0:
            for i in range(self.waveSize):
                spacing = WIDTH / (1 + self.waveSize)
                x = spacing * (1 + i)
                self.enemies.append(Enemy(x, 10))
            self.waveSize = self.waveSize + 1
    
    def update(self):
        self.cleanGarbage()
        self.generateEnemies()

        self.player.update(self.enemies)

        for e in self.enemies:
            e.update(self.player)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

    def cleanGarbage(self):
        self.enemies = [e for e in self.enemies if not e.dead]
        self.player.bullets = [b for b in self.player.bullets if not b.spent]

        for e in self.enemies:
            e.bullets = [b for b in e.bullets if not b.spent]

    
    def draw(self, screen, screenHeight):
        self.player.draw(screen)
        for e in self.enemies:
            e.draw(screen)
