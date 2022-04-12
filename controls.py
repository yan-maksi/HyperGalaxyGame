import pygame
import sys
import time
from bullet import Bullet
from alien import Alien


def events(screen, hero, bullets):
    """game event handling"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Create actions (triggers) when pressing buttons
        elif event.type == pygame.KEYDOWN:
            # character movement to the right - right key (->)
            if event.key == pygame.K_RIGHT:
                hero.mright = True

            # character movement to the left - left key (<-)
            if event.key == pygame.K_LEFT:
                hero.mleft = True

            # (Shooting) Firing a bullet - space bar
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, hero)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            # character movement to the right - right key (->)
            if event.key == pygame.K_RIGHT:
                hero.mright = False

            # character movement to the left - left key (<-)
            if event.key == pygame.K_LEFT:
                hero.mleft = False


def update(bg_color, screen, stats, sc, hero, aliens, bullets):
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
    screen.fill(bg_color)
    sc.show_score()

    for bullet in bullets.sprites():
        bullet.bullet_motion()
        bullet.draw_bullet()

    hero.hero_view()
    aliens.draw(screen)
    pygame.display.flip()


def disappearing_bullets(screen, stats, sc, aliens, bullets):
    """update bullet positions (bullets will disappear when outside the screen)"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))

    # collision adjustment / 'True' - to remove both the bullet and the alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += 10
        sc.image_score()
        sc.image_heros()
        chek_hight_score(stats, sc)

    # creating a new group of aliens after the death of a player
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)


def hero_kill(stats, screen, sc, hero, aliens, bullets):
    """clash of cannon and army"""
    if stats.hero_left > 0:
        stats.hero_left -= 1
        aliens.empty()
        sc.image_heros()
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
        print('!!!!!!!!')
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
    alien_heigth = alien.rect.height
    number_alien_y = int((800 - 100 - 2 * alien_heigth) / alien_heigth)

    for row_number in range(number_alien_y - 1):
        for alen_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + alien_width * alen_number
            alien.y = alien_heigth + alien_heigth * row_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (alien.rect.height * row_number)
            # add a group of aliens to the screen
            aliens.add(alien)


def chek_hight_score(stats, sc):
    """"Check for new records"""
    if stats.score > stats.hight_score:
        stats.hight_score = stats.score
        sc.image_hight_score()
        with open('hightscore', 'w') as f:
            f.write(str(stats.hight_score))
