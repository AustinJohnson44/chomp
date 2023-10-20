import pygame
from settings import *


class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.right_image = pygame.image.load("assets/images/orange_fish.png").convert()
        self.right_image.set_colorkey((0, 0, 0))

        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.left_image.set_colorkey((0, 0, 0))

        self.image = self.right_image

        self.x = x
        self.y = y
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_left:
            self.x -= 2
        elif self.moving_right:
            self.x += 2
        if self.moving_up:
            self.y -= 2
        elif self.moving_down:
            self.y += 2
        # make fish stay on screen
        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_WIDTH - TILE_SIZE:
            self.x = SCREEN_WIDTH - TILE_SIZE
        if self.y < 0:
            self.y = 0
        elif self.y > SCREEN_HEIGHT - TILE_SIZE*3:
            self.y = SCREEN_HEIGHT - TILE_SIZE*3

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
