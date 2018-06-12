import sys

import pygame

from alien import Alien
from settings import Settings
from ship import Ship
from bullet import Bullet

def check_events(ai_settings, ship, bullets):

	#Track keyboard and mouse events:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
				print('Thanks for playing! Come back soon!')
				sys.exit()

			if event.type == pygame.KEYDOWN:
				check_key_down_events(ship, ai_settings, ship.screen, bullets)

			if event.type == pygame.KEYUP:
				check_key_up_events(ship)

		if(ship.moving):
				move_ship(ship, ai_settings)					

def check_key_up_events(ship):
	ship.moving = False
				
def check_key_down_events(ship, ai_settings, screen, bullets):
	ship.keys_pressed = pygame.key.get_pressed()

	if(ship.keys_pressed[pygame.K_SPACE]):
		fire_bullet(bullets, ai_settings, screen, ship)	
	
	ship.moving = True

def move_ship(ship, ai_settings):
	if ship.keys_pressed[pygame.K_RIGHT] and ship.rect.right < ship.screen_rect.right:
		ship.rect.centerx += ai_settings.battleship_side_move_distance
	if ship.keys_pressed[pygame.K_LEFT] and ship.rect.left > 0:
		ship.rect.centerx -= ai_settings.battleship_side_move_distance
	if ship.keys_pressed[pygame.K_UP] and ship.rect.y > 0:
		ship.rect.centery -= ai_settings.battleship_side_move_distance
	if ship.keys_pressed[pygame.K_DOWN]:
		if(ship.rect.y < ai_settings.screen_height - ai_settings.battleship_height):
			ship.rect.centery += ai_settings.battleship_side_move_distance	

def create_fleet(ai_settings, screen, aliens):
		number_alliens_x = get_number_aliens_x(ai_settings)

		number_rows = get_number_rows(ai_settings)

		for row in range(number_rows):
			for alien_number in range(number_alliens_x):
				create_alien(ai_settings, screen, aliens, alien_number, row)

def get_number_aliens_x(ai_settings):
	available_space_x = ai_settings.screen_width - 2 * ai_settings.battleship_width
	number_alliens_x = int(available_space_x / (2 * ai_settings.battleship_width))
	return int(number_alliens_x / 2)

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	alien = Alien(ai_settings, screen)
	alien.x = ai_settings.battleship_width + 3 * ai_settings.battleship_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def get_number_rows(ai_settings):
	available_space_y = (ai_settings.screen_height - ( 3* ai_settings.battleship_height) - ai_settings.battleship_height )
	number_rows = int(available_space_y / (2 * ai_settings.battleship_height))
	return number_rows

def update_aliens(ai_settings, aliens):
	check_fleet_edges(ai_settings, aliens)
	aliens.update()

def check_fleet_edges(ai_settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break	

def change_fleet_direction(ai_settings, aliens):
	print("Changing direction!")
	"""Drop the entire fleet and change the fleet's direction."""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1
	print("Changed direction")	
	print(alien.ai_settings.fleet_direction)





def update_screen(ai_settings, screen, ship, aliens, bullets):
	screen.fill(ai_settings.bg_color)
	ship.draw()
	aliens.draw(screen)
	update_bullets(bullets)

	#Make the most recently drawn screen visible:
	pygame.display.flip()

def fire_bullet(bullets, ai_settings, screen, ship):
	if len(bullets) < ai_settings.bullets_allowed:
			new_bullet = Bullet(ai_settings, screen, ship)
			bullets.add(new_bullet)

def update_bullets(bullets):
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	bullets.update()



