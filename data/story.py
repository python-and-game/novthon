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
        ["loader", "black", (0, 0, 0)],
        ["loader", "bg day", "day_bg.png"],
        ["loader", "bg night", "night_bg.png"],
        ["play", "main_menu"],
    ],
    # Meet Nov, but beware of your actions, or else, moon awaits you.
    "begin": [
        ["fade", "black", "bg day"],
        ["dialogue", "Hello! Nice to meet you, I'm Nov!"],
        ["dialogue", "Nov: I usually come here to relax."],
        ["dialogue", "Nov and I are having a great time together, but Nov asked me something..."],
        ["menu", { "dialogue": "Nov: Why don't we go somewhere?",
                   "No, thanks.": ["play", "bad_ending"],
                   "That's a good idea.": ["play", "normal_ending"],
                   "How about watching a movie?": ["play", "good_ending"]
                 }
        ]
    ],
    # If you don't want to go any where, then ready to live at the moon.
    "bad_ending": [
        ["dialogue", "Nov: What? Then go to the moon!"],
        ["dialogue", "Nov is confused and shocked because I and Nov just talked happily and now I just say something that broke Nov's feelings."],
        ["dialogue", "Nov is angry and suprised."],
        ["sound", "kick_sound.mp3"], # I didn't expect that, sorry.
        ["dialogue", "*You got kicked and landed on the moon*"],
        ["stop"],
        ["cdialogue", "THE END."],
        ["play", "main_menu"]
    ],
    # You and Nov decide to meet again this night.
    "normal_ending": [
        ["dialogue", "Nov and I decided to meet today's night."],
        ["fade", "bg day", "bg night"],
        ["dialogue", "Nov: Today is so fun, I think we should go out more often."],
        ["dialogue", "Yeah."],
        ["cdialogue", "THE END."],
        ["play", "main_menu"]
    ],
    # If you go to the cinema with Nov, then ready for another time.
    "good_ending": [
        ["fade", "bg day", "black"],
        ["dialogue", f"What a wonderful day, I wish we can continue it."],
        ["dialogue", "Nov: Yeah!"],
        ["cdialogue", "THE END."],
        ["play", "main_menu"]
    ]
}

if 'specials' in globals():
    for scene, parts in specials.items():
        scenes[scene] = parts
