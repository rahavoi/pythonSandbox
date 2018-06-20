import game_functions as gf

import pygame
from pygame.sprite import Group
import sys

from alien import Alien
from settings import Settings
from ship import Ship

from game_stats import GameStats

def run_game():
	#Initialize game
	pygame.init()

	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

	# Make a ship.
	ship = Ship(screen)	

	stats = GameStats(ai_settings)

	bullets = Group()
	aliens = Group()

	gf.create_fleet(ai_settings, screen, ship, aliens)

	#Main loop for the game:
	while  True:
		gf.check_events(ai_settings, ship, bullets)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
		gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)


run_game()				

