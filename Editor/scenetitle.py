import pygame
import json

import asset
import var
import const
import UI

import draw
import save
import physics

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    var.screen.blit(const.Font.title.render('2D Platformer Editor', False, const.Color.black), UI.title_text)
    
    pygame.draw.rect(var.screen, const.Color.black, UI.new_button, 2)
    var.screen.blit(const.Font.title.render('New File', False, const.Color.black), UI.new_text)
    pygame.draw.rect(var.screen, const.Color.black, UI.load_button, 2)
    var.screen.blit(const.Font.title.render('Load File', False, const.Color.black), UI.load_text)

    if var.state == 'load':
        draw.draw_load_window()

    pygame.display.flip()

def mouse_up(x, y, button):
    if button == 1:
        if var.state == '':
            if physics.point_inside_rect_array(x, y, UI.new_button):
                var.scene = 'edit'
                var.state = ''
                var.file_name = ''
                var.editor = json.loads(json.dumps(const.empty_editor))
                var.pointer_mode = 'pointer'
                var.tab_mode = 'block'
                var.selected_block = -1
                var.selected_thing = -1
                var.selected_goal = -1

            if physics.point_inside_rect_array(x, y, UI.load_button):
                var.state = 'load'
                save.make_file_list()
                var.load_page_number = 0
                var.load_selected_item = -1

        elif var.state == 'load':
            if physics.point_inside_rect_array(x, y, UI.Load_Window.close):
                var.state = ''

            for i in range(6):
                if physics.point_inside_rect_array(x, y, UI.Load_Window.file_list_rect[i]):
                    if var.load_page_number * 6 + i < len(var.file_list):
                        var.load_selected_item = i

                if physics.point_inside_rect_array(x, y, UI.Load_Window.load_button):
                    if var.load_selected_item > -1:
                        var.file_name = var.file_list[var.load_page_number * 6 + var.load_selected_item]
                        save.load_file(var.file_name)
                        var.scene = 'edit'
                        var.state = ''
                        var.click_mode = ''
                        var.pointer_mode = 'pointer'
                        var.tab_mode = 'block'
                        var.selected_block = -1
                        var.selected_thing = -1
                        var.selected_goal = -1

def key_down(key):
    pass