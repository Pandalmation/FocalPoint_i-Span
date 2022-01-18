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

#
w.configure(bg='#262626')
w.resizable(0,0)


l1=Label(w,text='Python',fg='white',bg='#262626')
l1.config(font=('Comic Sans MS',90))
l1.pack(expand=True)


def toggle_win():
    f1=Frame(w,width=300,height=500,bg='#12c4c0')
    f1.place(x=0,y=0)


    #buttons
    def bttn(x,y,text,bcolor,fcolor,cmd):
     
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= '#262626'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#262626'

        myButton1 = Button(f1,text=text,
                       width=42,
                       height=2,
                       fg='#262626',
                       border=0,
                       bg=fcolor,
                       activeforeground='#262626',
                       activebackground=bcolor,            
                        command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

    bttn(0,80,'A C E R','#0f9d9a','#12c4c0',None)
    bttn(0,117,'D E L L','#0f9d9a','#12c4c0',None)
    bttn(0,154,'A P P L E','#0f9d9a','#12c4c0',None)
    bttn(0,191,'A S U S','#0f9d9a','#12c4c0',None)
    bttn(0,228,'A C E R','#0f9d9a','#12c4c0',None)
    bttn(0,265,'A C E R','#0f9d9a','#12c4c0',None)

    #
    def dele():
        f1.destroy()

    global img2
    img2 = ImageTk.PhotoImage(Image.open('salir.png'))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#12c4c0',
           activebackground='#12c4c0').place(x=5,y=10)
    

img1 = ImageTk.PhotoImage(Image.open('menu.png'))

Button(w,image=img1,
       command=toggle_win,
       border=0,
       bg='#262626',
       activebackground='#262626').place(x=5,y=10)

screen.mainloop()
