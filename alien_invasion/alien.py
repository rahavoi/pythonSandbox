import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent an allien"""

	def __init__(self, ai_settings, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#Load image
		self.image = pygame.image.load('ufo.png')
		self.image = pygame.transform.scale(self.image, (ai_settings.battleship_height, ai_settings.battleship_height))
		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien's exact position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	
	def check_edges(self):
		print("Ch!!!!")
		screen_rect = self.screen.get_rect()
		if(self.rect.right >= screen_rect.right or self.rect.left <= 0):
			return True	

	def blitme(self):
		self.screen.blit(self.image, self.rect)	

	def update(self):
		self.x += 3 * self.ai_settings.fleet_direction
		self.rect.x = self.x