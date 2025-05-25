# This file defines some special scenes that will be used as screens, such as the main menu.
# It's a short example that only includes the main menu. The value True after the options
# dictionary is to tell the game to resize the box to the size of the text.
specials = {
    "main_menu": [
        ["delete", "all"],
        ["cmenu", {
            "Start Game": ["play", "begin"],
            "Quit Game": "exit_game"
        }, True]
    ]
}
