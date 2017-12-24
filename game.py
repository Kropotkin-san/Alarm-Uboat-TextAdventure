from player import Player
import world
from collections import OrderedDict

def play():
	print("Alarm!")
	player = Player()
	while True:
		try:
			room = world.tile_at(player.x, player.y)
			print(room.intro_text())
			room.modify_player(player)
			choose_action(room, player)

		except KeyboardInterrupt:
			print("")
			exit()
		except EOFError:
			print("")
			exit()

def get_available_actions(room, player):
	actions = OrderedDict()
	print("What are your orders Herr Kaleun? Available orders are:")
	if player.inventory:
		action_adder(actions, 'i', player.print_inventory, "Print Inventory")
	if isinstance(room, world.GenericWarshipTile) and room.enemy.is_alive():
		action_adder(actions, 'a', player.attack, "Attack")
	if isinstance(room, world.GenericMerchantTile) and room.enemy.is_alive():
		action_adder(actions, 'a', player.attack, "Attack")
	else:
		if world.tile_at(room.x, room.y -1):
			action_adder(actions, 'n', player.move_North, "Go North")
		if world.tile_at(room.x, room.y +1):
			action_adder(actions, 's', player.move_South, "Go South")
		if world.tile_at(room.x +1, room.y):
			action_adder(actions, 'e', player.move_East, "Go East")
		if world.tile_at(room.x -1, room.y):
			action_adder(actions, 'w', player.move_West, "Go West")
		return actions

def action_adder(action_dict, hotkey, action, name):
	action_dict[hotkey.lower()] = action
	action_dict[hotkey.upper()] = action
	print("{}: {}".format(hotkey, name))

def choose_action(room, player):
	action = None
	while not action:
		available_actions = get_available_actions(room, player)
		action_input = input("Orders: ")
		action = available_actions.get(action_input)
		if action:
			action()
		else:
			print("Invalid Orders!")
play()