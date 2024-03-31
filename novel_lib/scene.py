# Import pygame
import pygame
from pygame.locals import *

# Init pygame
pygame.init()

# Import some important elements of most games.
from .config import *
from .image import *
from .text import *
from .music import *

clock = pygame.time.Clock()

def dialogue(text):
    i = 0

    while True:
        clock.tick(fps)
        if text_speed > 0:
            i += text_speed
        else:
            i = len(text)

        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYDOWN and keys.get(e.key) == 'exit_game'):
                return 'exit_game'                

            if e.type == KEYDOWN and keys.get(e.key) == 'ok':
                if len(text[:int(i)]) == len(text):
                    return
                else:
                    i = len(text)

        screen.fill((0, 0, 0))
        draw()

        Text(text[:int(i)]).draw()

        pygame.display.update()

def menu(items):
    if 'dialogue' in items:
        dialogue_text = items['dialogue']

    options_break = '\n'
    current_option = 1

    i = 0

    while True:
        clock.tick(fps)


        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYDOWN and keys.get(e.key) == 'exit_game'):
                return 'exit_game'                        

            if e.type == KEYDOWN:
                if keys.get(e.key) == 'move_up':
                    current_option = (current_option - 1) % len(items)
                elif keys.get(e.key) == 'move_down':
                    current_option = (current_option + 1) % len(items)
                elif keys.get(e.key) == 'ok':
                    item_name, item_value = list(items.items())[current_option]
                    if callable(item_value):
                        return item_value()
                    else:
                        return item_value

        screen.fill((0, 0, 0))
        draw()

        for i, (item_name, item_value) in enumerate(items.items()):
            if item_name != 'dialogue':
                if i == current_option:
                    option = Text(options_break * (i + 1) + item_name)
                else:
                    option = Text(options_break * (i + 1) + item_name, 'gray')

                option.draw()

        try:
            Text(dialogue_text).draw()
        except:
            pass

        pygame.display.update()


def cdialogue(text):
    i = 0

    while True:
        clock.tick(fps)
        if text_speed > 0:
            i += text_speed
        else:
            i = len(text)

        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYDOWN and keys.get(e.key) == 'exit_game'):
                return 'exit_game'                

            if e.type == KEYDOWN and keys.get(e.key) == 'ok':
                if len(text[:int(i)]) == len(text):
                    return
                else:
                    i = len(text)

        screen.fill((0, 0, 0))
        draw()

        CenteredText(text[:int(i)]).draw()

        pygame.display.update()

def cmenu(items):
    if 'dialogue' in items:
        dialogue_text = items['dialogue']
        current_option = 1
    else:
        dialogue_text = None
        current_option = 0

    options_break = '\n'

    while True:
        clock.tick(fps)

        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYDOWN and keys.get(e.key) == 'exit_game'):
                return 'exit_game'                        

            if e.type == KEYDOWN:
                if keys.get(e.key) == 'move_up':
                    current_option = (current_option - 1) % len(items)
                elif keys.get(e.key) == 'move_down':
                    current_option = (current_option + 1) % len(items)
                elif keys.get(e.key) == 'ok':
                    item_name, item_value = list(items.items())[current_option]
                    if callable(item_value):
                        return item_value()
                    else:
                        return item_value

        screen.fill((0, 0, 0))
        draw()

        for i, (item_name, item_value) in enumerate(items.items()):
            if item_name != 'dialogue':
                if i == current_option:
                    if dialogue_text: option = CenteredText(options_break * (i + 1) + item_name)
                    else: option = CenteredText(options_break * i + item_name)
                else:
                    if dialogue_text: option = CenteredText(options_break * (i + 1) + item_name, 'gray')
                    else: option = CenteredText(options_break * i + item_name, 'gray')

            option.draw()

        try:
            CenteredText(dialogue_text).draw()
        except:
            pass

        pygame.display.update()

def run_parts(scenes, scene):
    # An executor for a scene.

    for part in scenes[scene]:
        part_type = part[0]  # Get the part type
        part_value = part[1:]  # Store the values in a list.

        if part_type == 'loader':
            loader(*part_value)

        elif part_type == 'add':
            add_to_render(part_value[0])

        elif part_type == 'delete':
            delete(part_value[0])

        elif part_type == 'dialogue':
            result = dialogue(*part_value)
            if result == 'exit_game':
                return

        elif part_type == 'menu':
            result = menu(*part_value)

            if result == 'exit_game':
                return

            else:
                if isinstance(result, list) or isinstance(result, tuple):
                    # This works like part, but it's called 'commands', only
                    # a few parts can also be commands.
                    cmd_type = result[0]
                    cmd_value = result[1]
                    if cmd_type == 'play': 
                        scene = cmd_value
                        run_parts(scenes, scene)   

        elif part_type == 'cdialogue':
            result = cdialogue(*part_value)
            if result == 'exit_game':
                return

        elif part_type == 'cmenu':
            result = cmenu(*part_value)
            if result == 'exit_game':
                return

            else:
                if isinstance(result, list) or isinstance(result, tuple):
                    # This works like part, but it's called 'commands', only
                    # a few parts can also be commands.
                    cmd_type = result[0]
                    cmd_value = result[1]
                    if cmd_type == 'play': 
                        scene = cmd_value
                        run_parts(scenes, scene)   

        elif part_type == 'call':
            call(*part_value)

        elif part_type == 'stop':
            stop()

        elif part_type == 'play':
            scene = part_value[0]
            run_parts(scenes, scene)