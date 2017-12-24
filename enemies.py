class Enemy:
	def __init__(self,damage,hp,name,tonnage):
		self.damage = damage
		self.hp = hp
		self.name = name
		self.tonnage = tonnage

	def is_alive(self):
		return self.hp > 0

class Tanker(Enemy):
	def __init__(self):
		super().__init__(name="Tanker",
			hp=50,
			damage=0,
			tonnage=10000
			)

#class (Enemy):
#	def __init__(self):
#		super().__init__(name="",
#			hp=,
#			damage=,
#			tonnage=)

class Lmerchant(Enemy):
	def __init__(self):
		super().__init__(name="Large Merchant",
			hp=80,
			damage=15,
			tonnage=8500)

class Merchant(Enemy):
	def __init__(self):
		super().__init__(name="Merchant",
			hp=70,
			damage=10,
			tonnage=6000,)

class Destroyer(Enemy):
	def __init__(self):
		super().__init__(name="Destroyer",
			hp=40,
			damage=75,
			tonnage=3000,)

class Troop(Enemy):
	def __init__(self):
		super().__init__(name="Troop Transport",
			hp=85,
			damage=0,
			tonnage=9000,)
class Submarine(Enemy):
	def __init__(self):
		super().__init__(name="British T-Class Submarine",
			hp=20,
			damage=35,
			tonnage=1000,)