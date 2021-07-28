import pygame as p
from pygame.locals import *
from random import choice
from time import time

from constants import *
from helpers import create_text

p.init()

fullscreen_mode = False
flags = FULLSCREEN & fullscreen_mode
window_surface = p.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), flags)
p.display.set_caption("Kiizu - for Raymond")
APP_ICON = p.image.load(APP_ICON_URL)
p.display.set_icon(APP_ICON)

try:
    WORD_LIST_FILE = open("resources/word_list.txt")
    word_list = [i.rstrip("\n") for i in WORD_LIST_FILE.readlines()]
    WORD_LIST_FILE.close()
except OSError as err:
    print("OSError: {0}".format(err))

pressed_keys = []
current_word = ""
typed_word = ""
cpm = 0

replica_title_font = p.font.Font("resources/replica-bold.ttf", 128)
replica_subtitle_font = p.font.Font("resources/replica-bold.ttf", 64)
replica_small_font = p.font.Font("resources/replica-bold.ttf", 36)
notosans_font = p.font.Font("resources/notosans-regular.otf", 24)
clock = p.time.Clock()


def menu():
    menu_background_color = MINT
    while 1:
        window_surface.fill(menu_background_color)
        create_text(window_surface, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, "Press SPACE or RETURN to start",
                    replica_subtitle_font, fore_color=BLACK, align_x="center", align_y="center")
        create_text(window_surface, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 5 * 4,
                    "* Remember to press SPACE after each word!", replica_small_font,
                    fore_color=BLACK, align_x="center", align_y="center")
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
    global pressed_keys, current_word, typed_word, cpm
    menu()
    word_complete = False
    current_word = choice(word_list)
    next_word = choice(word_list)
    word_list.remove(current_word)
    word_list.remove(next_word)
    start_time = time()
    score = 0
    chars = 0
    while 1:
        window_surface.fill(BLUE)
        if word_complete:
            chars += len(current_word)
            score += 50 * len(current_word)
            cpm = round(chars / ((time() - start_time) / 60), 1)
            current_word = next_word
            next_word = choice(word_list)
            word_list.remove(next_word)
            typed_word = ""
            word_complete = False
        create_text(window_surface, 5, 0, str(len(word_list)) + " words left in bank", notosans_font,
                    fore_color=BLACK)
        create_text(window_surface, WINDOW_WIDTH - 5, 0, str(cpm) + " CPM", notosans_font,
                    fore_color=BLACK, align_x="right")
        create_text(window_surface, WINDOW_WIDTH / 2, WINDOW_HEIGHT, "SCORE: " + str(score), replica_small_font,
                    fore_color=BLACK, align_x="center", align_y="bottom")
        create_text(window_surface, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4, current_word, replica_title_font,
                    fore_color=BLACK, align_x="center", align_y="center")
        create_text(window_surface, WINDOW_WIDTH / 5 * 4, WINDOW_HEIGHT / 4, next_word, replica_subtitle_font,
                    fore_color=GRAY, align_x="center", align_y="center")
        create_text(window_surface, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4 * 3, typed_word, replica_title_font,
                    fore_color=CHARCOAL, align_x="center", align_y="center")
        for event in p.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    p.quit()
                    exit(0)
                if event.key == K_BACKSPACE and len(typed_word) > 0:
                    typed_word = typed_word[:-1]
                if event.key == K_SPACE:
                    if typed_word == current_word:
                        word_complete = True
                        continue
                typed_letter = p.key.name(event.key)
                if event.mod & (KMOD_LSHIFT | KMOD_RSHIFT):
                    typed_letter = typed_letter.upper()
                if len(typed_word) < len(current_word) and typed_letter == current_word[len(typed_word)]:
                    typed_word += current_word[len(typed_word)]
                else:
                    score -= 100
            if event.type == QUIT:
                p.quit()
                exit(0)

        p.display.update()
        clock.tick(60)


main()
