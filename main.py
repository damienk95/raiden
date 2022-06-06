import pygame
from Game import Game
from util import WIDTH, HEIGHT

pygame.init()

screen = pygame.Surface((WIDTH, HEIGHT))
window = pygame.display.set_mode((WIDTH*8, HEIGHT*8))

clock = pygame.time.Clock()
game = Game()

while True:
    screen.fill((0, 0, 0))

    game.update()
    game.draw(screen, HEIGHT)

    window.blit(pygame.transform.scale(screen, window.get_rect().size), (0, 0))
    pygame.display.update()
    clock.tick(45)

