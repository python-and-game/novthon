#!/usr/bin/env python3
# This is where all of the game-related files will be loaded to start the default game of NovThon program.

# First, import all files from the novel_lib module which will compile the game's script
# (also import the json module to load the story script)
from novel_lib import *
import os.path

# Load the script(s), a bunch of datas which are moved to the `data_dir` directory to make this file look cleaner.
try:
    exec(open(data_dir + '/special_scene.py').read(), globals())
except:
    pass

exec(open(data_dir + '/story.py').read(), globals())

# Now let's start the game.
running = True
while running:
    try:
        result = run_parts(scenes, 'init')  # Init scene allows users to load stuff before playing the game.
    except:
        try:
            result = run_parts(scenes, 'main_menu')

        except:
            result = run_parts(scenes, 'begin')

    running = False