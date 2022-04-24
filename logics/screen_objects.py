import pygame.font
import pygame
import consts
from logics.heart import Heart
from pygame.sprite import Group

from logics.stats import Stats


class ScreenObjects:
    def __init__(self, screen, stats: Stats):
        """storing player's scoring"""

        self.heroes = None
        self.score_img = None
        self.score_rect = None
        self.height_score_rect = None
        self.height_score_image = None

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

        # drawing imagen on the screen
        self.draw_images()

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

    def draw_images(self, bullets=None):
        self.image_score()
        self.image_heroes()
        self.image_height_score()

        if bullets is not None:
            self.draw_bullet(bullets)

    def update(self, bg_color, hero, aliens, bullets):  # screen controller
        """
        screen update
        *Args:
             bg_color: assign the background
             screen: passing the screen parameters
             stats: player statistic
             sc: displaying player statistics on the screen
             hero: place the main character on the screen
             alien: display the alien on the screen
             bullets: placing the bullet behind the rear hero
        """
        self.screen.fill(bg_color)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 600), (700, 600), width=1)
        self.show_score()

        for bullet in bullets.sprites():
            bullet.bullet_motion()

        # drawing imagen on the screen
        self.draw_images(bullets)

        hero.hero_view()
        aliens.draw(self.screen)
        pygame.display.flip()

    def draw_bullet(self, bullets):
        """drawing a bullet on the screen"""
        for bullet in bullets:
            if bullet.rect.bottom <= 0:
                print("0")
                bullets.remove(bullet)
            else:
                pygame.draw.rect(self.screen, consts.RED, bullet.rect)
