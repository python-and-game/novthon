import pygame.mixer
from .config import *
pygame.mixer.init()

def call(music_file, loops=-1):
    # Call a music file.
    pygame.mixer.music.load(music_dir + '/' + music_file)
    pygame.mixer.music.play(loops)

def stop():
    pygame.mixer.music.stop()
