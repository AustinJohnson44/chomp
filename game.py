import pygame
import sys
import random
import fish
from minnow import Minnow, minnows
from settings import *

pygame.init()  # tells pygame to look/listen for inputs and events

game_font = pygame.font.Font("assets/fonts/Sketch Gothic School.ttf", TITLE_SIZE)
screen = pygame.display.set_mode((SCREEN_WIDTH,
                                  SCREEN_HEIGHT))  # collapsed variables inside parenthesis
pygame.display.set_caption("Chomp!")
sand = pygame.image.load("assets/images/sand.png").convert()  # .convert() to make the background transparent
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
sand_top.set_colorkey((0, 0, 0))  # tells blit to ignore transparent pixels and use whatever color is behind them
seagrass = pygame.image.load("assets/images/seagrass.png").convert()
seagrass.set_colorkey((0, 0, 0))
score = 0

my_fish = fish.Fish(200, 200)  # create a new fish
for thing in range(NUM_MINNOWS):
    minnows.add(Minnow(random.randint(0, SCREEN_WIDTH - TILE_SIZE),
                       random.randint(0, WATER_BOTTOM - TILE_SIZE)))

background = screen.copy()  # makes a second copy of the screen/canvas
clock = pygame.time.Clock()


def draw_background():
    # make blue background
    background.fill(WATER_COLOR)
    # making a sandy bottom
    for i in range(SCREEN_WIDTH // TILE_SIZE):  # // to give quotient and not a float
        background.blit(sand, (TILE_SIZE * i, SCREEN_HEIGHT - TILE_SIZE))
        background.blit(sand_top, (TILE_SIZE * i, SCREEN_HEIGHT - TILE_SIZE * 2))

    # randomly place 4 pieces of grass along the bottom of the background
    for i in range(4):
        x = random.randint(0, 11) * TILE_SIZE
        y = random.randint(SCREEN_HEIGHT - 2 * TILE_SIZE, SCREEN_HEIGHT) - (0.5 * TILE_SIZE)
        background.blit(seagrass, (x, y))

    # drawing game title
    text = game_font.render("Chomp!", True, (79, 79, 79))
    background.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))


draw_background()

while len(minnows)>0:
    # listen for events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Thanks for playing!")
            pygame.quit()  # stops process that pygame.init started
            sys.exit()  # uber break - breaks out of everything

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_fish.moving_left = True
            if event.key == pygame.K_RIGHT:
                my_fish.moving_right = True
            if event.key == pygame.K_UP:
                my_fish.moving_up = True
            if event.key == pygame.K_DOWN:
                my_fish.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_fish.moving_left = False
            if event.key == pygame.K_RIGHT:
                my_fish.moving_right = False
            if event.key == pygame.K_UP:
                my_fish.moving_up = False
            if event.key == pygame.K_DOWN:
                my_fish.moving_down = False

    # update game objects
    my_fish.update()
    minnows.update()

    # check for collisions
    chomped_minnows = pygame.sprite.spritecollide(my_fish, minnows, True)
    score += len(chomped_minnows)
    if len(chomped_minnows) >= 1:
        print(f"{score} minnows have been chomped!")

    # draw game screen
    screen.blit(background, (0, 0))
    my_fish.draw(screen)

    minnows.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # locks game to 60fps
print("You ate all of the minnows!")
