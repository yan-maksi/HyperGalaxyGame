import pygame.font
import varibbles
from hero import Hero
from pygame.sprite import Group


class Scores:
    """playful output"""

    def __init__(self, screen, stats):
        """Doing a player's scoring"""
        self.heros = None
        self.screen = screen
        self.screen_rect = screen.get_rect
        # connecting player statistics
        self.stats = stats
        # color of the text
        self.text_color = varibbles.RED
        # text font
        self.font = pygame.font.SysFont(None, 35)
        self.image_score()
        self.image_heros()

    def image_score(self):
        """converts text into a graphical image"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, varibbles.WHITE)
        self.score_rect = self.score_img.get_rect()
        # screen indents
        self.score_rect.right = 40
        self.score_rect = 20


    def image_heros(self):
        """"amount of life"""
        self.heros = Group()
        for hero_number in range(self.stats.hero_left):
            hero = Hero(self.screen)
            hero.rect.x = 15 + hero_number * hero.rect.width
            hero.rect.y = 20
            self.heros.add(hero)

    def show_score(self):
        """bill display"""
        self.screen.blit(self.score_img, (680,0))
        self.heros.draw(self.screen)