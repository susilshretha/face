from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student 
from time import strftime
from datetime import datetime
import os
from train import Train
from face_recognition import Face_Recognition
import numpy as  np 
from attendace import Attandance
from developer import Developer
from help import Help
import time
import random
import datetime
import mysql.connector
from tkinter import messagebox
import re

# import smtplib,ssl



class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System Register")

        # varialbes 
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
      
       

        
        
        
        
        
        # bg image 
        self.bg=ImageTk.PhotoImage(file=r"college_images\back.jpg")

        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,width=1366,height=768)

        #  left image 
        self.bg1=ImageTk.PhotoImage(file=r"college_images\fru.jpg")

        left_lbl1=Label(self.root,image=self.bg1)
        left_lbl1.place(x=40,y=130,width=450,height=500)
        
        # main frame 
        frame=Frame(self.root,bg="white")
        frame.place(x=455,y=130,width=700,height=500)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="black")
        register_lbl.place(x=20,y=20)
        
        # first row
        # label and entry 
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=140,width=250)
        
        # last name
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        l_name.place(x=370,y=100)
        
        # last name entry 
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=140,width=250)

        # second row
        # label and entry 
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)
        
        #callnback and validate conntact
        validate_PhoneNo=self.root.register(self.checkPhoneNo)
        self.txt_contact.config(validate='key',validatecommand=(validate_PhoneNo,'%P'))
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)
        
        # 3rd row
        # label and entry 
        security_Q=Label(frame,text="Select security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_Q.place(x=50,y=240)
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",12,"bold"),state="readonly",width=17)
        self.combo_security_Q["values"]=("Select","Your Birth-Place","Your College Name","Your Favourite Color","Your Hobbies")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50,y=270,width=250)

        
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_A.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)
        
        # 4th row
        # label and entry 
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        pswd.place(x=50,y=310)
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        cofirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        cofirm_pswd.place(x=370,y=310)
        
        self.txtcofirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txtcofirm_pswd.place(x=370,y=340,width=250)
        
        #  check button
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,onvalue=1,offvalue=0,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"))
        self.checkbtn.place(x=50,y=380)
        
        #  button 
        img=Image.open(r"C:\Users\welcome\Desktop\Face_Recognition System\college_images\rr.jpg")
        img=img.resize((100,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="black",bg="white")
        b1.place(x=50,y=430,width=200)
        
        img1=Image.open(r"C:\Users\welcome\Desktop\Face_Recognition System\college_images\loginn.jpg")
        img1=img1.resize((100,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="black")
        b1.place(x=370,y=430,width=150)
        
        #  function declerataion    
        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
                messagebox.showerror("Error","All fields are required.")
        elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","Password and Confirm Password must be same.")
        elif self.var_check.get()==0:
                messagebox.showerror("Error","Please agree our terms and conditions")       
        else:
           conn=mysql.connector.connect(host="localhost",username="root",password="Nabin@.1?",database="face_recognizer")
           my_cursor=conn.cursor()
           query=("select * from register where email=%s")
           value=(self.var_email.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
        #    print row
           if row!=None:
               messagebox.showerror("Error","User already exist,Please try another email")
           else:   
                my_cursor.execute("Insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                        
                                                                                         ))
                                                                                        
                        
                conn.commit()
                conn.close()
                messagebox.showinfo("success","Register successfully",parent=self.root)                                                                              


    #check phone no
    def checkPhoneNo(self,PhoneNo):
        if PhoneNo.isdigit():
            return True
        if len(str(PhoneNo))==0:
            return True
        else:
            messagebox.showerror("Invalid","Invalid entry.")
            return False
        
    # def checkpassword(self,password):
    #     if len(password)<=21:
    #         if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",password):
    #             return True
    #         else:
    #             messagebox.showerror('Invalid','Enter valid password like Nabin@123 ')
    #             return False
    #     else:
    #         messagebox.showerror('Invalid',"Length try to exceed")
    #         return False       
            
    # def checkemail(self,email):
    #     if len(email)>7:
    #         if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)([a-zA-z]{2,5})$",email):
    #             return True
    #         else:
    #             messagebox.showwarning('Alert','Invalid email Enter valid email like nabin99@gmail.com ')
    #             return False
    #     else:
    #         messagebox.showinfo('Invalid',"Follow standard.")
      
    #         return False   
    
    # def checkemail(self,Email):    
    #     pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
    #     user_id=input('Enter the email id')
    #     if re.search(pattern,user_id):
    #      print('valid email id')
    #     else:
    #      print('invalid')
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()         