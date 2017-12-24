import items
import world

class Player:
	def __init__(self):
		self.inventory = [items.Torpedo(),
						items.Gun()
						]
		self.hp = 100
		self.x = 0
		self.y = 0		

	def print_inventory(self):
		print("Inventory:")
		for item in self.inventory:
			print('* ' + str(item))

	def is_alive(self):
		return self.hp > 0

	def move(self, dx ,dy):
		self.x += dx
		self.y += dy

	def move_North(self):
		self.move(dx = 0, dy = -1)

	def move_South(self):
		self.move(dx = 0, dy = 1)

	def move_East(self):
		self.move(dx = 1, dy = 0)

	def move_West(self):
		self.move(dx = -1, dy = 0)