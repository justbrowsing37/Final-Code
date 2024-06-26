import os
import time
from classes import GameState, StopWatch, keyboardDisable, Color
from ui import print_instructions, load_game, save_game, separation
from gameplay import display_room_info, Take, move, quit, inv_check, help, map_check, show_available_moves
from game_map import game_map, directions


os.system('cls')
main_loop = True
disable = keyboardDisable()

stopwatch = StopWatch()
stopwatch.start()
while main_loop:
    game = input("Would you like to restore a previous game [y/n]: ").strip().lower()
    match game:
        case "y":
            os.system('cls')
            game_state = load_game()
            if game_state is None:
                print("\nNo previous game found...\nStarting a new game...")
                disable.start()
                time.sleep(3)
                game_state = GameState()
                os.system('cls')
                print_instructions()
                disable.stop()
        case "n":
            game_state = GameState()
            os.system('cls')
            print_instructions()
        case _:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
    while game_state.current_room:
        display_room_info(game_state.current_room, game_map)
        command = input("\nWhat would you like to do?: ").strip().lower()
        match command:   
            case "save":
                save_game(game_state)
                print("Game saved.")
                continue
            case "inv":
                inv_check(game_state)
                continue
            case "help":
                help(game_state)
                continue
            case "moves":
                show_available_moves(game_state.current_room, game_map, game_state.player_inventory)
            case "quit":
                if quit(game_state):
                    os.system('cls')
                    print("Quitting the game... \n\n\nGoodbye! \n\n")
                    main_loop = False
                    break  # Exit the game loop
                else:
                    print("Resuming the game...")
                    continue  # Continue the game loop
                continue
            case "take":
                Take(game_state, game_map)
                separation()
            case "move":
                game_state = move(game_state, game_map,  directions)
                separation()
            case "map":
                map_check(game_state)
            case _:
                print(f"You don't know how to '{command}'")
                separation()
                continue
           