import pygame
import consts


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, hero) :
        """
        Bullet motion

        :param screen: this parameter to display the bullet on the screen
        :param hero_location: x,y of the hero
        """
        super(Bullet, self).__init__()
        self.screen = screen
        # dimensions of the bullet
        self.rect = pygame.Rect(0, 0, 2, 12)
        # color of the bullet
        self.color = consts.RED
        # bullet speed
        self.speed = 4
        # bullet location
        self.rect.centerx = hero.rect.centerx
        self.rect.top = hero.rect.top
        self.y = float(self.rect.y)

    def bullet_motion(self):
        """upward motion of the bullet"""
        self.y -= self.speed
        self.rect.y = self.y

