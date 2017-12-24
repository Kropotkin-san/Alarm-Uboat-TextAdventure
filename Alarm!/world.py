import enemies
import items
import random

class Maptile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def intro_text(self):
    raise NotImplementedError()
 
def modify_player(self, player):
    raise NotImplementedError()

class StartingTile(Maptile):
	def intro_text(self):
		return """
You're in a french subpen ready to depart on a war patrol. You can travel to the south or to the east. Your orders are to engage enemy shipping and sink as many merchants as conditions allow.
Gute Jagd Herr Kaleun!

"""

	def modify_player(self, player):
		pass

#class EnemyTile(Maptile):
#	def __init__(self, x, y, enemy):
#		self.enemy = enemy
#		super().__init__(x, y)
#
#	def modify_player(self, the_player):
#		if self.enemy.is_alive():
#			the_player.hp = the_player.hp - self.enemy.damage
#			print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

class EmptySea(Maptile):
	def intro_text(self):
		return """Nothing but sea herr Kaleun.

		"""
	def modify_player(self, player):
		pass

class GenericMerchantTile(Maptile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.50:
			self.enemy = enemies.Merchant()
		elif r < 0.75:
			self.enemy = enemies.Lmerchant()
		else:
			self.enemy = enemies.Tanker()

		super().__init__(x, y)

	def intro_text(self):
		if self.enemy.is_alive() and self.enemy != None:
			return"""A {} has been spotted herr Kaleun!

			""".format(self.enemy.name)
		else:
			return"""Here lies the wreckage of the {} we sunk.

			""".format(self.enemy.name)

class GenericWarshipTile(Maptile):
	def __init__(self, x, y):
		r = random.random()
		if r < 0.65:
			self.enemy = enemies.Destroyer()
		else:
			self.enemy = enemies.Submarine()

		super().__init__(x, y)

	def intro_text(self):
		if self.enemy.is_alive():
			return"""A {} has been spotted herr Kaleun!

			""".format(self.enemy.name)
		else:
			return"""Here lies the wreckage of the {} we sunk.

			""".format(self.enemt.name)

world_map = [
	[StartingTile(0,0), EmptySea(1,0), GenericMerchantTile(2,0), EmptySea(3,0), EmptySea(4,0)],
	[EmptySea(0,1), GenericMerchantTile(1,1), GenericWarshipTile(2,1), EmptySea(3,1), EmptySea(4,1)],
	[GenericWarshipTile(0,2), EmptySea(1,2), EmptySea(2,2), GenericMerchantTile(3,2), EmptySea(4,2)],
	[EmptySea(0,3), EmptySea(1,3), GenericMerchantTile(2,3), GenericWarshipTile(3,3), GenericMerchantTile(4,3)],
	[GenericMerchantTile(0,4), GenericMerchantTile(1,4), EmptySea(2,4), EmptySea(3,4), EmptySea(4,4)]
]

def tile_at(x, y):
	if x < 0 or y < 0:
		return None
	try:
		return world_map[x][y]
	except IndexError:
		return None