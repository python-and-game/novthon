# This file defines some special scenes that will be used as screens, such as the main menu.
# It's a short example that only includes the main menu. The value True after the options
# dictionary is to tell the game to resize the box to the size of the text.
specials = {
    "init": [
        ["loader", "black", (0, 0, 0)],
        ["loader", "bg ruins", (255, 0, 0)],
        ["loader", "bg void", (0, 255, 0)],
        ["loader", "bg future", (0, 0, 255)],
        ["loader", "bg machine", (255, 255, 255)],
        ["play", "main_menu"]
    ],
    "main_menu": [
        ["delete", "all"],
        ["cmenu", {
            "Start Game": ["play", "begin"],
            "Quit Game": "exit_game"
        }, True]
    ]
}
