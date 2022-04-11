import pygame
from pygame.sprite import Sprite


class Hero(Sprite):

    def __init__(self, screen):
        """Creating the logic of the main character"""
        super(Hero, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/Game_person.png')

        # transform the character on the rectangle of the screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # make the movement smoother, so you can put a float number
        self.center = float(self.screen_rect.centerx)

        # the position of the character
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # character movement buttons
        self.mright = False
        self.mleft = False

    def hero_view(self):
        """display the hero on the screen"""
        self.screen.blit(self.image, self.rect)

    def hero_movement(self):
        """character relocation update"""

        # character move RIGHT
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 2.5

        # character move LEFT
        if self.mleft and self.rect.left > 0:
            self.center -= 2.5

        self.rect.centerx = self.center

    def create_hero(self):
        """Creates the hero anew after death"""
        self.center = self.screen_rect.centerx #-----------------------
