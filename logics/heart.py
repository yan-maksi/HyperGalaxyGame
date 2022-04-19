import pygame


class Heart(pygame.sprite.Sprite):

    def __init__(self, screen):
        """lives of the main character"""
        super(Heart, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/heart.png')

        # transform the character on the rectangle of the screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


