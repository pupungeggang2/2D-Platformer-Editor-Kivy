import pygame

import asset
import var
import const
import UI

def draw_upper_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Upper_Bar.rect, 2)
    var.screen.blit(asset.Img.Icon.new, UI.Upper_Bar.new)
    var.screen.blit(asset.Img.Icon.load, UI.Upper_Bar.load)
    var.screen.blit(asset.Img.Icon.save, UI.Upper_Bar.save)
    var.screen.blit(asset.Img.Icon.pointer, UI.Upper_Bar.pointer)
    var.screen.blit(asset.Img.Icon.brush, UI.Upper_Bar.brush)
    var.screen.blit(asset.Img.Icon.erase, UI.Upper_Bar.erase)
    var.screen.blit(asset.Img.Icon.move, UI.Upper_Bar.move)
    var.screen.blit(asset.Img.Icon.play, UI.Upper_Bar.play)

    if var.pointer_mode == 'pointer':
        pygame.draw.rect(var.screen, const.Color.green, UI.Upper_Bar.pointer, 2)

    elif var.pointer_mode == 'brush':
        pygame.draw.rect(var.screen, const.Color.green, UI.Upper_Bar.brush, 2)

    elif var.pointer_mode == 'erase':
        pygame.draw.rect(var.screen, const.Color.green, UI.Upper_Bar.erase, 2)

    elif var.pointer_mode == 'move':
        pygame.draw.rect(var.screen, const.Color.green, UI.Upper_Bar.move, 2)

def draw_file_name_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.File_Name_Bar.rect, 2)
    var.screen.blit(const.Font.title.render(var.file_name, False, const.Color.black), UI.File_Name_Bar.text)

def draw_left_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.rect, 2)

    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.tab_block, 2)
    var.screen.blit(asset.Img.Icon.block, UI.Left_Bar.icon_block)
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.tab_thing, 2)
    var.screen.blit(asset.Img.Icon.coin, UI.Left_Bar.icon_thing)
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.tab_goal, 2)
    var.screen.blit(asset.Img.Icon.flag, UI.Left_Bar.icon_goal)
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.tab_background, 2)
    var.screen.blit(asset.Img.Icon.background, UI.Left_Bar.icon_background)

    if var.tab_mode == 'block':
        pygame.draw.rect(var.screen, const.Color.green, UI.Left_Bar.tab_block, 2)

        for i in range(0, len(const.button_list_block)):
            row = i // 6
            column = i % 6

            pygame.draw.rect(var.screen, const.Color.black, [UI.Left_Bar.button_start[0] + column * 80, UI.Left_Bar.button_start[1] + row * 80, 80, 80], 2)
            var.screen.blit(asset.Img.block[const.button_list_block[i]], [UI.Left_Bar.button_start[0] + column * 80 + 20, UI.Left_Bar.button_start[1] + row * 80 + 20])

        if var.selected_block != -1:
            row = var.selected_block // 6
            column = var.selected_block % 6
            pygame.draw.rect(var.screen, const.Color.green, [UI.Left_Bar.button_start[0] + column * 80, UI.Left_Bar.button_start[1] + row * 80, 80, 80], 2)

def draw_game_screen():
    pygame.draw.rect(var.screen, const.Color.black, UI.Game_Screen.rect, 2)
    var.screen.blit(asset.Img.player, [UI.Game_Screen.rect[0] + var.editor['start_position'][0], UI.Game_Screen.rect[1] + var.editor['start_position'][1]])

    for i in range(15):
        for j in range(20):
            if var.editor['block'][i][j] != 0:
                var.screen.blit(asset.Img.block[var.editor['block'][i][j]], [UI.Game_Screen.rect[0] + j * 40, UI.Game_Screen.rect[1] + i * 40])

    for i in range(15):
        for j in range(20):
            pygame.draw.rect(var.screen, const.Color.gray, [UI.Game_Screen.rect[0] + j * 40, UI.Game_Screen.rect[1] + i * 40, 40, 40], 1)

def draw_lower_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Lower_Bar.rect, 2)
    var.screen.blit(const.Font.title.render(var.pointer_mode, False, const.Color.black), UI.Lower_Bar.text_mode)

def draw_save_window():
    pygame.draw.rect(var.screen, const.Color.white, UI.Save_Window.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.rect, 2)

    var.screen.blit(const.Font.title.render('Save', False, const.Color.black), UI.Save_Window.window_title)
    var.screen.blit(asset.Img.Icon.close, UI.Save_Window.close)

    var.screen.blit(const.Font.title.render('Name', False, const.Color.black), UI.Save_Window.text_name)

    if var.click_mode == '':
        pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.text_box, 2)
    elif var.click_mode == 'text_input':
        pygame.draw.rect(var.screen, const.Color.green, UI.Save_Window.text_box, 2)

    var.screen.blit(const.Font.title.render(var.save_textbox, False, const.Color.black), UI.Save_Window.file_name)

    var.screen.blit(const.Font.title.render('Save', False, const.Color.black), UI.Save_Window.text_save)
    pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.button_save, 2)

def draw_load_window():
    pygame.draw.rect(var.screen, const.Color.white, UI.Load_Window.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Load_Window.rect, 2)

    var.screen.blit(const.Font.title.render('Load', False, const.Color.black), UI.Load_Window.window_title)
    var.screen.blit(asset.Img.Icon.close, UI.Load_Window.close)

    for i in range(6):
        pygame.draw.rect(var.screen, const.Color.black, UI.Load_Window.file_list_rect[i], 2)

    for i in range(6):
        if i < len(var.file_list):
            var.screen.blit(const.Font.title.render(var.file_list[var.load_page_number * 6 + i], False, const.Color.black), UI.Load_Window.file_list_text[i])

    pygame.draw.rect(var.screen, const.Color.black, UI.Load_Window.load_button, 2)
    var.screen.blit(const.Font.title.render('Load', False, const.Color.black), UI.Load_Window.load_text)

    if var.load_selected_item > -1:
        pygame.draw.rect(var.screen, const.Color.green, UI.Load_Window.file_list_rect[var.load_selected_item], 2)