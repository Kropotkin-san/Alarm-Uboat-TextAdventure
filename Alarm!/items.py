class Item():
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def __str__(self):
		return "{} {}".format(self.name, self.description)

class Tonnage(Item):
	def __init__(self, amt):
		self.amt = amt
		super().__init__(name="Tonnage",
							description="The amount of tons you have sunken. The more the better Herr Kaleun!")

class Weapon(Item):
	def __init__(self, damage, description, name, ammunition):
		self.damage = damage
		self.ammunition = ammunition
		super().__init__(name, description)

	
	def __str__(self):
		return "{} {} Amount:{}".format(self.name, self.description, self.ammunition)

class Torpedo(Weapon):
	def __init__(self):
		super().__init__(name = "T2 Torpedo",
			description = "Updated version of the T1. Powered by an electric engine.",
			damage = 100,
			ammunition = 14)

class Gun(Weapon):
	def __init__(self):
		super().__init__(name = "88mm Deck Gun",
			description = "Deck cannon, mostly used for attacking unarmed merchants.",
			damage = 45,
			ammunition = 120)