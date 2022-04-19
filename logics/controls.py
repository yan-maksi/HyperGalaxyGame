import pygame
import sys
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
