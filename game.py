import pygame
import time

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Chomp!")

screen.fill((57, 165, 237))
pygame.draw.rect(screen, (100, 25, 0), (0, 380, 400, 400))
pygame.draw.rect(screen, (0, 255, 0), (200, 200, 25, 25))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Nope. Can't quit today.")