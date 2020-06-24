import os
from math import ceil
import time
import threading
import tkinter.messagebox
from tkinter import *
from pygame import mixer
from mutagen.mp3 import MP3
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import themed_tk as tk
import youtube_dl
from tkinter.ttk import Progressbar

root = tk.ThemedTk()
root.geometry('750x750')
root.resizable(False,False)

root.get_themes()
root.set_theme("plastik")



statusbar = ttk.Label(root, text="My Music Player", relief=tkinter.RAISED, anchor=tkinter.N,background='#3dc1d3',
                      font="Verdana 15 italic", )  # W stands for West
statusbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)

menubar = Menu(root)
root.config(menu=menubar)
root["bg"] = "#82ccdd"


def about_us():
    tkinter.messagebox.showinfo('info', 'You are trying the GUI made by PRERNA')


playlist = []


def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)

def del_song():
    try:
        selected_song = playlistbox.curselection()
        selected_song = int(selected_song[0])
        playlistbox.delete(selected_song)
        playlist.pop(selected_song)
    except:
        tkinter.messagebox.showwarning('Error', 'Add Music to delete')

def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    playlist.insert(index, filename_path)

    index += 1


submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open", command=browse_file)
submenu.add_command(label="Exit", command=root.destroy)

submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="About us", command=about_us)

mixer.init()

root.title("Music Player")

root.iconbitmap('playericon.ico')

fileLabel = ttk.Label(root, text="Without music, life would be a mistake", font="Helvetica 20 italic",
                      foreground="cyan", background="darkorchid")
fileLabel.pack()

leftframe = Frame(root, bg="#82ccdd")
leftframe.pack(side=tkinter.LEFT)

playlistbox = Listbox(leftframe, bg="thistle2", width=30)
playlistbox.grid(row=1,column=0,columnspan=2)

danceimage = PhotoImage(file="dance.png")
dancephoto = Label(leftframe, image=danceimage, anchor=N, height=400, background="#82ccdd")
dancephoto.grid(row=0,column=0,columnspan=2)

addimage = PhotoImage(file="plus.png")
addbutton = ttk.Button(leftframe, image=addimage, command=browse_file)
addbutton.grid(row=2,column=0)

delimage = PhotoImage(file="sub.png")
delbuttton = ttk.Button(leftframe, image=delimage, command=del_song)
delbuttton.grid(row=2,column=1)







rightframe = Frame(root, pady=30, bg="#82ccdd")
rightframe.pack()

topframe = Frame(rightframe, bg="pink1")
topframe.grid(row=0,column=0,columnspan=3,rowspan=2,pady=30)

lengthlabel = Label(topframe, text='Total Length - --/--', bg="pink1")
lengthlabel.grid(row=0,column=0,rowspan=2)


def downloadmusic():
    musiclink = str(dwnldbox.get())
    params = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'

        }]
    }
    music = youtube_dl.YoutubeDL(params)
    music.download([musiclink])
    statusbar['text'] = "Music Downloaded!"


def show_details(play_song):
    fileLabel['text'] = "Playing " + ' ' + os.path.basename(play_song)

    file_data = os.path.splitext(play_song)
    if (file_data[1] == ".mp3"):
        audio = MP3(play_song)
        total_length = int(audio.info.length)
        ProgressbarMusic['maximum'] = total_length

        def teer():
            current_pos = mixer.music.get_pos() / 1000
            ProgressbarMusic['value'] = current_pos
            ProgressbarMusic.after(200, teer)

        teer()

    else:

        a = mixer.Sound(play_song)
        total_length = a.get_length()

    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)

    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlabel['text'] = "Total Length" + ' ' + timeformat

    


global paused, ProgressbarMusic
paused = tkinter.FALSE


def play_music():
    global paused
    if paused:
        mixer.music.unpause()
        statusbar['text'] = "Music Resumed"
        paused = tkinter.FALSE

        def teer():
            current_pos = mixer.music.get_pos() / 1000
            ProgressbarMusic['value'] = current_pos
            ProgressbarMusic.after(200, teer)

        teer()





    else:

            stop_music()
            time.sleep(1)
            selected_song = playlistbox.curselection()
            selected_song = int(selected_song[0])
            play_it = playlist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            statusbar['text'] = "Playing Music" + ' ' + os.path.basename(play_it)
            show_details(play_it)
            def teer():
                current_pos = mixer.music.get_pos() / 1000
                ProgressbarMusic['value'] = current_pos
                ProgressbarMusic.after(200, teer)

            teer()



            paused = tkinter.TRUE


def stop_music():
    mixer.music.stop()
    statusbar['text'] = "Music Stopped"


def set_vol(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)


def pause_music():
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = "Music Paused"


muted = FALSE


def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(70)
        volumebtn.configure(image=volumephoto)
        scale.set(70)
        muted = tkinter.FALSE
    else:
        muted = TRUE
        mixer.music.set_volume(0)
        volumebtn.configure(image=mutephoto)
        scale.set(0)


middleframe = Frame(rightframe, bg="#82ccdd")
middleframe.grid(row=2,column=0,columnspan=3,pady=30)

playphoto = PhotoImage(file="play.png")
playbtn = ttk.Button(middleframe, image=playphoto, command=play_music)
playbtn.grid(row=0, column=0, padx=10)

stopphoto = PhotoImage(file="stop.png")
stopbtn = ttk.Button(middleframe, image=stopphoto, command=stop_music)
stopbtn.grid(row=0, column=1, padx=10)

pausephoto = PhotoImage(file="pause.png")
pausebtn = ttk.Button(middleframe, image=pausephoto, command=pause_music)
pausebtn.grid(row=0, column=2, padx=10)

bottomframe = Frame(rightframe, bg="#82ccdd")
bottomframe.grid(row=3,column=0,columnspan=3,pady=30)

mutephoto = PhotoImage(file="mute.png")
volumephoto = PhotoImage(file="volume.png")
volumebtn = ttk.Button(bottomframe, image=volumephoto, command=mute_music)
volumebtn.grid(row=0, column=1)

scale = ttk.Scale(bottomframe, from_=0, to=100, orient=tkinter.HORIZONTAL, command=set_vol)
scale.set(50)
mixer.music.set_volume(0.5)
scale.grid(row=0, column=2,padx=20)

downloadframe = Frame(rightframe,bg="#82ccdd")
downloadframe.grid(row=5,column=0,pady=30)

downloadlabel = Label(downloadframe,text="Download Section:",font="couriernew 20 italic",fg="#f8a5c2",bg="#574b90")
downloadlabel.grid(row=0,column=0)



downloadimage = PhotoImage(file="download.png")
downloadbtn = ttk.Button(downloadframe, image=downloadimage, command=downloadmusic)
downloadbtn.grid(row=1,column=4,padx=20)


dot=StringVar()
dd="Enter your url"
dot.set(dd)
dwnldbox = ttk.Entry(downloadframe,textvariable=dot,width=50)
dwnldbox.grid(row=1,column=0,columnspan=4)


def on_closing():
    stop_music()
    root.destroy()


current_pos = 0
s = ttk.Style()
s.theme_use('alt')
s.configure("lightskyblue.Horizontal.TProgressbar", foreground='#c70039', background='#c70039')


progressframe = Frame(rightframe,bg="#82ccdd")
progressframe.grid(row=4,column=0,pady=30)

ProgressbarLabel_music = Label(progressframe, bg='lightskyblue', width=80)
ProgressbarLabel_music.grid(row=0,column=0)

ProgressbarMusic = Progressbar(ProgressbarLabel_music, orient=HORIZONTAL, style="lightskyblue.Horizontal.TProgressbar",
                               mode='determinate', value=current_pos, length=440)
ProgressbarMusic.grid(row=0, column=0)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()