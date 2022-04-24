import sys
import time
import pygame
from characters.alien import Alien


def collision_adjustment(stats, sc, aliens, bullets):
    """collision adjustment / 'True' - to remove both the bullet and the alien"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += 10

        sc.image_score()
        sc.image_heroes()
        stats.check_height_score(sc)


def alien_revival(screen, aliens, bullets):
    """ creating a new group of aliens after the death of a player"""
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)


def hero_kill(stats, screen, sc, hero, aliens, bullets):  # hero controller
    """clash of cannon and army"""
    if stats.hero_left > 0:
        stats.hero_left -= 1
        aliens.empty()
        sc.image_heroes()
        bullets.empty()
        create_army(screen, aliens)
        hero.create_hero()
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()


def update_aliens(stats, screen, sc, hero, aliens, bullets):
    """updates the position of the aliens"""
    aliens.update()
    if pygame.sprite.spritecollideany(hero, aliens):
        hero_kill(stats, screen, sc, hero, aliens, bullets)
    alien_check(stats, screen, sc, hero, aliens, bullets)


def alien_check(stats, screen, sc, hero, aliens, bullets):
    """checking if the army has reached the edge of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            hero_kill(stats, screen, sc, hero, aliens, bullets)
            break


def create_army(screen, aliens):
    """
    Creating an alien army
    :param screen: passing the screen parameters
    :param aliens: passing the alien class
    """
    alien = Alien(screen)

    # Calculate how many aliens can fit on the "x"-axis
    alien_width = alien.rect.width
    number_alien_x = int((700 - 2 * alien_width) / alien_width)

    # Calculate how many aliens can fit on the "y"-axis
    alien_height = alien.rect.height
    number_alien_y = int((800 - 100 - 2 * alien_height) / alien_height)

    for row_number in range(number_alien_y - 1):
        for alen_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + alien_width * alen_number
            alien.y = alien_height + alien_height * row_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (alien.rect.height * row_number)
            # add a group of aliens to the screen
            aliens.add(alien)
