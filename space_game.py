import pygame

from logics import controls, aliens_controler
import consts
from characters.hero import Hero
from pygame.sprite import Group  # Creates a group of objects
from logics.scores import Scores
from logics.stats import Stats


def main():
    pygame.init()
    screen = pygame.display.set_mode(consts.WINDOW_SIZE)
    pygame.display.set_caption("Star Ido Wars")
    bg_color = consts.WHITE
    hero = Hero(screen)
    bullets = Group()
    aliens = Group()
    aliens_controler.create_army(screen, aliens)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        # describe all user actions in our game
        controls.events(screen, hero, bullets)
        # If stats.rin_game = False, we lose the game
        if stats.run_game:
            hero.hero_movement()
            bullets.update()
            controls.update(bg_color, screen, sc, hero, aliens, bullets)
            controls.disappearing_bullets(bullets)
            aliens_controler.collision_adjustment(stats, sc, aliens, bullets)
            aliens_controler.alien_revival(screen, aliens, bullets)
            aliens_controler.update_aliens(stats, screen, sc, hero, aliens, bullets)


if __name__ == '__main__':
    main()
