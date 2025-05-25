from pygame.locals import *

# Window settings
window_width = 800
window_height = 600
window_title = 'Game Window'

# Game settings.
fps = 60
keys = {
    K_RETURN: 'ok',
    K_SPACE: 'ok',
    K_UP: 'move_up',
    K_w: 'move_up',
    K_DOWN: 'move_down',
    K_s: 'move_down',
    K_ESCAPE: 'exit_game',
    K_s: 'save_game',
    K_l: 'load_game'
}

# File location settings
data_dir = 'data'
image_dir = data_dir + '/images'
music_dir = data_dir + '/music'

# Text settings
font_file = None # Default font
font_size = 25
shadow_offset = 2
text_speed = 0.5

# Textbox settings
box_alpha = 150
box_color = 'blue'
box_outline_size = 2
box_border = 6
box_select_color = 'darkblue'

# Fade settings
in_duration = 0.5
hold_duration = 0
out_duration = 0.5

# Load the customized config file from the game
try:
    f = open(data_dir + '/game_config.py')
    exec(f.read(), globals())
    f.close()
except:
    pass

    
