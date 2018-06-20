import pygame

from settings import Settings

class Ship():
	"""docstring for Ship"""
	def __init__(self, screen):
		self.screen = screen

		ai_settings = Settings()

		#Load the ship image 
		self.image = pygame.image.load('rocket.png')
		self.image = pygame.transform.scale(self.image, (ai_settings.battleship_width, ai_settings.battleship_height))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.moving = False
		self.keys_pressed = None

	def draw(self):
		"""Draw the ship at the current location"""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Center the ship on the screen."""
		self.center = self.screen_rect.centerx	


