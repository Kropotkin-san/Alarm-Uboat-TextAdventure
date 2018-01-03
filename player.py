import items
import world
import random

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

	def attack1(self):
		room = world.tile_at(self.x, self.y)
		enemy = room.enemy
		print("You fire a torpedo at the {}".format(enemy.name))
		r = random.random()
		if r < 0.15:
			print("Your torpedo misses!")
		elif r < 0.65:
			print("We hit her Herr Kaleun!")
			enemy.hp -= 60
			if not enemy.is_alive():
				print("Wir hab ihn! We sunk the {}".format(enemy.name))
			else:
				print("She is damaged herr Kaleun!")
		elif r < 1:
			print("Critical hit Herr Kaleun!")
			enemy.hp -= 90
			if not enemy.is_alive():
				print("Wir hab ihn! We sunk the {}".format(enemy.name))
			else:
				print("She is damaged herr Kaleun!")

	def exit(self):
		print("Auf Wiedersehn Herr Kaleun!")
		exit()

	def attack2(self):
		room = world.tile_at(self.x, self.y)
		enemy = room.enemy
		print("You fire the deck gun at the {}".format(enemy.name))
		r = random.random()
		if r < 0.15:
			print("Your deck gun misses!")
		elif r < 0.5:
			print("We hit her above the water line Herr Kaleun!")
			enemy.hp -= 30
			if not enemy.is_alive():
				print("Wir hab ihn! We sunk the {}".format(enemy.name))
			else:
				print("She is damaged herr Kaleun!")
		elif r < 75:
			print("We hit her at the water line Herr Kaleun!")
			enemy.hp -= 60
			if not enemy.is_alive():
				print("Wir hab ihn! We sunk the {}".format(enemy.name))
			else:
				print("She is damaged herr Kaleun!")
		elif r < 1:
			print("Critical hit at the engine Herr Kaleun!")
			enemy.hp -= 70
			if not enemy.is_alive():
				print("Wir hab ihn! We sunk the {}".format(enemy.name))
			else:
				print("She is damaged herr Kaleun!")
		

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