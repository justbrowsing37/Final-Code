import os
import time
from classes import GameState, StopWatch
from ui import GameIntro, print_instructions, load_game, save_game, separation
from gameplay import display_room_info, Take, move, quit, inv_check, help, hint_timer, map_check
from game_map import game_map, moves, directions


def main():
    GameIntro()

    os.system('cls')
    main_loop = True

    stopwatch = StopWatch()
    stopwatch.start()
    while main_loop:
        #this is all pregame stuff
        game = input("Would you like to restore a previous game [y/n]:\n\n>> ").strip().lower()
        if game == "y":
            game_state = load_game()
            if game_state is None:
                print("No previous game found...\nStarting a new game...")
                time.sleep(3)
                game_state = GameState()
                os.system('cls')
                print_instructions()
        elif game == "n":
            game_state = GameState()
            os.system('cls')
            print_instructions()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        while game_state.current_room:
            display_room_info(game_state.current_room, game_map)
            command = input("\nWhat would you like to do?: ").strip().lower()
            if command == "save":
                save_game(game_state)
                print("Game saved.")
                continue
            if command == "inv":
                inv_check(game_state)
                continue
            elif command == "help":
                help()
                continue
            elif command == "quit":
                if quit():
                    os.system('cls')
                    print("Quitting the game... \n\n\nGoodbye! \n\n")
                    main_loop = False
                    break  # Exit the game loop
                else:
                    print("Resuming the game...")
                    continue  # Continue the game loop

            if command not in moves:
                print(f"You don't know how to '{command}'")
                separation()
                continue
            elif command == "take":
                Take(game_state, game_map)
                separation()
            elif command == "move":
                game_state = move(game_state, game_map,  directions)
                separation()
            elif command == "map":
                map_check(game_state)

            stopwatch.reset()
            stopwatch.start()
main()