import var
import const
import os
import json

def save_file(file_name):
    f = open('Map/' + file_name + '.txt', 'w')
    f.write(json.dumps(var.editor))
    f.close()

def load_file(file_name):
    try:
        f = open('Map/' + file_name + '.txt', 'r')
        line = f.readline()
        var.editor = json.loads(line)
        f.close()

    except FileNotFoundError:
        f = open('Map/' + file_name + '.txt', 'w')
        f.write(json.dumps(const.empty_editor))
        f.close()

        f = open('Map/' + file_name + '.txt', 'r')
        line = f.readline()
        var.editor = json.loads(line)
        f.close()

def make_file_list():
    var.file_list = []
    temp_dir = os.listdir('Map')

    for i in range(len(temp_dir)):
        name = temp_dir[i].split('.')[0]
        extension = temp_dir[i].split('.')[1]

        if extension == 'txt':
            var.file_list.append(name)

    var.file_list.sort()