import pygame
import sys

pygame.init() # tells pygame to look/listen for inputs and events

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Chomp!")

screen.fill((57, 165, 237)) # tuple of rgb values for color of the screen

pygame.draw.rect(screen, (100, 25, 0), (0, 380, 400, 400)) # color is rgb values, rect has x location, y location, height, width
sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(sand, (200, 200, 64, 64))
pygame.display.flip()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Thanks for playing!")
            pygame.quit() # stops process that pygame.init started
            sys.exit() # uber break
