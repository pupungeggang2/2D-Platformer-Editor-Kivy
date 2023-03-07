screen = None
screen_size = [1280, 720]
FPS = 60
clock = None
lang = 'en'

# Input Variables
mouse_pressed = True
arrow_pressed = {
    'up' : False,
    'down' : False,
    'left' : False,
    'right' : False
}

# Mode Variables
scene = 'title'
state = ''
click_mode = ''
pointer_mode = 'pointer'
tab_mode = 'block'

# Variables from Editing
selected_block = -1
selected_thing = -1
selected_goal = -1

file_name = ''
file_list = []
load_page_number = 0
load_selected_item = -1

editor = {
    'start_position' : [],
    'wall' : [],
    'block' : [],
    'thing' : [],
}

play = {
    'player_position' : [],
    'wall' : [],
    'block' : [],
    'thing' : [],
    'player_speed' : 160,
    'player_yspeed' : 0,
    'player_ground' : False,
    'terminal_speed' : 800,
    'gravity' : 600,
    'player_jump' : 1,
    'player_jump_power' : -400,
}

save_textbox = ''