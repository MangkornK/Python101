import tkinter as tk
from tkinter import ttk
import time

def record_time():
    current_time = time.strftime("%H:%M:%S")
    with open("work_log.txt", "a") as log:
        log.write("Started work at: " + current_time + "\n")
    start_time_label.config(text="Started work at: " + current_time)

root = tk.Tk()
root.title("Work Logger")

start_time_label = ttk.Label(root, text="")
start_time_label.pack()

record_time_button = ttk.Button(root, text="Record Start Time", command=record_time)
record_time_button.pack()
