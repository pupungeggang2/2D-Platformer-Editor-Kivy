import pygame

import asset
import var
import const
import UI

import save
import draw
import physics

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    draw.draw_upper_bar()
    draw.draw_lower_bar()
    draw.draw_left_bar()
    draw.draw_game_screen()

    if var.state == 'save':
        draw.draw_save_window()

    pygame.display.flip()

def mouse_up(x, y, button):
    if button == 1:
        if var.state == '':
            if physics.point_inside_rect_array(x, y, UI.Upper_Bar.save):
                if var.file_name == '':
                    var.state = 'save'
                    var.click_mode = ''
                    var.save_textbox = ''

                else:
                    save.save_file(var.file_name)

        elif var.state == 'save':
            if physics.point_inside_rect_array(x, y, UI.Save_Window.close):
                var.state = ''

            if physics.point_inside_rect_array(x, y, UI.Save_Window.text_box):
                if var.click_mode == '':
                    var.click_mode = 'text_input'

                elif var.click_mode == 'text_input':
                    var.click_mode = ''

            if physics.point_inside_rect_array(x, y, UI.Save_Window.button_save):
                if var.save_textbox != '':
                    save.save_file(var.save_textbox)
                    var.file_name = var.save_textbox

def key_down(key):
    if var.state == 'save':
        if var.click_mode == 'text_input':
            if key >= 97 and key <= 122 or key >= 48 and key <= 57:
                var.save_textbox += chr(key)

            if key == pygame.K_BACKSPACE:
                if len(var.save_textbox) > 0:
                    var.save_textbox = var.save_textbox[0:len(var.save_textbox) - 1]