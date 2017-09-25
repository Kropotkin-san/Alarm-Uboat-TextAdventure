import enemies
import items

class Maptile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def intro_text(self):
	raise NotImplementedError()

def modify_player(self, player):
	raise NotImplementedError()


class StartingRoom(Maptile):
	def intro_text(self):
		return """
		You're in a french subpen ready to depart on a war patrol. Your orders are to engage enemy shipping and sink as many merchants as conditions allow. 