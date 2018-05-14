import game_functions as gf

import pygame
import sys

from settings import Settings
from ship import Ship

def run_game():
	#Initialize game
	pygame.init()

	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

	# Make a ship.
	ship = Ship(screen)	

	#Main loop for the game:
	while  True:
		gf.check_events(ai_settings, ship)
		gf.update_screen(ai_settings, screen, ship)


run_game()				

