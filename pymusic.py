## example of simple music player using pygame

from tkinter import *
import pygame
import os


class MusicPlayer: #adapter class that adapt the interface object
  def __init__(self,root):
    self.root = root
    # Title of the window
    self.root.title("PyMusic")

    self.root.iconbitmap("C:\icon\icon.ico")
    # Window Geometry
    self.root.geometry("500x300")
    # Initiating Pygame
    pygame.init()
    # Initiating Pygame Mixer
    pygame.mixer.init()
    # Declaring track Variable
    self.track = StringVar()

    frame = Frame(self.root)
    frame.pack()

    scroll = Scrollbar(frame,orient=VERTICAL)
    
    self.songbox = Listbox(frame,yscrollcommand=scroll.set,selectbackground="gray",selectmode=SINGLE, bg="blue", font=("arial",12, "bold"),width=40,relief=GROOVE)

    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=self.songbox.yview)
    self.songbox.pack(fill=BOTH)


    btn_frame = Frame(self.root)
    btn_frame.pack()
    
    play_btn = Button(btn_frame,bg="gray",command=self.playsong, text="PLAY", font=("ARIAL", 12, "bold"), fg="white", borderwidth=4)
    pause_btn = Button(btn_frame,bg="gray",command=self.pausesong,text="PAUSE", font=("ARIAL", 12, "bold"),fg="white", borderwidth=4)
    unpause_btn = Button(btn_frame,bg="gray",command=self.unpausesong, text="UNPAUSE", font=("ARIAL", 12, "bold"),fg="white", borderwidth=4)
    stop_btn = Button(btn_frame,bg="gray",command=self.stopsong, text="STOP", font=("ARIAL", 12, "bold"),fg="white", borderwidth=4)

    play_btn.grid(row=0, column=0)
    pause_btn.grid(row=0, column=1)
    unpause_btn.grid(row=0, column=2)
    stop_btn.grid(row=0, column=3)

    os.chdir("C:\Python\musics")
    # Fetching Songs
    songtracks = os.listdir()
    # Inserting Songs into Playlist
    for track in songtracks:
      self.songbox.insert(END,track)

  def playsong(self):# interface object
    # Loading Selected Song
    pygame.mixer.music.load(self.songbox.get(ACTIVE))
    # Playing Selected Song
    pygame.mixer.music.play()

  def pausesong(self):# interface object
    # Paused Song
    pygame.mixer.music.pause()

  def unpausesong(self):# interface object
    # Playing back Song
    pygame.mixer.music.unpause()

  def stopsong(self):# interface object
    # Stopped Song
    pygame.mixer.music.stop()

# Creating TK Container
root = Tk()
# Passing Root to MusicPlayer Class
MusicPlayer(root)
# Root Window Looping
root.mainloop()
