import pygame
import sys

# Dimensions
TILE_SIZE = 64  # tiles are square so height==width
SCREEN_WIDTH = 12*TILE_SIZE
SCREEN_HEIGHT = 8*TILE_SIZE
SAND_HEIGHT = 20

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
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
sand_top.set_colorkey((0, 0, 0))  # tells blit to ignore transparent pixels and use whatever color is behind them

# BLIT SAND TILES ACROSS THE BOTTOM OF THE SCREEN
for i in range(SCREEN_WIDTH // TILE_SIZE):  # // to give quotient and not a float
    screen.blit(sand, (TILE_SIZE * i, SCREEN_HEIGHT - TILE_SIZE))
    screen.blit(sand_top, (TILE_SIZE * i, SCREEN_HEIGHT - TILE_SIZE*2))

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Thanks for playing!")
            pygame.quit()  # stops process that pygame.init started
            sys.exit()  # uber break - breaks out of everything

    pygame.display.flip()
