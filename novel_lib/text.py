import pygame
from .config import *
from .image import screen

class Text:
    
    def __init__(self, text, color='white'):
        pygame.init()
        try:
            self.font = pygame.font.Font(font_file, font_size)
        except:
            self.font = pygame.font.SysFont(font_file, font_size)

        self.lines = []
        self.color = color

        # Split the text into lines based on the '\n' character
        lines = text.split('\n')

        for line in lines:
            current_line = ""
            words = line.split()
            for i, word in enumerate(words):
                if i == 0:
                    if self.font.size(current_line + word)[0] <= window_width:
                        current_line += word
                    else:
                        self.lines.append(current_line)
                        current_line = word
                else:
                    if self.font.size(current_line + " " + word)[0] <= window_width:
                        current_line += " " + word
                    else:
                        self.lines.append(current_line)
                        current_line = word
                    
            self.lines.append(current_line)

    def draw(self):
        x, y = (0, 0)
        for line in self.lines:
            rendered = self.font.render(line, True, self.color)
            shadow = self.font.render(line, True, 'black')
            rect = rendered.get_rect()
            shadow_rect = shadow.get_rect()
            rect.topleft = (x, y)
            shadow_rect.topleft = (x+shadow_offset, y+shadow_offset)
            screen.blit(shadow, shadow_rect)
            screen.blit(rendered, rect)
            y += rect.height

class CenteredText:
    
    def __init__(self, text, color='white'):
        pygame.init()
        try:
            self.font = pygame.font.Font(font_file, font_size)
        except:
            self.font = pygame.font.SysFont(font_file, font_size)

        self.lines = []
        self.color = color

        # Split the text into lines based on the '\n' character
        lines = text.split('\n')

        for line in lines:
            current_line = ""
            words = line.split()
            for i, word in enumerate(words):
                if i == 0:
                    if self.font.size(current_line + word)[0] <= window_width:
                        current_line += word
                    else:
                        self.lines.append(current_line)
                        current_line = word
                else:
                    if self.font.size(current_line + " " + word)[0] <= window_width:
                        current_line += " " + word
                    else:
                        self.lines.append(current_line)
                        current_line = word
                    
            self.lines.append(current_line)

    def draw(self):
        x, y = screen.get_rect().center
        for line in self.lines:
            rendered = self.font.render(line, True, self.color)
            shadow = self.font.render(line, True, 'black')
            rect = rendered.get_rect()
            shadow_rect = shadow.get_rect()
            rect.center = (x, y)
            shadow_rect.center = (x+shadow_offset, y+shadow_offset)
            screen.blit(shadow, shadow_rect)
            screen.blit(rendered, rect)
            y += rect.height