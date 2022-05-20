from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student 
from time import strftime
from datetime import datetime
import os
from train import Train
import numpy as  np 
from attendace import Attandance
from developer import Developer
from help import Help



class Validation:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Register page using voice.")

        # image
        self.bg=ImageTk.PhotoImage(file=r"college_images\back.jpg")
        bg_lbl=Label(self.root,image=self.bg,bd=2,relief=RAISED)
        bg_lbl.place(x=0,y=0,width=1366,height=768)
        
        logo_img=Image.open(file=r"college_images\login.jpg")
        logo_img=logo_img.resize((60, 60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(logo_img)
                
        # title frame 
        title_frame=Frame(self.root,bd=1,relief=RIDGE)
        title_frame.place(x=450,y=28,width=550,height=82)
        
        title_lbl=Label(title_frame,text="USER REGISTRATION FORM",font=("times new roman",30,"bold"),fg="darkblue")
        title_lbl.place(x=10,y=10)

        
        # information frame 
        main_frame=Frame(self.root,bd=1,relief=RIDGE)
        main_frame.place(x=450,y=110,width=550,height=520)




if __name__ == "__main__":
    root=Tk()
    obj=Validation(root)
    root.mainloop()        