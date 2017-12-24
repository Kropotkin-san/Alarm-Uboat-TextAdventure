from player import Player
import world

def play():
	print("Alarm!")
	player = Player()
	while True:
		try:
			room = world.tile_at(player.x, player.y)
			print(room.intro_text())
			action_input = get_player_command()
			if action_input.upper() == "NORTH" or action_input.upper() == "N":
				player.move_North()
			elif action_input.upper() == "EAST" or action_input.upper() == "E":
				player.move_East()
			elif action_input.upper() == "WEST" or action_input.upper() == "W":
				player.move_West()
			elif action_input.upper() == "SOUTH" or action_input.upper() == "S":
				player.move_South()
			elif action_input.upper() == "I" or action_input.upper() == "INVENTORY":
				player.print_inventory()
			elif action_input.upper() == "EXIT":
				exit()
			else:
				print("Invalid command. Try again.")

		except KeyboardInterrupt:
			print("")
			exit()
		except EOFError:
			print("")
			exit()

def get_player_command():
	return input('Orders: ')

def get_available_actions(room, player):
	actions = OrderedDict()
	print("What are your orders Herr Kaleun? ")
	if player.inventory:
		action_adder(actions, 'i', 'I', player.print_inventory, "Print Inventory")
	if isinstance(room, world.GenericWarshipTile, world.GenericMerchantTile) and room.enemy.is_alive():
		action_adder(actions, 'a', 'A', player.attack, "Attack")
	else:
		if world.tile_at(room.x, room.)

play()