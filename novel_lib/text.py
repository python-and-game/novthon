import pygame
from .config import *
from .image import screen

class TextBox:

    def __init__(self, width, height, x, y, color=None, centered=False):
        self.width = width
        self.height = height
        self.position = (x, y)
        self.color = color or box_color
        self.centered = centered
     
    def draw(self):
        color = pygame.Color(self.color)
        color.a = box_alpha

        box = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(box, color, box.get_rect(), border_radius=box_border)
        pygame.draw.rect(box, 'white', box.get_rect(), width=box_outline_size, border_radius=box_border)

        if self.centered:
            box_rect = box.get_rect()
            box_rect.center = self.position
        else:
            box_rect = box.get_rect()
            box_rect.topleft = self.position

        screen.blit(box, box_rect)        

class Text:
    
    def __init__(self, text, box=None, color='white'):
        pygame.init()
        try:
            self.font = pygame.font.Font(font_file, font_size)
        except:
            self.font = pygame.font.SysFont(font_file, font_size)

        self.lines = []
        self.color = color
        self.box_color = box

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
        box_width = window_width
        box_height = sum(self.font.size(line)[1] for line in self.lines)
        box_y = y

        text_img = pygame.Surface((window_width, window_height), pygame.SRCALPHA)

        for line in self.lines:

            if not line: 
                box_height -= self.font.size(line)[1]
                box_y += self.font.size(line)[1]

            rendered = self.font.render(line, True, self.color)
            shadow = self.font.render(line, True, 'black')
            rect = rendered.get_rect()
            shadow_rect = shadow.get_rect()
            rect.topleft = (x, y)
            shadow_rect.topleft = (x+shadow_offset, y+shadow_offset)
            text_img.blit(shadow, shadow_rect)
            text_img.blit(rendered, rect)
            y += rect.height

        TextBox(box_width, box_height, x, box_y, self.box_color).draw()
        screen.blit(text_img, (0, 0))
       

class CenteredText:
    
    def __init__(self, text, box=None, color='white'):
        pygame.init()
        try:
            self.font = pygame.font.Font(font_file, font_size)
        except:
            self.font = pygame.font.SysFont(font_file, font_size)

        self.lines = []
        self.color = color
        self.box_color = box

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
        box_width = window_width
        box_height = sum(self.font.size(line)[1] for line in self.lines)
        box_y = y

        text_img = pygame.Surface((window_width, window_height), pygame.SRCALPHA)

        for line in self.lines:

            if not line: 
                box_height -= self.font.size(line)[1]
                box_y += self.font.size(line)[1]

            rendered = self.font.render(line, True, self.color)
            shadow = self.font.render(line, True, 'black')
            rect = rendered.get_rect()
            shadow_rect = shadow.get_rect()
            rect.center = (x, y)
            shadow_rect.center = (x+shadow_offset, y+shadow_offset)
            text_img.blit(shadow, shadow_rect)
            text_img.blit(rendered, rect)
            y += rect.height

        TextBox(box_width, box_height, x, box_y, self.box_color, True).draw()
        screen.blit(text_img, (0, 0))
       