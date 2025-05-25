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

def fadein(image, duration=in_duration):
    add_to_render(image)
    frames = int(duration * fps)
    for frame in range(frames):
        alpha = int(255 * (1 - frame / frames))
        images[image].image.set_alpha(alpha)
        screen.fill((0, 0, 0))
        draw()
        pygame.display.flip()

        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == QUIT:
                return 'exit_game'
            if event.type == KEYDOWN and keys.get(event.key) == 'ok':
                # Skip fade, show image fully visible immediately
                images[image].image.set_alpha(0)
                screen.fill((0, 0, 0))
                draw()
                pygame.display.flip()
                return 'skipped'
    return 'done'

def hold(duration=hold_duration):
    frames = int(duration * fps)
    for _ in range(frames):
        screen.fill((0, 0, 0))
        pygame.display.flip()

        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == QUIT:
                return 'exit_game'
            if event.type == KEYDOWN and keys.get(event.key) == 'ok':
                return 'skipped'
    return 'done'

def fadeout(image, duration=out_duration):
    add_to_render(image)
    frames = int(duration * fps)
    for frame in range(frames):
        alpha = int(255 * (frame / frames))
        images[image].image.set_alpha(alpha)
        screen.fill((0, 0, 0))
        draw()
        pygame.display.flip()

        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == QUIT:
                return 'exit_game'
            if event.type == KEYDOWN and keys.get(event.key) == 'ok':
                # Skip fade, show image fully faded immediately
                images[image].image.set_alpha(255)
                screen.fill((0, 0, 0))
                draw()
                pygame.display.flip()
                return 'skipped'
    return 'done'


def fade(in_image, out_image, in_=in_duration, hold_=hold_duration, out_=out_duration):
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and keys.get(event.key) == 'exit_game'):
                return 'exit_game'

        result = fadein(in_image, in_)
        if result == 'exit_game':
            return 'exit_game'

        result = hold(hold_)
        if result == 'exit_game':
            return 'exit_game'

        result = fadeout(out_image, out_)
        if result == 'exit_game':
            return 'exit_game'

        return 'fade_end'

def dialogue(text):
    i = 0
    while True:
        clock.tick(fps)
        i = len(text) if text_speed == 0 else i + text_speed

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and keys.get(event.key) == 'exit_game'):
                return 'exit_game'

            if event.type == KEYDOWN and keys.get(event.key) == 'ok':
                if i >= len(text):
                    return
                i = len(text)

        screen.fill('black')
        draw()
        Text(text[:int(i)]).draw()
        pygame.display.update()

def cdialogue(text):
    i = 0
    while True:
        clock.tick(fps)
        i = len(text) if text_speed == 0 else i + text_speed

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and keys.get(event.key) == 'exit_game'):
                return 'exit_game'

            if event.type == KEYDOWN and keys.get(event.key) == 'ok':
                if i >= len(text):
                    return
                i = len(text)

        screen.fill('black')
        draw()
        CenteredText(text[:int(i)]).draw()
        pygame.display.update()

def menu(items):
    if 'dialogue' in items:
        dialogue_text = items['dialogue']
        current_option = 1
    else:
        dialogue_text = None
        current_option = 0

    options_break = '\n'

    i = 0

    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and keys.get(event.key) == 'exit_game'):
                return 'exit_game'                        

            if event.type == KEYDOWN:
                if keys.get(event.key) == 'move_up':
                    current_option = (current_option - 1) % len(items)
                    if list(items.keys())[current_option] == 'dialogue':
                        current_option = len(options.keys())-1

                elif keys.get(event.key) == 'move_down':
                    current_option = (current_option + 1) % len(items)
                    if list(items.keys())[current_option] == 'dialogue':
                        current_option = 1
                elif keys.get(event.key) == 'ok':
                    item_name, item_value = list(items.items())[current_option]
                    if callable(item_value):
                        return item_value()
                    else:
                        return item_value

        screen.fill('black')
        draw()

        if dialogue_text:
            text = Text(dialogue_text)
            text.draw()

        for i, (item_name, item_value) in enumerate(items.items()):
            if item_name != 'dialogue':
                if i == current_option:
                    if dialogue_text: option = Text(options_break * (i + 1) + item_name, color=text_selected_color, box=box_select_color)
                    else: option = Text(options_break * i + item_name, color=text_selected_color, box=box_select_color)
                else:
                    if dialogue_text: option = Text(options_break * (i + 1) + item_name, color=text_selected_color)
                    else: option = Text(options_break * i + item_name, color=text_unselected_color)

                option.draw()

        pygame.display.update()


def cmenu(items, fit_text=False):
    if 'dialogue' in items:
        dialogue_text = items['dialogue']
        current_option = 1
    else:
        dialogue_text = None
        current_option = 0

    options_break = '\n'

    i = 0

    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and keys.get(event.key) == 'exit_game'):
                return 'exit_game'                        

            if event.type == KEYDOWN:
                if keys.get(event.key) == 'move_up':
                    current_option = (current_option - 1) % len(items)
                    if list(items.keys())[current_option] == 'dialogue':
                        current_option = len(options.keys())-1

                elif keys.get(event.key) == 'move_down':
                    current_option = (current_option + 1) % len(items)
                    if list(items.keys())[current_option] == 'dialogue':
                        current_option = 1
                elif keys.get(event.key) == 'ok':
                    item_name, item_value = list(items.items())[current_option]
                    if callable(item_value):
                        return item_value()
                    else:
                        return item_value

        screen.fill('black')
        draw()

        if dialogue_text:
            text = Text(dialogue_text)
            text.draw()

        for i, (item_name, item_value) in enumerate(items.items()):
            if item_name != 'dialogue':
                if i == current_option:
                    if dialogue_text: option = CenteredText(options_break * (i + 1) + item_name, color=text_selected_color, box=box_select_color, box_fit_text=fit_text)
                    else: option = CenteredText(options_break * i + item_name, color=text_selected_color, box=box_select_color, box_fit_text=fit_text)
                else:
                    if dialogue_text: option = CenteredText(options_break * (i + 1) + item_name, color=text_selected_color, box_fit_text=fit_text)
                    else: option = CenteredText(options_break * i + item_name, color=text_unselected_color, box_fit_text=fit_text)

                option.draw()

        pygame.display.update()


def run_parts(scenes, scene):
    # Executor for a scene.
    for part in scenes[scene]:
        part_type, *part_value = part
        print(part)

        if part_type == 'loader':
            loader(*part_value)
        elif part_type == 'add':
            add_to_render(part_value[0])
        elif part_type == 'fade':
            result = fade(*part_value)
            if result == 'exit_game':
                return
        elif part_type == 'delete':
            delete(part_value[0])
        elif part_type in ['dialogue', 'cdialogue']:
            func = dialogue if part_type == 'dialogue' else cdialogue
            if func(*part_value) == 'exit_game':
                return
        elif part_type in ['menu', 'cmenu']:
            func = menu if part_type == 'menu' else cmenu
            result = func(*part_value)
            if result == 'exit_game':
                return
            if isinstance(result, (list, tuple)):
                if result[0] == 'play':
                    run_parts(scenes, result[1])

        elif part_type == 'call':
            call(*part_value)
        elif part_type == 'sound':
            sound(*part_value)
        elif part_type == 'stop':
            stop()
        elif part_type == 'play':
            run_parts(scenes, part_value[0])
