import pygame
import sys

# Dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SAND_HEIGHT = 20
TILE_SIZE = 64  # tiles are square so height==width

# Colors
WATER_COLOR = (57, 165, 237)  # color is rgb values, rect has left position, top position, width, and height
SAND_COLOR = (100, 25, 0)

pygame.init()  # tells pygame to look/listen for inputs and events

screen = pygame.display.set_mode((SCREEN_WIDTH,
                                  SCREEN_HEIGHT))  # collapsed variables inside parenthesis
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)

pygame.draw.rect(screen, SAND_COLOR, (0,
                                      SCREEN_HEIGHT-SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))
sand = pygame.image.load("assets/images/sand.png").convert()  # .convert() to make the background transparent
screen.blit(sand, (SCREEN_WIDTH/2 - TILE_SIZE/2,
                   SCREEN_HEIGHT/2 - TILE_SIZE/2))

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Thanks for playing!")
            pygame.quit()  # stops process that pygame.init started
            sys.exit()  # uber break - breaks out of everything

    pygame.display.flip()
