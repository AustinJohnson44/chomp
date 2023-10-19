import pygame


class Fish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/images/orange_fish.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.x = x
        self.y = y
        print("I am a brand new fish :) ")

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def move_up(self):
        self.y -= 10

    def move_down(self):
        self.y += 10

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
