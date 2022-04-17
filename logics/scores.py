import pygame.font
import consts
from logics.heart import Heart
from pygame.sprite import Group


class Scores:
    """playful output"""

    def __init__(self, screen, stats):
        """Doing a player's scoring"""
        self.heroes = None
        self.height_score_rect = None
        self.height_score_image = None
        self.score_rect = None
        self.score_img = None
        self.screen = screen
        self.screen_rect = screen.get_rect
        # connecting player statistics
        self.stats = stats
        # color of the text
        self.text_color = consts.RED
        # text font
        self.font = pygame.font.SysFont('None', 35)
        self.image_score()
        self.image_heroes()
        self.image_height_score()

    def image_score(self):
        """converts text into a graphical image"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, consts.WHITE)
        self.score_rect = self.score_img.get_rect()
        # screen indents
        self.score_rect.right = 40
        self.score_rect = 20

    def image_height_score(self):
        """converts the record to a graphical representation"""
        self.height_score_image = self.font.render(str(self.stats.height_score), True, self.text_color, consts.WHITE)
        self.height_score_rect = self.height_score_image.get_rect()
        self.height_score_rect.top = 20

    def image_heroes(self):
        """"amount of life"""
        self.heroes = Group()
        for hero_number in range(self.stats.hero_left):
            hero = Heart(self.screen)
            hero.rect.x = 80 + hero_number * hero.rect.width
            hero.rect.y = 0
            self.heroes.add(hero)

    def show_score(self):
        """bill display"""
        self.screen.blit(self.score_img, (640, 20))
        self.screen.blit(self.height_score_image, self.height_score_rect)
        self.heroes.draw(self.screen)
