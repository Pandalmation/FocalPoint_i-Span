from distutils.ccompiler import show_compilers
from time import time
import tkinter as tk
from tkinter import *
import random 
import sys
from PIL import ImageTk, Image


screen = Tk()
screen.geometry("600x900")
screen.title('I-SPAN')

#################
screen.configure(bg='#262626')
screen.resizable(0, 0)


l1 = Label(screen, text='I-SPAN', fg='white', bg='#262626')
l1.config(font=('Comic Sans MS', 90))
l1.pack(expand=True)

frame = Frame(screen)

def clearlogo():
    l1.destroy()
    
def mainmenu():
    global f1
    f1 = Frame(screen, width=400, height=500, bg='#12c4c0')
    f1.place(x=0, y=0)

    #buttons
    def bttn(x, y, text, bcolor, fcolor, cmd):

        def on_entera(e):
            myButton1['background'] = bcolor  # ffcc66
            myButton1['foreground'] = '#262626'  # 000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = '#262626'

        myButton1 = Button(f1, text=text,
                           width=20,
                           height=2,
                           fg='#262626',
                           border=0,
                           bg=fcolor,
                           activeforeground='#262626',
                           activebackground=bcolor,
                           command=cmd)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    bttn(0, 80, 'G A M E', '#0f9d9a', '#12c4c0', Cardgame)
    bttn(0, 117, 'M I S S I O N', '#0f9d9a', '#12c4c0', missions)
    bttn(0, 154, 'P R O G R E S S', '#0f9d9a', '#12c4c0', Progres)
    bttn(0, 191, 'S T O R E ', '#0f9d9a', '#12c4c0', shop)
    

    #
    def dele():
        f1.destroy()
    global img2
    img2 = ImageTk.PhotoImage(Image.open('menulinesr.png'))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#12c4c0',
           activebackground='#12c4c0').place(x=5,y=10)

img1 = ImageTk.PhotoImage(Image.open('menulinesr.png'))

Button(screen, image=img1,
       command=mainmenu,
       border=0,
       bg='#262626',
       activebackground='#262626').place(x=5, y=10)
timeleft = 30

def missions():
    def dele():
        f1.destroy()
    dele()
    clearlogo()

    def newl1():
        L1 = Label(screen, text='Missions', fg='white', bg='#262626')
        L1.config(font=('Arial', 48))
        L1.place(x= 190, y=0)

        L2 = Label(screen, text= 'Todays Missions = \n                                          * Get some fresh air go take a picture now outside\n* Eat a meal with veggies', fg= 'white', bg='#262626')
        L2.config(font=("Arial", 12))
        L2.place(x = 0, y= 100)

        L3 = Label(screen, text= 'RELAX')
        L3.config(font=("Arial", 12))
        L3.place(x = 130, y= 300)

        L4 = Label(screen, text= 'FITNESS')
        L4.config(font=("Arial", 12))
        L4.place(x = 270, y= 300)

        L5 = Label(screen, text= 'STUDY')
        L5.config(font=("Arial", 12))
        L5.place(x = 430, y= 300)

        L6 = Label(screen, text= 'DIET')
        L6.config(font=("Arial", 12))
        L6.place(x = 130, y= 400)

        L7 = Label(screen, text= 'RANDOM')
        L7.config(font=("Arial", 12))
        L7.place(x = 270, y= 400)

        L8 = Label(screen, text= 'ART')
        L8.config(font=("Arial", 12))
        L8.place(x = 430, y= 400)

        L9 = Label(screen, text= 'Todays Focal Points earned = 10')
        L9.config(font=("Arial", 12))
        L9.place(x = 130, y = 500)
    newl1()
def shop():
    def dele():
        f1.destroy()
    dele()
    clearlogo()
    def store():
        L1 = Label(screen, text='Store', fg='white', bg='#262626')
        L1.config(font=('Arial', 48))
        L1.place(x=210, y=0)

        L2 = Label(screen, text='Work in progress', fg='white', bg='#262626')
        L2.config(font=('Arial', 48))
        L2.place(x=70, y=280)
    store()
def Progres():
    def dele():
        f1.destroy()
    dele()
    clearlogo()
    def workinprogress():
        L1 = Label(screen, text='Progress', fg='white', bg='#262626')
        L1.config(font=('Arial', 48))
        L1.place(x=190, y=0)

        L2 = Label(screen, text='Work in Progress', fg='white', bg='#262626')
        L2.config(font=('Arial', 48))
        L2.place(x=50, y=280)
    workinprogress()
def Cardgame():
    def dele():
        f1.destroy()
    dele()
    clearlogo()
    def start(event):
        
        t2.config(text="")
        if timeleft==180:
            countdown()
        nextcolor()
        
    global s

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
            score.place (x= 260,y=300)
        if timeleft == 0:
            tk.messagebox.showinfo("Game Over",f"Hey your time is up and your score is {s}")
    def countdown():
        global timeleft
        
        if timeleft > 0:
            timeleft -= 1 
            tm=Label(screen, text='Time Left: ' + str(timeleft),font=("Arial",15),fg='red')
            tm.place (x=240, y=330)
            tm.after(1000,countdown)
            
        
    colours = ['Red','Blue','Orange','Green','Yellow','Pink','Purple','Brown','White']
    s=0
    t = Label(screen, text= "Please type the color of the text, not the word itself", font= ("Aria",17), fg ="red")
    t.place (x=50, y= 250)

    t2= Label(screen, text= "PRESS ENTER TO START", font= ('Aria',17), fg= "red")
    t2.place (x=180, y= 350)

    i= Entry(screen, font = ('Aria',17), fg= "black", width= 15)
    i.place (x=200, y= 600)

    text = Label(screen,font = ('Arial',100))
    text.place(x=150,y=400)

    screen.bind('<Return>', start)
    i.focus_set()

screen.mainloop()
