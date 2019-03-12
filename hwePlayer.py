# !/usr/bin/python3
from tkinter import *
from pygame import mixer
import glob, os
import requests
import time

top = Tk()
top.geometry("800x460")
#top.attributes("-fullscreen", True)

os.chdir(os.getcwd())


files = glob.glob("*.ogg")



mixer.init()

class Player():

    def __init__(self, title):
        self.title = title

    def play(self): 
        mixer.music.load(self.title)
        mixer.music.play()
        requests.post("http://192.168.4.1",data={'state':1})

i = 0
for x in files: 
    name = os.path.splitext(files[i])[0]
    x = Button(top, text = name, command = Player(x).play, bg="gray")
    x.place(x = 20, width = 760, y = 20 + i * ((460 - (len(files) + 1) * 20) / len(files) + 20), height = (460 - (len(files) + 1) * 20) / len(files))
    i = i + 1


def task():
    if mixer.music.get_busy() == 0:
        requests.post("http://192.168.4.1", data={'state':0})            
    top.after(500, task)  # reschedule event in 1 seconds


top.after(500, task)
top.mainloop()



