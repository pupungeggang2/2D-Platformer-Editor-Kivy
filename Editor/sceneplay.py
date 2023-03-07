import pygame

import asset
import var
import const
import UI

import draw
import physics
import game

def loop():
    loop_game()
    display()

def loop_game():
    game.player_move()

def display():
    var.screen.fill(const.Color.white)
    draw.draw_upper_play()
    draw.draw_game_screen_play()
    pygame.display.flip()

def mouse_up(x, y, button):
    if button == 1:
        if physics.point_inside_rect_array(x, y, UI.Upper_Play.stop):
            var.scene = 'edit'
            var.state = ''

def key_down(key):
    if var.state == 'play':
        if key == pygame.K_w or key == pygame.K_UP:
            var.arrow_pressed['up'] = True

        if key == pygame.K_a or key == pygame.K_LEFT:
            var.arrow_pressed['left'] = True

        if key == pygame.K_s or key == pygame.K_DOWN:
            var.arrow_pressed['down'] = True

        if key == pygame.K_d or key == pygame.K_RIGHT:
            var.arrow_pressed['right'] = True

def key_up(key):
    if var.state == 'play':
        if key == pygame.K_w or key == pygame.K_UP:
            var.arrow_pressed['up'] = False

        if key == pygame.K_a or key == pygame.K_LEFT:
            var.arrow_pressed['left'] = False

        if key == pygame.K_s or key == pygame.K_DOWN:
            var.arrow_pressed['down'] = False

        if key == pygame.K_d or key == pygame.K_RIGHT:
            var.arrow_pressed['right'] = False