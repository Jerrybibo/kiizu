import pygame as p
from constants import *
from pygame.locals import *

window_surface = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption("Kiizu - for Raymond", APP_ICON)


def menu():
    menu_background_color = BLACK
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
    menu()
    while 1:
        window_surface.fill(BLACK)

        for event in p.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    p.quit()
                    exit(0)
            if event.type == QUIT:
                p.quit()
                exit(0)

        p.display.update()


main()
