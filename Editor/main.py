import pygame
import sys

import asset
import var
import const

import sceneplay
import sceneedit
import scenetitle

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.screen_size)
    pygame.display.set_caption('2D Platformer Editor')
    var.clock = pygame.time.Clock()

    load_font()
    load_image()

def load_font():
    pygame.font.init()
    const.Font.title = pygame.font.Font('Font/neodgm.ttf', 32)
    const.Font.main_1 = pygame.font.Font('Font/neodgm.ttf', 24)
    const.Font.main_2 = pygame.font.Font('Font/neodgm.ttf', 16)

def load_image():
    asset.Img.Icon.new = pygame.image.load('Image/Icon/New.png')

def main():
    while True:
        var.clock.tick(60)
        input_handle()
        loop_scene()

def loop_scene():
    if var.scene == 'title':
        scenetitle.loop()

    elif var.scene == 'edit':
        sceneedit.loop()

    elif var.scene == 'play':
        sceneplay.loop()

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            button = event.button

            if var.scene == 'title':
                scenetitle.mouse_up(x, y, button)

            elif var.scene == 'edit':
                sceneedit.mouse_up(x, y, button)

            elif var.scene == 'play':
                sceneplay.mouse_up(x, y, button)

init()
main()