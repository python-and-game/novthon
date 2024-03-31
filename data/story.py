# The script where the scenes defined, each scenes contained a part (command)
# each scene is identified by a key and each part is tuple or list, with a type 
# and a bunch of values.
#     E.g: [ 'type', 'value1', 'value2', ...]
#     type: The type of the part which is used to determine actions.
#     value1, value2, ...: A list of values to use for the determined actions. 

scenes = {
    # Initalizing the game, load day background then start the game
    # by playing the main menu.
    "init": [
        ["loader", "bg day", "day_bg.png"],
        ["play", "main_menu"],
    ],
    # A centered menu, with 2 options: 
    # - Start Game (play begin scene)
    # - Quit Game (exit the game)
    "main_menu": [
        ["cmenu", {
            "Start Game": ["play", "begin"],
            "Quit Game": "exit_game"
        }]
    ],
    # Meet Nov, but beware of your actions, or else, moon awaits you.
    "begin": [
        ["add", "bg day"],
        ["dialogue", "Hello! Nice to meet you, I'm Nov!"],
        ["menu", { "dialogue": "Nov: Do you want to go somewhere?",
                   "No, I don't want to.": ["play", "bad_ending"],
                   "How about watching a movie?": ["play", "good_ending"]
                 }
        ]
    ],
    # If you don't want to go any where, then ready to live at the moon.
    "bad_ending": [
        ["dialogue", "Nov: What? Then go to the moon!"],
        ["dialogue", "*You got kicked and landed on the moon*"],
        ["cdialogue", "THE END."],
        ["play", "main_menu"]
    ],
    # If you go to the cinema with Nov, then ready for another time.
    "good_ending": [
        ["delete", "bg day"],
        ["dialogue", f"What a wonderful day, I wish we can continue it."],
        ["dialogue", "Nov: Yeah!"],
        ["cdialogue", "THE END."],
        ["play", "main_menu"]
    ]
}