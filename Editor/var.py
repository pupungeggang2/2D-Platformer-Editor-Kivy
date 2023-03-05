screen = None
screen_size = [1280, 720]
FPS = 60
clock = None
lang = 'en'

scene = 'title'
state = ''
click_mode = ''
pointer_mode = 'pointer'
tab_mode = 'block'
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

save_textbox = ''