from time import time
import tkinter as tk
from tkinter import *

import random 


screen = Tk()
screen.geometry("600x900")
screen.title('Colour game')

timeleft = 30
def start(event):
    t2.config(text="")
    if timeleft==30:
        countdown()
    nextcolor()

def nextcolor():
    global s
    global timeleft

    if timeleft > 0:
        i.focus_set()
        if i.get().lower()==colours[1].lower():
            s+=1
        i.delete(0,END)
        random.shuffle(colours)
        text.config (fg=str(colours[1]), text= str(colours[0]))
        score=Label (text="score : " + str(s),font=("Arial",15),fg="red")
        score.place (x= 220,y=90)
    if timeleft == 0:
        tk.messagebox.showinfo("Game Over",f"Hey your time is up and your score is {s}")

def countdown():
    global timeleft
    
    if timeleft > 0:
        timeleft -= 1 
        tm=Label(screen, text='Time Left: ' + str(timeleft),font=("Arial",15),fg='red')
        tm.place (x=220, y=120)
        tm.after(1000,countdown)
        
    
    
        
colours = ['Red','Blue','Orange','Green','Yellow','Pink','Purple','Brown','White']
s=0
t = Label(screen, text= "Please type the color of the text, not the word itself", font= ("Aria",17), fg ="red")
t.place (x=50, y= 30)

t2= Label(screen, text= "PRESS ENTER TO START", font= ('Aria',17), fg= "red")
t2.place (x=180, y= 80)

i= Entry(screen, font = ('Aria',17), fg= "black", width= 15)
i.place (x=200, y= 400)

text = Label(screen,font = ('Arial',100))
text.place(x=150,y=190)

screen.bind('<Return>', start)
i.focus_set()

screen.mainloop()