import pygame as p
from pygame.locals import *
from random import choice

from constants import *
from helpers import create_text

window_surface = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption("Kiizu - for Raymond", APP_ICON)

try:
    WORD_LIST_FILE = open("resources/word_list.txt")
    WORD_LIST = [i.rstrip("\n") for i in WORD_LIST_FILE.readlines()]
    WORD_LIST_FILE.close()
except OSError as err:
    print("OSError: {0}".format(err))

pressed_keys = []
current_word = ""

clock = p.time.Clock()

def menu():
    menu_background_color = MINT
    while 1:
        window_surface.fill(menu_background_color)
        for event in p.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    p.quit()
                    exit(0)
                if event.key in (K_RETURN, K_SPACE):
                    return
            if event.type == QUIT:
                p.quit()
                exit(0)

        p.display.update()


def main():
    global pressed_keys, current_word
    menu()
    word_complete = True
    while 1:
        window_surface.fill(BLUE)
        pressed_keys = p.key.get_pressed()
        if word_complete:
            current_word = choice(WORD_LIST)
        for event in p.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    p.quit()
                    exit(0)
            if event.type == QUIT:
                p.quit()
                exit(0)

        p.display.update()
        clock.tick(60)


main()
