import pygame


class Alien(pygame.sprite.Sprite):

    def __init__(self, screen):
        """
        mark the basic parameters of the alien. He is the antagonist of the protagonist, he must move on the
        protagonist in order to kill him or go behind the black line
        :param screen: mark his location
        """
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien.png')

        # transform the alien into a rectangle
        self.rect = self.image.get_rect()

        # place the alien on the coordinate axis
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # alien speed
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """display the alien on the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """moving aliens to the player"""
        speed_alien = 0.1
        self.y += speed_alien
        self.rect.y = self.y
