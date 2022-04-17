import pygame
import sys
import time
import aliens_controler
from objects.bullet import Bullet


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


def update(bg_color, screen, sc, hero, aliens, bullets):
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
    pygame.draw.line(screen, (0, 0, 0), (0, 600), (700, 600), width=1)
    sc.show_score()

    for bullet in bullets.sprites():
        bullet.bullet_motion()
        bullet.draw_bullet()

    hero.hero_view()
    aliens.draw(screen)
    pygame.display.flip()


def disappearing_bullets(bullets):
    """update bullet positions (bullets will disappear when outside the screen)"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def hero_kill(stats, screen, sc, hero, aliens, bullets):
    """clash of cannon and army"""
    if stats.hero_left > 0:
        stats.hero_left -= 1
        aliens.empty()
        sc.image_heroes()
        bullets.empty()
        aliens_controler.create_army(screen, aliens)
        hero.create_hero()
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()