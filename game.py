#!/usr/bin/env python3
# This is where all of the game-related files will be loaded to start the default game of NovThon program.

# First, import all files from the novel_lib module which will compile the game's script
# (also import the json module to load the story script)
import os
import sys

if len(sys.argv) > 1:
    os.chdir(sys.argv[1])

from novel_lib import *

# Load the script(s), a bunch of datas which are moved to the `data_dir` directory to make this file look cleaner.
if os.path.exists(os.path.join(data_dir, 'special_scene.py')):
    f = open(os.path.join(data_dir, 'special_scene.py'), encoding='utf-8')
    exec(f.read(), globals())
    f.close()

story = open(os.path.join(data_dir, 'story.py'), encoding='utf-8')
exec(story.read(), globals())
story.close()

# Now let's start the game.
running = True
while running:
    try:
        result = run_parts(scenes, 'init')  # Init scene allows users to load stuff before playing the game.
    except:
        try:
            result = run_parts(scenes, 'main_menu')

        except:
            result = run_parts(scenes, 'soda_intro')

    running = False