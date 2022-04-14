import pygame
import controls
from hero import Hero
from pygame.sprite import Group  # Creates a group of objects
from scores import Scores
from stats import Stats
import varibbles


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(varibbles.WINDOW_SIZE)
    pygame.display.set_caption("Star Ido Wars")
    bg_color = varibbles.WHITE
    hero = Hero(screen)
    bullets = Group()
    aliens = Group()
    controls.create_army(screen, aliens)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        # describe all user actions in our game
        controls.events(screen, hero, bullets)
        # If stats.rin_game = False, we lose the game
        if stats.run_game:
            hero.hero_movement()
            bullets.update()
            controls.update(bg_color, screen, stats, sc, hero, aliens, bullets)
            controls.disappearing_bullets(screen, stats, sc, aliens, bullets)
            controls.update_aliens(stats, screen, sc, hero, aliens, bullets)
