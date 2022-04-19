import pygame.font
import pygame
import consts
from logics.heart import Heart
from pygame.sprite import Group


class Scores:
    def __init__(self, screen, stats):
        """storing player's scoring"""

        self.screen = screen
        self.screen_rect = screen.get_rect
        # connecting player statistics
        self.stats = stats
        self.text_color = consts.RED
        self.font = pygame.font.SysFont('None', 35)

        self.heart_y = 0
        self.heart_x = 80

        self.screen_of_bill_x = 640
        self.screen_of_bill_y = 20

        self.image_score()
        self.image_heroes()
        self.image_height_score()

    def image_score(self):
        """converts text into a graphical image"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, consts.WHITE)
        self.score_rect = self.score_img.get_rect()

    def image_height_score(self):
        """converts the record to a graphical representation"""
        self.height_score_image = self.font.render(str(self.stats.height_score), True, self.text_color, consts.WHITE)
        self.height_score_rect = self.height_score_image.get_rect()

    def image_heroes(self):
        """"amount of life"""
        self.heroes = Group()
        for hero_number in range(self.stats.hero_left):
            hart = Heart(self.screen)
            hart.rect.x = self.heart_x + hero_number * hart.rect.width
            hart.rect.y = self.heart_y
            self.heroes.add(hart)

    def show_score(self):
        """bill display"""
        self.screen.blit(self.score_img, (self.screen_of_bill_x, self.screen_of_bill_y))
        self.screen.blit(self.height_score_image, self.height_score_rect)
        self.heroes.draw(self.screen)
