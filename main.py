import pygame
import consts

from logics.stats import Stats
from pygame.sprite import Group
from logics.screen_objects import ScreenObjects
from characters.hero import Hero

from logics import controls
from logics import aliens_controler


def main():
    pygame.init()
    pygame.display.set_caption("Star Ido Wars")
    stats = Stats()
    sc = ScreenObjects(pygame.display.set_mode(consts.WINDOW_SIZE), stats)
    bg_color = consts.WHITE
    hero = Hero(sc.screen.get_rect())
    bullets = Group()
    aliens = Group()
    aliens_controler.create_army(sc.screen, aliens)

    while True:
        # describe all user actions in our game
        controls.events(sc.screen, hero, bullets)
        # If stats.rin_game = False, we lose the game
        if stats.run_game:
            hero.hero_movement()
            sc.update(bg_color, hero, aliens, bullets)
            bullets.update()
            aliens_controler.collision_adjustment(stats, sc, aliens, bullets)
            aliens_controler.alien_revival(sc.screen, aliens, bullets)
            aliens_controler.update_aliens(stats, sc.screen, sc, hero, aliens, bullets)


if __name__ == '__main__':
    main()
