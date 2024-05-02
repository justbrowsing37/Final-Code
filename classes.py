import time
import os
import msvcrt
from game_map import objects

class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARK_CYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    ITALICS = '\033[3m'

class GameState:
    def __init__(self, current_room=None, player_inventory=None):
        self.current_room = current_room if current_room else "Chapel"  # Start in the Chapel by default
        self.player_inventory = player_inventory if player_inventory else []
    def to_dict(self):
        return {
            "current_room": self.current_room,
            "player_inventory": self.player_inventory
        }
    
    @classmethod
    def from_dict(cls, state_dict):
        return cls(state_dict["current_room"], state_dict["player_inventory"])

class StopWatch:
    def __init__(self):
        self.startTime = None
        self.elapsedTime = 0
        self.isRunning = False
    def start(self):
        if not self.isRunning:
            self.startTime = time.time()
            self.isRunning = True
    def stop(self):
        if self.isRunning:
            self.elapsedTime = time.time() - self.startTime
            self.isRunning = False
    def reset(self):
        self.elapsedTime = 0
        self.isRunning = False
    def getElapsedTime(self):
        totalTime = self.elapsedTime
        if self.isRunning:
            totalTime += time.time() - self.startTime
        print(f"Time survived: {totalTime:.2f} seconds")

class Objects():
    def opened():
        pass
    
    def closed():
        pass

    def moved():
        pass
    
    def unmoved():
        pass

import time
class keyboardDisable():

    def start(self):
        self.on = True

    def stop(self):
        self.on = False

    def __call__(self): 
        while self.on:
            msvcrt.getwch()


    def __init__(self):
        self.on = False
        import msvcrt