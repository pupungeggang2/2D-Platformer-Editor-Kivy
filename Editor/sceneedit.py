import pygame

import asset
import var
import const
import UI

import json
import save
import draw
import physics
import editor

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    draw.draw_upper_bar()
    draw.draw_file_name_bar()
    draw.draw_lower_bar()
    draw.draw_left_bar()
    draw.draw_game_screen()

    if var.state == 'save':
        draw.draw_save_window()

    elif var.state == 'load':
        draw.draw_load_window()

    pygame.display.flip()

def edit_tile(x, y):
    if physics.point_inside_rect_array(x, y, UI.Game_Screen.rect):
        if var.pointer_mode == 'brush':
            if var.tab_mode == 'block':
                if var.selected_block != -1:
                    row = (y - UI.Game_Screen.rect[1]) // 40
                    column = (x - UI.Game_Screen.rect[0]) // 40

                    var.editor['block'][row][column] = const.button_list_block[var.selected_block]
                    var.editor['wall'][row][column] = 1

            elif var.tab_mode == 'goal':
                if var.selected_goal != -1:
                    row = (y - UI.Game_Screen.rect[1]) // 40
                    column = (x - UI.Game_Screen.rect[0]) // 40

                    temp_goal = {'ID' : const.button_list_goal[var.selected_goal], 'rect' : [column * 40, row * 40, 40, 40]}
                    var.editor['thing'].append(temp_goal)

        elif var.pointer_mode == 'erase':
            if var.tab_mode == 'block':
                row = (y - UI.Game_Screen.rect[1]) // 40
                column = (x - UI.Game_Screen.rect[0]) // 40
                var.editor['block'][row][column] = 0
                var.editor['wall'][row][column] = 0

            elif var.tab_mode == 'goal':
                screen_x = x - UI.Game_Screen.rect[0]
                screen_y = y - UI.Game_Screen.rect[1]

                for i in range(len(var.editor['thing'])):
                    if physics.point_inside_rect_array(screen_x, screen_y, var.editor['thing'][i]['rect']):
                        var.editor['thing'].pop(i)
                        break

        elif var.pointer_mode == 'move':
            if physics.point_inside_rect_array(x, y, UI.Game_Screen.rect):
                if x - UI.Game_Screen.rect[0] - 16 >= 0 and x - UI.Game_Screen.rect[0] - 16 <= 768 and y - UI.Game_Screen.rect[1] - 16 >= 0 and y - UI.Game_Screen.rect[1] - 16 <= 568:
                    var.editor['start_position'] = [x - UI.Game_Screen.rect[0] - 16, y - UI.Game_Screen.rect[1] - 16]

def mouse_down(x, y, button):
    if button == 1:
        var.mouse_pressed = True

        if var.state == '':
            edit_tile(x, y)

def mouse_motion(x, y):
    if var.mouse_pressed == True:
        if var.state == '':
            edit_tile(x, y)

def mouse_up(x, y, button):
    if button == 1:
        var.mouse_pressed = False

        if var.state == '':
            if physics.point_inside_rect_array(x, y, UI.Upper_Bar.save):
                if var.file_name == '':
                    var.state = 'save'
                    var.click_mode = ''
                    var.save_textbox = ''

                else:
                    save.save_file(var.file_name)

            elif physics.point_inside_rect_array(x, y, UI.Upper_Bar.new):
                var.state = ''
                var.file_name = ''
                var.editor = json.loads(json.dumps(const.empty_editor))
                var.pointer_mode = 'pointer'
                var.tab_mode = 'block'
                var.selected_block = -1
                var.selected_thing = -1
                var.selected_goal = -1

            elif physics.point_inside_rect_array(x, y, UI.Upper_Bar.load):
                var.state = 'load'
                save.make_file_list()
                var.load_page_number = 0
                var.load_selected_item = -1

            # Edit Icons
            if physics.point_inside_rect_array(x, y, UI.Upper_Bar.pointer):
                var.pointer_mode = 'pointer'

            elif physics.point_inside_rect_array(x, y, UI.Upper_Bar.brush):
                var.pointer_mode = 'brush'

            elif physics.point_inside_rect_array(x, y, UI.Upper_Bar.erase):
                var.pointer_mode = 'erase'

            elif physics.point_inside_rect_array(x, y, UI.Upper_Bar.move):
                var.pointer_mode = 'move'

            elif physics.point_inside_rect_array(x, y, UI.Upper_Bar.play):
                if editor.map_validity_check():
                    editor.map_convert()
                    var.scene = 'play'
                    var.state = 'play'

            elif physics.point_inside_rect_array(x, y, UI.Upper_Bar.close):
                var.scene = 'title'
                var.state = ''

            # Left Bar
            if physics.point_inside_rect_array(x, y, UI.Left_Bar.tab_block):
                var.tab_mode = 'block'

            elif physics.point_inside_rect_array(x, y, UI.Left_Bar.tab_thing):
                var.tab_mode = 'thing'

            elif physics.point_inside_rect_array(x, y, UI.Left_Bar.tab_goal):
                var.tab_mode = 'goal'

            elif physics.point_inside_rect_array(x, y, UI.Left_Bar.tab_background):
                var.tab_mode = 'background'

            if physics.point_inside_rect_array(x, y, UI.Left_Bar.rect):
                if var.tab_mode == 'block':
                    for i in range(len(const.button_list_block)):
                        row = i // 6
                        column = i % 6
                        
                        if physics.point_inside_rect(x, y, UI.Left_Bar.button_start[0] + column * 80, UI.Left_Bar.button_start[1] + row * 80, 80, 80):
                            if i == var.selected_block:
                                var.selected_block = -1
                            else:
                                var.selected_block = i

                elif var.tab_mode == 'thing':
                    pass

                elif var.tab_mode == 'goal':
                    for i in range(len(const.button_list_goal)):
                        row = i // 6
                        column = i % 6

                        if physics.point_inside_rect(x, y, UI.Left_Bar.button_start[0] + column * 80, UI.Left_Bar.button_start[1] + row * 80, 80, 80):
                            if i == var.selected_goal:
                                var.selected_goal = -1
                            else:
                                var.selected_goal = i

                elif var.tab_mode == 'background':
                    for i in range(len(const.button_list_background)):
                        row = i // 6
                        column = i % 6

                        if physics.point_inside_rect(x, y, UI.Left_Bar.button_start[0] + column * 80, UI.Left_Bar.button_start[1] + row * 80, 80, 80):
                            var.editor['background'] = const.button_list_background[i]

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
                    var.state = ''

        elif var.state == 'load':
            if physics.point_inside_rect_array(x, y, UI.Load_Window.close):
                var.state = ''

            for i in range(6):
                if physics.point_inside_rect_array(x, y, UI.Load_Window.file_list_rect[i]):
                    if var.load_page_number * 6 + i < len(var.file_list):
                        var.load_selected_item = i

                if physics.point_inside_rect_array(x, y, UI.Load_Window.button_next):
                    page_num_max = len(var.file_list) // 6
                    
                    if var.load_page_number + 1 <= page_num_max:
                        var.load_page_number += 1

                if physics.point_inside_rect_array(x, y, UI.Load_Window.button_prev):
                    if var.load_page_number > 0:
                        var.load_page_number -= 1

                if physics.point_inside_rect_array(x, y, UI.Load_Window.load_button):
                    if var.load_selected_item > -1:
                        var.file_name = var.file_list[var.load_page_number * 6 + var.load_selected_item]
                        save.load_file(var.file_name)
                        var.state = ''
                        var.click_mode = ''
                        var.tab_mode = 'block'
                        var.selected_block = -1
                        var.selected_thing = -1
                        var.selected_goal = -1

def key_down(key):
    if var.state == 'save':
        if var.click_mode == 'text_input':
            if key >= 97 and key <= 122 or key >= 48 and key <= 57:
                var.save_textbox += chr(key)

            if key == pygame.K_BACKSPACE:
                if len(var.save_textbox) > 0:
                    var.save_textbox = var.save_textbox[0:len(var.save_textbox) - 1]