from tkinter import *
from tkinter import ttk
from os import system
from tkinter import Button
from tkinter import Label
from tkinter import Entry
from tkinter import Tk
from tkinter import messagebox
import pickle

window = Tk()
window.title("FC")
window.attributes("-fullscreen",True)
window.configure(bg='BLACK' )
label_title = Label(window, text="GENDER AND EMOTION CLASSIFICATION SYSTEM",width=60  ,height=2 , bg='YELLOW', fg='BLACK' ,font=('times', 30, ' bold ') ) 
label_title.place(x=0,y=0 )



def predict_all():
    cmd = "python video_emotion_gender.py"
    system(cmd)

def predict_gender():
    cmd = "python video_gender.py"
    system(cmd)

def predict_emotion():
    cmd = "python video_emotion.py"
    system(cmd)

take_group_att_btn = Button(window, text="GENDER AND EMOTION CLASSIFIER", bg="blue", fg="white", command=predict_all, font=('times', 20, ' bold '))
take_group_att_btn.place(relx=0.3, rely=0.3, )
take_group_att_btn = Button(window, text="GENDER CLASSIFIER", bg="red", fg="white", command=predict_gender, font=('times', 20, ' bold '))
take_group_att_btn.place(relx=0.35, rely=0.4,  )
take_group_att_btn = Button(window, text="EMOTION CLASSIFIER", bg="green", fg="white", command=predict_emotion, font=('times', 20, ' bold '))
take_group_att_btn.place(relx=0.35, rely=0.5,  )
take_group_att_btn = Button(window, text="EXIT", bg="red", fg="white", command=quit, font=('times', 12, ' bold '))
take_group_att_btn.place(relx=0.96, rely=0.01,  )
window.mainloop()