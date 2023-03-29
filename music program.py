import pygame
from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
import os
from pygame import mixer
home_directory = os.path.expanduser( '~' )
print( home_directory )

pygame.mixer.init()


root = Tk()
root.title("Music")
root.geometry("500x430+550+200")
root.resizable(0,0)
root.attributes('-topmost', True)
root.iconbitmap(f"c:\Program Files\music program\images\musical.ico")
img=PhotoImage(file="c:\Program Files\music program\images\musical.png")
Label(root,image=img,bg="black").place(x=0,y=0)
Frame(root,bg="black",width=1000,height=100).place(x=0,y=360)




songs=[]
current_song=""
paused=False
def load_music():
     global current_song
     global name
     global song
     song_list.delete(0,"end")
     root.directory=filedialog.askdirectory()# to select folder only...
     for song in os.listdir(root.directory):
        name,ext=os.path.splitext(song)
        if ext==".mp3":
            songs.append(song)
     for song in songs:
        song_list.insert("end",song)
     song_list.selection_set(0)
     current_song=songs[song_list.curselection()[0]]
Menubar=Menu(root)
root.config(menu=Menubar)
organise_menue=Menu(Menubar,tearoff=False)
def develober():
    messagebox.showinfo("Ahmed Ramadan Abd Elnaser","Contact Me On\nAhmed-Ramadan-Abd-Elnaser@protonmail.com")
    
Menubar.add_command(label="Devoleped By",command=develober,font=('DS-DIGIB',18,"bold"))
Menubar.add_command(label="Select Music Folder",background="black",command=load_music,font=('DS-DIGIB',18,"bold"))

def delete():
    deleet=song_list.delete(0,END)
    return deleet

def select():
    select=song_list.get("anchor")
    mixer.music.load(os.path.join(root.directory,select))
    mixer.music.play()

def play():
    global current_song
    pygame.mixer.music.load(os.path.join(root.directory,current_song))
    pygame.mixer.music.play()
    
    
     
def pause():
    global paused
    pygame.mixer.music.pause()
   

def next():
    
    global current_song
    song_list.selection_clear(0,END)
    song_list.select_set(songs.index(current_song)+1)
    current_song=songs[song_list.curselection()[0]]
    play()
    
def prev():
   global current_song
   song_list.selection_clear(0,END)
   song_list.select_set(songs.index(current_song)-1)
   current_song=songs[song_list.curselection()[0]]
   play()
  
   
def loop_music():
    global current_song
    pygame.mixer.music.play(-1)
def no_loop():
    pygame.mixer.music.play(loops=0)
    play()
    
    


play_music=PhotoImage(file="c:\Program Files\music program\images\play-buttton.png")
pause_music=PhotoImage(file=f"c:\Program Files\music program\images\pause.png")
next_music=PhotoImage(file=f"c:\\Program Files\\music program\\images\\arrowhead.png")
prev_music=PhotoImage(file="c:\Program Files\music program\images\previous.png")


play_button = Button(root, text="Play",image=play_music, command=select,activebackground="green",width=60,bd=0,height=0)
stop_button = Button(root, text="Stop", image=pause_music,command=pause,pady=0,activebackground="red",width=60,bd=0)
next_button =Button(root, text="Next", image=next_music,command=next,pady=0,activebackground="green",width=60,bd=0)
prev_button = Button(root, text="Prev",image=prev_music ,command=prev,pady=0,activebackground="green",width=60,bd=0)

song_list=Listbox(root,bg="black",fg="green",width=36,height=5,font=('DS-DIGIB',18,"bold"))
song_list.place(x=6,y=2)

scrollbar = Scrollbar(root)
  
# Adding Scrollbar to the right
# side of root window
scrollbar.pack(side = RIGHT, fill = BOTH)

song_list.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = song_list.yview)



button_mode=True
def loop():
    global button_mode
    if button_mode:
        loop_button.config(image=loop_repeat,activebackground="green",bd=0)
        loop_button.config(command=loop_music)
        button_mode=False    
    else:
        loop_button.config(image=repeat,activebackground="white",bd=0)
        loop_button.config(command=no_loop)
        button_mode=True
repeat=PhotoImage(file="c:\\Program Files\\music program\\images\\repeat.png")
loop_repeat=PhotoImage(file="c:\\Program Files\\music program\\images\\repeat-once.png")
loop_button = Button(root,image=repeat,command=loop,bd=0)
loop_button.place(x=430,y=370)
play_button.place(x=170,y=368)
stop_button.place(x=240,y=368)
next_button.place(x=320,y=368)
prev_button.place(x=90,y=368)

root.mainloop()



