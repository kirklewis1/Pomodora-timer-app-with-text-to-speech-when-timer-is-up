import tkinter as tk
import time
import winsound
import win32com.client as wincl

def start_timer():
    global running
    running = True
    minutes = int(entry.get())
    seconds = minutes * 60
    while running and seconds > 0:
        display_time = time.strftime('%M:%S', time.gmtime(seconds))
        label.config(text=display_time)
        time.sleep(1)
        root.update()
        seconds -= 1
    label.config(text="Time's up!", font=("Helvetica", 14))
    winsound.Beep(1000, 5000) # Play a 1000Hz beep for 5 seconds
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak("Time's up!")

def stop_timer():
    global running
    running = False

def reset_timer():
    global running
    running = False
    label.config(text="", font=("Helvetica", 14))

root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("200x150")

entry = tk.Entry(root, width=5, font=("Helvetica", 14))
entry.pack()

label = tk.Label(root, text="", font=("Helvetica", 14))
label.pack()

start_button = tk.Button(root, text="Start", command=start_timer, font=("Helvetica", 14))
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_timer, font=("Helvetica", 14))
stop_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_timer, font=("Helvetica", 14))
reset_button.pack()

running = False

root.mainloop()


