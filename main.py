from os import write
from pynput.keyboard import Listener

def write_to_file(data):
    with open("saved_data.txt","w") as f:
        f.write(str(data))
        f.close()

write_to_file("dasda")