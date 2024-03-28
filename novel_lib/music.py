import pygame.mixer
from .config import *
pygame.mixer.init()

def call(music_file, loops=-1):
    # Call a music file.
    pygame.mixer.music.load(music_dir + '/' + music_file)
    pygame.mixer.music.play(loops)

def sound(file, loops=0):
    # Call a sound file.
    sound = pygame.mixer.Sound(music_dir + '/' + file)
    sound.play(loops)

def stop():
    pygame.mixer.stop()
