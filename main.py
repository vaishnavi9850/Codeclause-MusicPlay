import tkinter as tk
from PIL import Image, ImageTk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x800")
canvas.config(bg="green")

rootpath = "E:\\Music Player using Python"
pattern = "*.mp3"
mixer.init()

prev_img = Image.open("E:/Music Player using Python/prev_button.jpg")
prev_img = ImageTk.PhotoImage(prev_img)

stop_img = Image.open("E:/Music Player using Python/stop_button.jpg")
stop_img = ImageTk.PhotoImage(stop_img)

play_img = Image.open("E:/Music Player using Python/play_button.png")
play_img = ImageTk.PhotoImage(play_img)

pause_img = Image.open("E:/Music Player using Python/pause_button.jpg")
pause_img = ImageTk.PhotoImage(pause_img)

next_img = Image.open("E:/Music Player using Python/next_button.jpg")
next_img = ImageTk.PhotoImage(next_img)

def select():
    label.config(text = listbox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listbox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listbox.select_clear('active')

def play_next():
    next_song = listbox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listbox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listbox.select_clear(0, 'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def play_prev():
    next_song = listbox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listbox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listbox.select_clear(0, 'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "Pause"

listbox = tk.Listbox(canvas, fg="cyan", bg="black", width=100, font=('poppins', 14))
listbox.pack(padx=15, pady=15)

label = tk.Label(canvas, text='', bg='black', fg='yellow', font=('poppins', 18))
label.pack(pady=15)

top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor='center')

prevButton = tk.Button(canvas, text="Prev", image=prev_img, bg='black', borderwidth=0, command=play_prev)
prevButton.pack(pady=15, in_=top, side='left')

stopButton = tk.Button(canvas, text="Stop", image=stop_img, bg='black', borderwidth=0, command=stop)
stopButton.pack(pady=15, in_=top, side='left')

playButton = tk.Button(canvas, text="Play", image=play_img, bg='black', borderwidth=0, command= select)
playButton.pack(pady=15, in_=top, side='left')

pauseButton = tk.Button(canvas, text="Pause", image=pause_img, bg='black', borderwidth=0, command=pause_song)
pauseButton.pack(pady=15, in_=top, side='left')

nextButton = tk.Button(canvas, text="Next", image=next_img, bg='black', borderwidth=0, command=play_next)
nextButton.pack(pady=15, in_=top, side='left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listbox.insert('end', filename)
canvas.mainloop()
