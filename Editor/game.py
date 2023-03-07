import var
import const

def player_move():
    temp_position = [var.play['player_position'][0], var.play['player_position'][1]]

    if var.arrow_pressed['right'] == True:
        temp_position[0] += var.play['player_speed'] / var.FPS

    elif var.arrow_pressed['left'] == True:
        temp_position[0] -= var.play['player_speed'] / var.FPS

    var.play['player_position'] = [temp_position[0], temp_position[1]]