import pygame

import asset
import var
import const
import UI

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

    pygame.display.flip()

def mouse_up(x, y, button):
    if button == 1:
        if var.state == '':
            if physics.point_inside_rect_array(x, y, UI.new_button):
                var.scene = 'edit'
                var.state = ''
                var.Editor.file_name = ''