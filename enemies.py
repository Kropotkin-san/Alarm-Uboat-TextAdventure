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
		super().__init__(name="T7 Tanker",
			hp=60,
			damage=0,
			tonnage=10000
			)

class Lmerchant(Enemy):
	def __init__(self):
		super.()__init__(name="Large Merchant",
			hp=80,
			damage=20,
			tonnage=8500)

class Merchant(Enemy):
	def __init__(self):
		super.()__init__(name="Merchant",
			hp=70,
			damage=15,
			tonnage=6000,)

class Destroyer(Enemy):
	def __init__(self):
		super.()__init__(name="Destroyer",
			hp=40,
			damage=75,
			tonnage=3000,)

class Battleship(Enemy):
	def __init__(self):
		super.()__init__(name="Battleship",
			hp=200,
			damage=100,
			tonnage=38000,)

class Troop(Enemy):
	def __init__(self):
		super.()__init__(name="Troop Transport",
			hp=85,
			damage=0,
			tonnage=9000,)

