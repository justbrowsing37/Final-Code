from classes import GameState, Color
from game_map import usable_items, game_map
from ui import save_game


#USE ACSII SYNTAX     GO GO GO GO GO



def show_available_moves(current_room, game_map, player_inventory):
    current_room_info = game_map[current_room]
    print("Available moves:")
    
    # Display available directions to move
    print("Directions:")
    for direction in current_room_info["Exits"]:
        print(f"- Move {direction} to go to {current_room_info['Exits'][direction]}")
    
    # Display available items to take in the room
    if current_room_info["Items"]:
        print("Items to take:")
        for item in current_room_info["Items"]:
            print(f"- Take {item}")
    
    # Display available items to use from the inventory
    if player_inventory:
        print("Items to use:")
        for item in player_inventory:
            if item in usable_items:
                print(f"- Use {item}")
    
    print("Other actions:")
    print("- Type 'inv' to check your inventory")
    print("- Type 'map' to see the game map")
    print("- Type 'quit' to quit the game")


def display_room_info(current_room, game_map):
    room_info = game_map[current_room]
    print("\nCurrent Room: " + current_room)
    print("Description:" + room_info["Description"])
    print("Exits:", ", ".join(room_info["Exits"]))
    print("Items in the room:", ", ".join(room_info["Items"]))
    print("Objects in the room:", ", ".join(room_info["Objects"]))

def Take(game_state, game_map):
    current_room_info = game_map[game_state.current_room]
    item_name = input("Which item would you like to pick up? ").strip().lower()
    if item_name in current_room_info["Items"]:
        # Remove the item from the room and add it to the player's inventory
        current_room_info["Items"].remove(item_name)
        game_state.player_inventory.append(item_name)
        print(f"You took the {item_name}.")
    else:
        print("There is no such item in the room.")
        
    return game_state
def move(game_state, game_map, directions):
    current_room_state = game_state.current_room
    current_room_info = game_map[current_room_state]
    # Get player's input for movement command
    move_command_input = input("Which direction would you like to move?: ").strip().lower()
    # Check if the move command is valid
    if move_command_input in directions:
        direction = directions[move_command_input]
        if direction in current_room_info["Exits"]:
            new_room = current_room_info["Exits"][direction]
            print(f"You moved to the {new_room}.")
            game_state.current_room = new_room  # Update the current room
        else:
            print("You can't move in that direction.")
    else:
        print("Invalid move command.")
    return game_state
def use(game_state, usable_items):
    item_name = input("What would you like to use?: ")
    if item_name in game_state.player_inventory and item_name in  usable_items:
        print(f"You used the {item_name}")
        #Put the different print actions here
        game_state.player_inventory.remove(item_name)
    elif item_name not in game_state.player_inventory:
        print("That item is not in your inventory.")
    elif item_name not in usable_items:
        print("You can't use that item.")
    else:
        print("That item doesn't exist.")
def quit(game_state):
    while True:        
        quit_game = input("Are you sure you want to quit the game? [y/n] \n\n>> ").strip().lower()
        if quit_game == "y":
            save = input("\nWould you like to save you're game before you go? [y/n] \n\n>>").strip().lower()
            if save == "y":
                save_game(game_state)
                return True
            elif save == "n":
                print("Ok we wont save you're game")
                save_game(game_state)
                return True
            else:
                print(f"{quit_game} is not a viable answer. Please enter 'y' or 'n'.")   
        elif quit_game == "n":
            return False
        else:
            print(f"{quit_game} is not a viable answer. Please enter 'y' or 'n'.")      
def eat(game_state, edible_items):
    item_name = input("What would you lke to eat?")
    if item_name in game_state.player_inventory and item_name in edible_items:
        print(f"You ate {item_name}, Yum yum yum!")
        #Add any effects that the player might experience.
        game_state.player_inventory.remove(item_name)
    elif item_name not in game_state.player_inventory:
        print("That item is not in your inventory")
    elif item_name not in edible_items:
        print("You cant eat this item. Stupid.")
    else:
        print("That item doesn't exist.")
def inv_check(game_state):
    if not game_state.player_inventory:
        print("Your inventory is empty...")
    else:
        print("Your inventory: ")
        for item in game_state.player_inventory:
            print(f"- {item}")
def help(game_state):
    category = input("\nWhat do you need help with? \nCommands, Story, Current Moves \n\n>>").strip().lower()
    
    if category == "commands":
        print(
            "Here is the list of commands: ",
            "\n\n'move'      move is used to navigate the playing area",
            "\n            and is the first thing you type when trying to move around",
            "\n\n'n,e,s,w'   these are the directions that the player [you] can move in",
            "\n            only type one of them when asked which way you want to go",
            "\n\n'take'      take is what lets you pick things up and  put them into your",
            "\n            inventory. but it only works if there is anything to pick up",
            "\n\n'use'       the use command is extremely situational, so far i haven't added",
            "\n            anything that needs this command, but ill get there, give me some time",
            "\n\n'inv'       this command is to check your inventory. which you should have",
            "\n            figured out by now, but if not, there ya go champ! type inv to use it",
            "\n\n'map'       map allows you to see not only what room you are in, but also",
            "\n            to see the entire playable area, along with their connections",
            "\n\n'quit'      this should be pretty self explanatory, but if you somehow",
            "\n            don't know what quit does, it just exits the game for you",
            "\n\n\n          That's all the commands I have implemented for now,",
            "\n            But more are on the way dont worry about it! Have fun!",
        )
    elif category == "current moves":
        show_available_moves(game_state.current_room, game_map, game_state.player_inventory)
    elif category == "Story":
        print("Figure it out :) bc im still trying to work on it")
def map_check(game_state):
    current_room = game_state.current_room
    print(f"Your current room is {current_room}")
  #←→↑↓«»
    # Define the map layout with room connections
    map_layout = [
        "                                                         Compass:     ↑N↑",
        "                     Gallery                                      « W [♦] E »",
        "                        |                                             ↓S↓",
        "Ballroom ----------- Chapel --------- Tunnel",
        "                        |           ",
        "                        |              Repository -- Pantry -- Lab",
        "                        |                 |",
        "Dungeon ------------ Stairs ---------- Kitchen",
        "   |                    |",
        "Torture -- Armory       |",
        "                        |",
        "                      Room",
        "",
        ""
    ]
    # Print the map with the current room highlighted in green
    print((Color.BOLD + Color.BLUE + "Game Map [Green text is the room you are in]:" + Color.END))
    for room_line in map_layout:
        line = ""
        for room_name in room_line.split(" "):
            if room_name == current_room:
                line += Color.GREEN + room_name + Color.END + " "
            else:
                line += room_name + " "
        print(line)