import pygame


class Alien(pygame.sprite.Sprite):
    def __init__(self, screen):
        """
        Alien object with location and speed
        :param screen: the window where the alien is
        """
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien.png')

        # transform the alien into a rectangle
        self.rect = self.image.get_rect()

        # place the alien on the coordinate axis
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = 0.1

    def draw(self):
        """display the alien on the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """moving aliens to the player"""
        self.y += self.speed
        self.rect.y = self.y
