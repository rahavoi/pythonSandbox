import sys

import pygame

from settings import Settings
from ship import Ship

def check_events(ai_settings, ship):
	#Track keyboard and mouse events:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print('Thanks for playing! Come back soon!')
				sys.exit()

			if event.type == pygame.KEYDOWN:
				ship.moving = True
				ship.keys_pressed = pygame.key.get_pressed()

			if event.type == pygame.KEYUP:
				ship.moving = False

		if(ship.moving):
				move_ship(ship, ai_settings)					

				

def move_ship(ship, ai_settings):
	if ship.keys_pressed[pygame.K_RIGHT]:
		ship.rect.centerx += ai_settings.battleship_side_move_distance
	if ship.keys_pressed[pygame.K_LEFT]:
		ship.rect.centerx -= ai_settings.battleship_side_move_distance
	if ship.keys_pressed[pygame.K_UP]:
		ship.rect.centery -= ai_settings.battleship_side_move_distance
	if ship.keys_pressed[pygame.K_DOWN]:
		if(ship.rect.y < ai_settings.screen_height - ai_settings.battleship_height):
			ship.rect.centery += ai_settings.battleship_side_move_distance	


def update_screen(ai_settings, screen, ship):
	screen.fill(ai_settings.bg_color)
	ship.draw()

	#Make the most recently drawn screen visible:
	pygame.display.flip()				