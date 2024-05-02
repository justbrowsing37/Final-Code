game_map = {
    "Chapel": {
        "Description": " I am standing in a majestic chapel."
                       "\n             There is a coffin in front of me.",
        "Exits": {"north": "Gallery", "east": "Tunnel", "west": "Ballroom", "south": "Stairs"},
        "Items": ["ring"],
        "Objects": ["coffin"]
    },
    "Gallery": {
        "Description": " There is a big window at the top of the stairs."
                       "\n             The view from here is amazing...",
        "Exits": {"south": "Chapel"},
        "Items": [],
        "Objects": ["window"]
    },
    "Ballroom": {
        "Description": " I am standing in the grand ballroom..."
                       "\n             Sure will you had a girl to dance with don't you?",
        "Exits": {"east": "Chapel"},
        "Items": [],
        "Objects": []
    },
    "Tunnel": {
        "Description": " I am in a tunnel with limestone walls."
                       "\n             There is a large stone door with a Sapphire in the middle.",
        "Exits": {"west": "Chapel"},
        "Items": ["bloody knife"],
        "Objects": []
    },
    "Stairs": {
        "Description": " I am in a dingy looking stairwell."
                       "\n             Broken glass is everywhere, looks like an explosion happened?",
        "Exits": {"north": "Chapel", "east": "Kitchen", "south": "Room", "west": "Dungeon"},
        "Items": ["broken glass"],
        "Objects": []
    },
    "Room": {
        "Description": "\nYou are in a plain, nondescript room.",
        "Exits": {"north": "Stairs"},
        "Items": [],
        "Objects": []
    },
    "Kitchen": {
        "Description": "\nThis looks like their version of a kitchen."
                       "\nLost of pots, pans, and kettles are in the sink...",
        "Exits": {"north": "Repository", "west": "Stairs"},
        "Items": [],
        "Objects": []
    },
    "Repository": {
        "Description": "\nIm standing in the room filled with animal heads."
                       "\nIt looks like these guys loved to hunt...",
        "Exits": {"east": "Pantry", "south": "Kitchen"},
        "Items": [],
        "Objects": []
    },
    "Pantry": {
        "Description": "\nFound the pantry, Might as well take a bite!"
                       "\nI wonder why they need a pantry in a chapel?",
        "Exits": {"west": "Head Room", "east": "Lab"},
        "Items": ["Meat", "Bread"],
        "Objects": ["Basket"]
    },
    "Lab": {
        "Description": "\nA Lab? What kind of a chapel is this?"
                       "\nAnyways, I wonder what they might be doing in here?",
        "Exits": {"west": "Pantry"},
        "Items": [],
        "Objects": ["chemicals"]
    },
    "Dungeon": {
        "Description": "\nThe dungeon seems to be a bit dusty,"
                       "\nThere are skeletons on the ground...",
        "Exits": {"east": "Stairs", "south": "Torture"},
        "Items": ["metal chain", "key"],
        "Objects": ["gate"]
    },
    "Torture": {
        "Description": "\nOne of the worst rooms in the whole castle",
        "Exits": {"north": "Dungeon", "east": "Armory"},
        "Items": ["bones", "Sword"],
        "Objects": ["Skeleton", "Bones"]
    },
    "Armory": {
        "Description": "\nLooks like you found the weapons hub of this whole place,"
                       "\nReally Staring to look more like a castle rather than a chapel",
        "Exits": {"west": "Torture Chamber"},
        "Items": ["Handcuffs"],
        "Objects": []
    }
}
'''
View of the game map:
                 Gallery
		  	        |
Ballroom -------- Chapel ----- Tunnel
                    |
		  	        |              Repository -- Pantry -- Lab
		            |                 |
Dungeon --------- Stairs --------- Kitchen
   |                |
Torture --- Armory  |
                    |
                   Room
'''

moves = ["n", "e", "s", "w", "take", "slide", "move", "turn", "climb", "push", "circle", "inv", "map", "quit"]

items = ["Handcuffs", "ring", "bones", "Sword", "metal chain", "key", "Meat", "Bread", "broken glass", "bloody knife"]

usable_items = ["ring"]

edible_items = []

objects = ["coffin", "window", "Basket", "chemicals", "gate", "Skeleton", "Bones"]

directions = {
    'n': 'north',
    'e': 'east',
    's': 'south',
    'w': 'west',
}