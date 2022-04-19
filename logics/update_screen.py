import pygame


def update(bg_color, screen, sc, hero, aliens, bullets):  # screen controller
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
