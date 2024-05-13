import json
from classes import Color, GameState
                                                        
def print_instructions():
    print((Color.BOLD + "Welcome to VOODOO CASTLE!" + Color.END).center(108))
    print("\n                  Welcome player to my wonderful creation! Just know that this is\n                  a test module and things in here are all subject to change. But\n                  don't worry too much. Since I am a very crazy person and I am \n                  always looking for new ways to improve my game! So if you have \n                  any ideas for the game, Be sure to let me know! Anyways, some \n                  commands are |'move', 'take', and 'use'| Have fun! - Bhanu S. :)")
    print("               ---------------------------------------------------------------------")
    print("\n")
def separation():
    linebreaks = (
            Color.BOLD + '______________________________________________________________________________________________' + Color.END)
    linebreaks_ = (
            Color.UNDERLINE + '\n║                                                                                            ║' + Color.END)
    print(linebreaks, linebreaks_)

def save_game(game_state):
    with open("game_state.json", "w") as file:
        json.dump(game_state.to_dict(), file)

def load_game():
    try:
        with open("game_state.json", "r") as file:
            ("Loading previous game...")
            return GameState.from_dict(json.load(file))
    except FileNotFoundError:
        return None