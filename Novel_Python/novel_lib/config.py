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
    K_ESCAPE: 'exit_game',
    K_s: 'move_down',
    K_DOWN: 'move_down',
    K_w: 'move_up',
    K_UP: 'move_up'
}

# File location settings
data_dir = 'data'
image_dir = data_dir + '/images'
music_dir = data_dir + '/music'

# Text settings
font_file = None # Default font
font_size = 30
shadow_offset = 2
text_speed = 0.5
text_unselected_color = 'gray'
text_color = 'white'
text_selected_color = text_color

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

try:
    f = open(data_dir + '/game_config.py', encoding='utf-8')
    exec(f.read(), globals())
    f.close()
except:
    pass