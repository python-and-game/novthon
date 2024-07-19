import pygame
from .config import *
pygame.init()

images = {}
images_to_render = {}

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(window_title)

class Image:

    def __init__(self, image):
        try:
            self.image = pygame.image.load(image_dir + '/' + image)
        except:
            self.image = pygame.Surface(screen.get_size())
            self.image.fill(image)

        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center

    def draw(self):
        screen.blit(self.image, self.rect) 

def loader(name, image):
    image = Image(image)
    images[name] = image

def add_to_render(name):
    if name in images:
        images_to_render[name] = images[name]
    
def draw():
    for image in images_to_render.values():
        image.draw()

def delete(name):
    global images_to_render
    if name in images_to_render: 
        del images_to_render[name]
    else:
        if name == 'all':
            images_to_render = {}
    draw()

    
