from tkinter import *
from PIL import Image,ImageTk
from pygame import mixer
import time

songs = ["highrated.mp3","tuaakdekhle.mp3","nocompetition.mp3","maanmerijaan.mp3"]
root = Tk()
root.geometry("600x500")
root.title("Music Player")
root.resizable(0,0)
i  = 0

mixer.init()
def playsong():
  global i
  print(i)
  mixer.music.load(songs[i])
  mixer.music.play()

def pausesong():
  mixer.music.pause()

def nextsong():
  global i
  if i>=4:
    i = -1
  i+=1
  print(i)
  mixer.music.load(songs[i])
  mixer.music.play()

def prevsong():
  global i 
  if i >=4:
    i = 4
  if i<=0:
    i = 4
  i-=1
  print(i)
  mixer.music.load(songs[i])
  mixer.music.play()

def unpauseMusic():
    mixer.music.unpause()


# heading
header = Frame(root,bg="white",width=600,height=60)
header.pack(fill=X,side=TOP)
Label(header,text="Music Player",fg="black",bg="white",font="Merriweather 28 bold").pack()

# pic
display = Frame(root,bg="green",width=600,height=350)
display.pack()
image = Image.open('concertpng.png')
resize_image = image.resize((600,350))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(display,image=img)
label1.pack()

# controls
controls = Frame(root,bg="white",width=600,height=70)
controls.pack(fill=X)

next_pic = PhotoImage(file='resized.png')
pause_pic = PhotoImage(file='pauseresized.png')
play_pic = PhotoImage(file='playresized.png')
prev_pic = PhotoImage(file='prevresized.png')
unpause_pic = PhotoImage(file='unpauseresized.png')

prev = Button(controls,image=prev_pic,borderwidth=0,command=prevsong)
prev.grid(row=0,column=1,padx=35)
pause = Button(controls,image=pause_pic,borderwidth=0,command=pausesong)
pause.grid(row=0,column=2,padx=30)
play = Button(controls,image=play_pic,borderwidth=0,command=playsong)
play.grid(row=0,column=3,padx=30)
unpause = Button(controls,image=unpause_pic,borderwidth=0,command=unpauseMusic)
unpause.grid(row=0,column=4,padx=30)
play.grid(row=0,column=5,padx=30)
next_ = Button(controls,image=next_pic,borderwidth=0,command=nextsong)
next_.grid(row=0,column=6,padx=30)

Label(root,bg="white").pack(fill=X)

last = Frame(root,bg="black")
last.pack(fill=X)
Label(last,text="Music is Life Itself",font="verdana 12 italic",bg="black",fg="white").pack(side=RIGHT,fill="x",anchor="ne")

root.mainloop()