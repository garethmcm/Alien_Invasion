import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf

def run_game():
    # initialise game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics
    stats = GameStats(ai_settings)

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in
    bullets = Group()
    aliens = Group()

    # Create fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start main loop for game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()