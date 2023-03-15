import var
import const
import json

def map_validity_check():
    left_top_position = [var.editor['start_position'][0], var.editor['start_position'][1]]
    right_top_position = [var.editor['start_position'][0] + 32, var.editor['start_position'][1]]
    left_bottom_position = [var.editor['start_position'][0], var.editor['start_position'][1] + 32]
    right_bottom_position = [var.editor['start_position'][0] + 32, var.editor['start_position'][1] + 32]

    left_top_cell = [left_top_position[1] // 40, left_top_position[0] // 40]
    right_top_cell = [right_top_position[1] // 40, right_top_position[0] // 40]
    left_bottom_cell = [left_bottom_position[1] // 40, left_bottom_position[0] // 40]
    right_bottom_cell = [right_bottom_position[1] // 40, right_bottom_position[0] // 40]

    if var.editor['wall'][left_top_cell[0]][left_top_cell[1]] != 0:
        return False
    
    if var.editor['wall'][right_top_cell[0]][right_top_cell[1]] != 0:
        return False
    
    if var.editor['wall'][left_bottom_cell[0]][left_bottom_cell[1]] != 0:
        return False
    
    if var.editor['wall'][right_bottom_cell[0]][right_bottom_cell[1]] != 0:
        return False
    
    return True

def map_convert():
    var.play['player_position'] = json.loads(json.dumps(var.editor['start_position']))
    var.play['wall'] = json.loads(json.dumps(var.editor['wall']))
    var.play['block'] = json.loads(json.dumps(var.editor['block']))
    var.play['thing'] = json.loads(json.dumps(var.editor['thing']))
    var.play['player_yspeed'] = 0
    var.play['player_jump'] = 0
    var.play['background'] = json.loads(json.dumps(var.editor['background']))

    var.arrow_pressed['up'] = False
    var.arrow_pressed['down'] = False
    var.arrow_pressed['left'] = False
    var.arrow_pressed['right'] = False