from Map import Map
from planes.Enemy import Enemy
from planes.Player import Plane
from Powerup import Powerup
from util import WIDTH, HEIGHT
import pygame
import random

class Game:

    def __init__(self):
        self.map = Map()
        self.offsetY = 0
        self.enemies = []
        self.powerups = []
        self.waveSize = 1
        self.player = Plane(WIDTH / 2, HEIGHT - 20)

    def generateEnemies(self):
        if len(self.enemies) == 0:
            for i in range(self.waveSize):
                spacing = WIDTH / (1 + self.waveSize)
                x = spacing * (1 + i)
                self.enemies.append(Enemy(x, 10))
            self.powerups.append(Powerup(random.randrange(0, 100), random.randrange(0, 100)))
            self.waveSize += 1
    
    def update(self):
        self.cleanGarbage()
        self.generateEnemies()
        self.offsetY += 1

        self.player.update(self.enemies)

        for e in self.enemies:
            e.update(self.player)
        for p in self.powerups:
            p.update(self.player)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

    def cleanGarbage(self):
        self.enemies = [e for e in self.enemies if not e.dead]
        self.powerups = [p for p in self.powerups if not p.spent]
        self.player.bullets = [b for b in self.player.bullets if not b.spent]

        for e in self.enemies:
            e.bullets = [b for b in e.bullets if not b.spent]

    
    def draw(self, screen, screenHeight):
        self.map.draw(screen, screenHeight, self.offsetY)
        self.player.draw(screen)
        for e in self.enemies:
            e.draw(screen)

        for p in self.powerups:
            p.draw(screen)