from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",20,"bold"),bg="lightblue",fg="red")
        title_lbl.place(x=0,y=0,width=1366,height=35)
        
        img_top=Image.open(r"college_images\helpp.jpg")
        img_top=img_top.resize((1366, 640),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1366,height=640)
        
        dev_label=Label(f_lbl,text="Email: nabinbamma99@gmail.com",font=("times new roman",15,"bold"),fg="black",bg="white")
        dev_label.place(x=110,y=25)
        dev_label=Label(f_lbl,text="Phone: +977 9869036535",font=("times new roman",15,"bold"),fg="black",bg="white")
        dev_label.place(x=110,y=60)        
        dev_label=Label(f_lbl,text="Address: Kathmandu,Nepal",font=("times new roman",15,"bold"),fg="black",bg="white")
        dev_label.place(x=110,y=95)
        dev_label=Label(f_lbl,text="Viber: +977 9869036535",font=("times new roman",15,"bold"),fg="black",bg="white")
        dev_label.place(x=110,y=130)        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()