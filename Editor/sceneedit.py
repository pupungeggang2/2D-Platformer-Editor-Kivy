import pygame

import asset
import var
import const
import UI

import draw
import physics

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    draw.draw_upper_bar()
    draw.draw_lower_bar()
    pygame.display.flip()

def mouse_up(x, y, button):
    pass