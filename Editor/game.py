import var
import const
import physics

def find_surrounding_cells(position):
    center_point = [position[0] + 16, position[1] + 16]
    center_point_row = int(center_point[1] // 40)
    center_point_column = int(center_point[0] // 40)
    row_col_list = []

    for i in range(-2, 3):
        for j in range(-2, 3):
            if 0 <= center_point_row + i and center_point_row + i <= 14 and 0 <= center_point_column + j and center_point_column + j <= 19:
                row_col_list.append([(center_point_column + j) * 40, (center_point_row + i) * 40, center_point_row + i, center_point_column + j])

    return row_col_list

def player_defeat_check():
    if var.play['player_position'][1] > 600:
        return True
    
    return False

def player_win_check():
    player_center = [var.play['player_position'][0] + 16, var.play['player_position'][1] + 16]

    for i in range(len(var.play['thing'])):
        if var.play['thing'][i]['ID'] == 102:
            if physics.point_inside_rect_array(player_center[0], player_center[1], var.play['thing'][i]['rect']):
                return True
            
    return False

def player_move():
    temp_position = [var.play['player_position'][0], var.play['player_position'][1]]

    if var.arrow_pressed['right'] == True:
        temp_position[0] += var.play['player_speed'] / var.FPS

    elif var.arrow_pressed['left'] == True:
        temp_position[0] -= var.play['player_speed'] / var.FPS

    var.play['player_ground'] = False

    temp_position[1] += var.play['player_yspeed'] / var.FPS

    surrounding = find_surrounding_cells([temp_position[0] + 16, temp_position[1] + 16])

    if var.play['player_yspeed'] < 0:
        for i in range(len(surrounding)):
            if physics.point_inside_rect(temp_position[0] + 16, temp_position[1] + 16, surrounding[i][0] + const.collide_bottom_rect[0], surrounding[i][1] + const.collide_bottom_rect[1], const.collide_bottom_rect[2], const.collide_bottom_rect[3]) and var.play['wall'][surrounding[i][2]][surrounding[i][3]] == 1:
                var.play['player_yspeed'] = 0
                temp_position[1] = surrounding[i][1] + 40
                break
    
    if var.play['player_yspeed'] >= 0:
        for i in range(len(surrounding)):
            if physics.point_inside_rect(temp_position[0] + 16, temp_position[1] + 16, surrounding[i][0] + const.collide_top_rect[0], surrounding[i][1] + const.collide_top_rect[1], const.collide_top_rect[2], const.collide_top_rect[3]) and var.play['wall'][surrounding[i][2]][surrounding[i][3]] == 1:
                var.play['player_yspeed'] = 0
                temp_position[1] = surrounding[i][1] - 32
                var.play['player_ground'] = True
                var.play['player_jump'] = 1
                break

    if var.play['player_ground'] == False:
        if var.play['player_yspeed'] + var.play['gravity'] / var.FPS >= var.play['terminal_speed']:
            var.play['player_yspeed'] = var.play['terminal_speed']
        else:
            var.play['player_yspeed'] += var.play['gravity'] / var.FPS

    for i in range(len(surrounding)):
        if physics.point_inside_rect(temp_position[0] + 16, temp_position[1] + 16, surrounding[i][0] + const.collide_right_rect[0], surrounding[i][1] + const.collide_right_rect[1], const.collide_right_rect[2], const.collide_right_rect[3]) and var.play['wall'][surrounding[i][2]][surrounding[i][3]] == 1:
            temp_position[0] = surrounding[i][0] + 40
            break

        if physics.point_inside_rect(temp_position[0] + 16, temp_position[1] + 16, surrounding[i][0] + const.collide_left_rect[0], surrounding[i][1] + const.collide_left_rect[1], const.collide_left_rect[2], const.collide_left_rect[3]) and var.play['wall'][surrounding[i][2]][surrounding[i][3]] == 1:
            temp_position[0] = surrounding[i][0] - 32
            break

    var.play['player_position'] = [temp_position[0], temp_position[1]]

def jump():
    if var.play['player_jump'] > 0:
        var.play['player_jump'] -= 1
        var.play['player_yspeed'] = var.play['player_jump_power']