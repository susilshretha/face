from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",20,"bold"),bg="lightblue",fg="darkred")
        title_lbl.place(x=0,y=0,width=1366,height=35)
        
        img_top=Image.open(r"college_images\bb.jpg")
        img_top=img_top.resize((1366, 640),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1366,height=640)
        
        # frame 
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=850,y=0,width=550,height=540)
        
        img_top1=Image.open(r"college_images\p1.jpg")
        img_top=img_top1.resize((150, 150),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=330,y=2,width=200,height=200)
        
        #developerr info
        dev_label=Label(main_frame,text="We are Nabin,Rabin,Santosh & Susil",font=("times new roman",15,"bold"),fg="black",bg="white")
        dev_label.place(x=0,y=5)
        dev_label=Label(main_frame,text="We are IT Engineer",font=("times new roman",15,"bold"),fg="black",bg="white")
        dev_label.place(x=0,y=35)
        dev_label=Label(main_frame,text="We are from EEC",font=("times new roman",15,"bold"),fg="black",bg="white")
        dev_label.place(x=0,y=65)
        dev_label=Label(main_frame,text="We want to upgrade our project.",font=("times new roman",15,"bold"),fg="black",bg="white")
        dev_label.place(x=0,y=95)
        
        
        img2=Image.open(r"C:\Users\welcome\Desktop\Face_Recognition System\college_images\st2.jpg")
        img2=img2.resize((500, 320),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=210,width=500,height=320)

        
        




if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()