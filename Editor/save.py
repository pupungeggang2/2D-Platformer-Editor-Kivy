import var
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

    except FileNotFoundError:
        return