from codecs import register
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student 
from time import strftime
from datetime import datetime
import os
from train import Train
from main import Face_Recognition_System
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
import cv2
import re 
from register import Register

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
    

 
class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System Login")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\welcome\Desktop\Face_Recognition System\college_images\bgg.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        
        # frame
        frame=Frame(self.root,bd=2,bg="black")
        frame.place(x=550,y=150,width=330,height=410)
        
        img1=Image.open(r"college_images\login.jpg")
        img1=img1.resize((100, 100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=665,y=150,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("cursive",17,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
        
        # label
        # password_lbl=Label(frame,text="Username",font=("cursive",14,"bold"),fg="white",bg="black")
        # password_lbl.place(x=70,y=155)
        
        # self.txtuser=ttk.Entry(frame,font=("cursive",14,"bold"))
        # self.txtuser.place(x=40,y=185,width=270)
        
        # #usename rakhera login garda
        # user_lbl=Label(frame,text="Username",font=("cursive",12,"bold"),fg="white",bg="black")
        # user_lbl.place(x=70,y=155)
        
        # self.txtuser=ttk.Entry(frame,font=("cursive",12,"bold"))
        # self.txtuser.place(x=40,y=185,width=270)
        
        # email rakhera login garda
        email_lbl=Label(frame,text="Email ",font=("cursive",12,"bold"),fg="white",bg="black")
        email_lbl.place(x=70,y=155)
        
        self.txtemail=ttk.Entry(frame,font=("cursive",12,"bold"))
        self.txtemail.place(x=40,y=185,width=270)
        
        username_lbl=Label(frame,text="Password ",font=("cursive",12,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,show="*",font=("cursive",12,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        
        # icon image
        img2=Image.open(r"college_images\login.jpg")
        img2=img2.resize((25, 25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)

        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=590,y=310,width=23,height=23)
        
        img3=Image.open(r"college_images\pass.jpg")
        img3=img3.resize((25, 25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)

        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=590,y=375,width=23,height=23)
        
        # button for login
        loginbtn=Button(frame,command=self.login,text="Login",activeforeground="white",activebackground="red",font=("times new roman",14,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
        loginbtn.place(x=110,y=290,width=100,height=30)
        
        # button for register
        registerbtn=Button(frame,text="New User Register",command=self.register_window,activeforeground="white",activebackground="black",font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black")
        registerbtn.place(x=15,y=320,width=150)
        
        # button for forget password
        btn=Button(frame,command=self.forgot_password_window,text="Forget Password",activeforeground="white",activebackground="black",font=("times new roman",12,"bold"),borderwidth=0,fg="white",bg="black")
        btn.place(x=10,y=360,width=150)
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
            
        
    def login(self):
        if self.txtemail.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All field are Required,smile please !")
        elif self.txtemail.get()=="nabinbamma99@gmail.com" and self.txtpass.get()=="Bamma@99" :
            messagebox.showinfo("Success","Welcome to Face Recognition system")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Nabin@.1?",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtemail.get(),
                                                                                        self.txtpass.get()
                                                                                     ))
            row=my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin Person.")    
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                    self.root.withdraw()
                   
                else:
                    if not open_main:
                        return
                conn.commit()
                conn.close()
                
                
                # reset password 
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","select Security Question ",parent=self.root2)            
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)        
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Nabin@.1?",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtemail.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")    
                value=(self.txt_newpass.get(),self.txtemail.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,please login with new password.",parent=self.root2)
                self.root2.destroy()

            
            
                
                
    #  forgot password window 
    def forgot_password_window(self):
        if self.txtemail.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Nabin@.1?",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtemail.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)
            
            if row==None:
                messagebox.showerror("Error","Please enter the valid email")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x400+950+170") 
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")   
                l.place(x=0,y=10,relwidth=1)
                
                security_Q=Label(self.root2,text="Select security Questions",font=("times new roman",15,"bold"),fg="black",bg="white")
                security_Q.place(x=50,y=80)
                
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",12,"bold"),state="readonly",width=17)
                self.combo_security_Q["values"]=("Select","Your Birth-Place","Your College Name","Your Favourite Color","Your Hobbies")
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=50,y=110,width=250)

                
                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
                security_A.place(x=50,y=140)
                
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=170,width=250)
                
                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black",bg="white")
                new_password.place(x=50,y=220)
                
                self.txt_newpass=ttk.Entry(self.root2,show="*",font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",18,"bold"),fg="white",bg="blue")
                btn.place(x=100,y=310)
                
                
            
                       
                            


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
       
    #    #callnback and validate conntact
    #     validate_PhoneNo=self.root.register(self.checkPhoneNo)
    #     self.txt_contact.config(validate='key',validatecommand=(validate_PhoneNo,'%P'))
        
        
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
        
        self.txt_pswd=ttk.Entry(frame,show="*",textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)
        
        cofirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        cofirm_pswd.place(x=370,y=310)
        
        self.txtcofirm_pswd=ttk.Entry(frame,show="*",textvariable=self.var_confpass,font=("times new roman",15))
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
        b1=Button(frame,command=self.return_login,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="black")
        b1.place(x=370,y=430,width=150)
       
        
        #  function declerataion    
        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
                messagebox.showerror("Error","All fields are required.")
        elif self.var_pass.get()!=self.var_confpass.get():
                messagebox.showerror("Error","Password and Confirm Password must be same.")
        # elif self.var_check.get()==0:
        #         messagebox.showerror("Error","Please agree our terms and conditions")       
        else:
           conn=mysql.connector.connect(host="localhost",username="root",password="Nabin@.1?",database="face_recognizer")
           my_cursor=conn.cursor()
           query=("select * from register where email=%s")
           value=(self.var_email.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
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

    def return_login(self):
        self.root.destroy()         



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        


        #first image
        img=Image.open(r"college_images\frs.jpg")
        img=img.resize((500, 130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second image
        img1=Image.open(r"college_images\face.jpg")
        img1=img1.resize((500, 130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # third image
        img2=Image.open(r"college_images\eec.jpg")
        img2=img2.resize((500, 130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        # background image
        img3=Image.open(r"college_images\back.jpg")
        img3=img3.resize((1366, 768),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1366,height=768)


        title_lbl=Label(bg_img,text="FACE RECONGNITION ATTENDENCE SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1366,height=45)
        
        # time 
        def time():
            string =strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        lbl=Label(title_lbl, font = ("times new roman",14,'bold'),background='white',foreground='blue')    
        lbl.place(x=0,y=0,width=110,height=50)
        time()
            

        # student button 
        img4=Image.open(r"college_images\student.jpg")
        img4=img4.resize((290, 290),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=90,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=280,width=220,height=40)
        
        
        # Detect Face button
        img5=Image.open(r"college_images\av.jpg")
        img5=img5.resize((220, 220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=90,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=280,width=220,height=40)


        # Attendence  button
        img6=Image.open(r"college_images\attendence.jpg")
        img6=img6.resize((220, 220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=90,width=220,height=220)

        b1_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=280,width=220,height=40)


        # Help Desk button
        img7=Image.open(r"college_images\help.jpg")
        img7=img7.resize((220, 220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=90,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=280,width=220,height=40)


        # Train button
        img8=Image.open(r"college_images\train.jpg")
        img8=img8.resize((220, 220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data,)
        b1.place(x=200,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=530,width=220,height=40)


        # photos button
        img9=Image.open(r"college_images\pp.jpg")
        img9=img9.resize((220, 220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img,)
        b1.place(x=500,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=530,width=220,height=40)


        # Developer button
        img10=Image.open(r"college_images\we.jpg")
        img10=img10.resize((220, 220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=530,width=220,height=40)


        # Exit button
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((220, 220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=350,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=530,width=220,height=40) 
        
    def open_img(self):
        os.startfile("data")  

        # function button

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit from this project, Good Luck !",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return    
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)    
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attandance(self.new_window)  
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window) 
        
        
        
        
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
    #     else:#
    #         messagebox.showinfo('Invalid',"Follow standard.")
    #         return False     
        #validation
      
                        
        
if __name__ == "__main__":
    main()
    
          
        
# if __name__ == "__main__":
#     root=Tk()
#     obj=Login_Window(root)
#     root.mainloop()        
    
