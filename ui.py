import sys
import random
import time
import os
from classes import Color



signatures = [
    "- Professional Moron",
    "- Car Enthusiast",
    "- The one and only Indian and Team",
    "- Your neighborhood idiot",
    "- Diphosphourus Trijasonide",
    "- Hyaa'sa ibn Jy'ud al-Qalai",
    "- Chu Che-Huo",
    "- Aluminum Nitrate",
    "- Afar ibn Baani al-Riyal and Team",
    "- Sulfur Hydrochloride",
    "- Nate Horne",
    "- Boris Skolensky",
    "- Gilberto Raymond and Team",
    "- Max Verstappen"
]

random_sign = random.choice(signatures)
def GameIntro():
    show_bar()
    os.system('cls')
    print_instructions()
def progress_bar(iteration, total, bar_length=60):
    percent = "{0:.3f}".format(100 * (iteration / float(total)))
    filled_length = int(bar_length * iteration // total)
    bar = (Color.GREEN + '█' + Color.END) * filled_length + (Color.RED + '█' + Color.END) * (
            bar_length - filled_length)
    sys.stdout.write('\r║%s║ %s%% ' % (bar, percent))
    sys.stdout.flush()
    if iteration < total / 2:
        time.sleep(0.1)
    elif iteration < total * 0.9:
        time.sleep(0.2)
    else:
        time.sleep(0.5)
def clear_bar():
    print('\n')
    print("\033[F\033[K", end="")
    print("\033[F\033[K", end="")
    print("\033[F\033[K", end="")
    print("\033[F\033[K", end="")
def show_bar():
    Message()
    time.sleep(2)
    print("\nInitializing....")
    time.sleep(0.5)
    total_iterations = 50
    for i in range(total_iterations + 1):
        progress_bar(i, total_iterations)
    time.sleep(1.5)
    clear_bar()
    print("\nExtracting text...")
    time.sleep(0.5)
    total_iterations = 75
    for i in range(total_iterations + 1):
        progress_bar(i, total_iterations)
    time.sleep(0.5)
    clear_bar()
    print("\nPreparing output...")
    time.sleep(0.5)
    total_iterations = 137
    for i in range(total_iterations + 1):
        progress_bar(i, total_iterations)
    time.sleep(0.5)
    print("\n\nReady to play")
    print("\nPress Enter")
    input("")
    os.system('cls')
    print((Color.BOLD + Color.UNDERLINE + "Please wait..." + Color.END))
    time.sleep(5)
    os.system('cls')
def Message():
    print("\nThe following game is " + (
            Color.BOLD + Color.ITALICS +  '  E E E E    E E E E E E E E E' + Color.END) + "\n        (im working on it... dont judge me)")
    print(f"\n\nThis project took me months to make... I hope you enjoy!\n     {random_sign}")
    print("\n\n" + "↓↓" + (
            Color.BOLD + Color.UNDERLINE + 'PLEASE WAIT FOR INSTRUCTIONS BELOW... DO NOT TYPE' + Color.END) + "↓↓")
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