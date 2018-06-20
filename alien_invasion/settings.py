class  Settings():
	"""docstring for  Settings"""
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (23, 80, 166)
		self.battleship_width = 22
		self.battleship_height = 45
		self.battleship_side_move_distance = 10

		self.bullet_speed_factor = 30
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = 173, 255, 47
		self.bullets_allowed = 10

		# 1 - right; -1 left
		self.fleet_direction = 1
		self.fleet_drop_speed = 20

		self.ship_limit = 3