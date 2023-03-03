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

def draw_left_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.rect, 2)

def draw_game_screen():
    pygame.draw.rect(var.screen, const.Color.black, UI.Game_Screen.rect, 2)

def draw_lower_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Lower_Bar.rect, 2)

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