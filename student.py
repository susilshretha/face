from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import re
import re as re2 
import cv2 as cv
import re
from datetime import datetime
# import smtplib 

  


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        


        # varibles
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_searchtxt=StringVar()
        self.var_search=StringVar()
        




        #first image
        img=Image.open(r"C:\Users\welcome\Desktop\Face_Recognition System\college_images\st1.jpg")
        img=img.resize((500, 130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second image
        img1=Image.open(r"C:\Users\welcome\Desktop\Face_Recognition System\college_images\cg.jpg")
        img1=img1.resize((500, 130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # third image
        img2=Image.open(r"C:\Users\welcome\Desktop\Face_Recognition System\college_images\st2.jpg")
        img2=img2.resize((500, 130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        # background image
        img3=Image.open(r"C:\Users\welcome\Desktop\Face_Recognition System\college_images\back.jpg")
        img3=img3.resize((1366, 768),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1366,height=780)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",20,"bold"),bg="lightblue",fg="darkred")
        title_lbl.place(x=0,y=0,width=1366,height=35)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=35,width=1340,height=540)

        # left side frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=2,y=2,width=660,height=520)

        img_left=Image.open(r"C:\Users\welcome\Desktop\Face_Recognition System\college_images\st3.jpg")
        img_left=img_left.resize((660, 90),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=2,y=0,width=660,height=90)

        # current course informatiom
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=90,width=648,height=108)

        #Department
        dep_label=Label(current_course_frame,text="Department :",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=5)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","IT","CMP","CIVIL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)

        # course
        course_label=Label(current_course_frame,text="Course :",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=17)
        course_combo["values"]=("Select Course","CN","CG","OODM","AI")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=8,sticky=W)
        # Year
        year_label=Label(current_course_frame,text="Year :",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=2,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year","2019-20","2020-21","2021-22","2022-23")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=8,sticky=W)

        # Semester
        semester_label=Label(current_course_frame,text="Semester :",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=2,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=17)
        semester_combo["values"]=("Select Semester","I","II","III","IV","V","VI","VII","VIII")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=8,sticky=W)

        # class student informatiom
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=2,y=200,width=648,height=294)

        # student id
        studentId_label=Label(class_Student_frame,text="StudentID :",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=2,pady=4,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_id,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=8,pady=4,sticky=W)
        
        #callnback and validate student name
        validate_ID=self.root.register(self.checkID)
        studentID_entry.config(validate='key',validatecommand=(validate_ID,'%P'))
        

        # student name
        studentName_label=Label(class_Student_frame,text="Student Name :",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=2,pady=4,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=8,pady=4,sticky=W)

        #callnback and validate student name
        validate_name=self.root.register(self.checkname)
        studentName_entry.config(validate='key',validatecommand=(validate_name,'%P'))
        
        
        # class division
        class_div_label=Label(class_Student_frame,text="Class Division :",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=2,pady=4,sticky=W)

        # class_div_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_div,font=("times new roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=8,pady=4,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,width=18,font=("times new roman",12,"bold"),state="readonly")
        div_combo["values"]=("Select Division","A","B","C","D","E","Other")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=8,pady=4,sticky=W)

        # Roll no
        roll_no_label=Label(class_Student_frame,text="RollNo :",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=2,pady=4,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=8,pady=4,sticky=W)

        #callnback and validate conntact
        validate_RollNo=self.root.register(self.checkRollNo)
        roll_no_entry.config(validate='key',validatecommand=(validate_RollNo,'%P'))
        

        # Gender
        gender_label=Label(class_Student_frame,text="Gender :",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=2,pady=4,sticky=W)

        # gender_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_gender,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=8,pady=4,sticky=W)
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=18,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Select gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=8,pady=4,sticky=W)

        # dob
        dob_label=Label(class_Student_frame,text="DOB :",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=2,pady=4,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_dob,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=8,pady=4,sticky=W)
        
        #callnback and validate conntact
        validate_DOB=self.root.register(self.validate)
        dob_entry.config(validate='key',validatecommand=(validate_DOB,'%P'))
        

        # Email
        email_label=Label(class_Student_frame,text="Email :",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=2,pady=4,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_email,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=8,pady=4,sticky=W)
        
        # #callnback and validate student name
        # validate_email=self.root.register(self.checkemail)
        # email_entry.config(validate='key',validatecommand=(validate_email,'%P'))
        
        
    

        # phone no
        phone_label=Label(class_Student_frame,text="PhoneNo :",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=2,pady=4,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_phone,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=8,pady=4,sticky=W)

        #callnback and validate conntact
        validate_phone=self.root.register(self.checkphone)
        phone_entry.config(validate='key',validatecommand=(validate_phone,'%P'))
        
        # Address
        address_label=Label(class_Student_frame,text="Address :",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=2,pady=4,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_address,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=8,pady=4,sticky=W)
        
        # #callnback and validate conntact
        # validate_add=self.root.register(self.checkadd)
        # address_entry.config(validate='key',validatecommand=(validate_add,'%P'))

        # Teacher Name
        teacher_label=Label(class_Student_frame,text="Teacher Name :",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=2,pady=4,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=8,pady=4,sticky=W)

        # radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=5,column=1)

        # button frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=1,y=190,width=642,height=35)

        save_button=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0)

        update_button=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=1)
        
        delete_button=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_button.grid(row=0,column=2)

        reset_button=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)

        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=1,y=230,width=642,height=35)

        take_photo_button=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=75,font=("times new roman",12,"bold"),bg="red",fg="white")
        take_photo_button.grid(row=0,column=0)

        # update_photo_button=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",12,"bold"),bg="red",fg="white")
        # update_photo_button.grid(row=0,column=1)





        # right side frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=670,y=2,width=660,height=520)

        img_right=Image.open(r"C:\Users\welcome\Desktop\Face_Recognition System\college_images\uml.jpg")
        img_right=img_right.resize((660, 90),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=2,y=0,width=660,height=90)

        # search system

        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=90,width=648,height=60)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",14,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=2,pady=4,sticky=W)

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_search,font=("times new roman",12,"bold"),state="readonly",width=12)
        search_combo["values"]=("Select","Id","Roll")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)

        search_entry=ttk.Entry(search_frame,textvariable=self.var_searchtxt,width=14,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=8,pady=4,sticky=W)


        search_button=Button(search_frame,command=self.search_data,text="Search",width=14,font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_button.grid(row=0,column=3,padx=3)
        
        # showAll_button=Button(search_frame,command=self.search_data,text="Show All",width=14,font=("times new roman",10,"bold"),bg="blue",fg="white")
        # showAll_button.grid(row=0,column=4,padx=3)
        # table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=155,width=648,height=340)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year") 
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photosamplestatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100) 
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=130)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=130)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=130)
        self.student_table.column("teacher",width=130)
        self.student_table.column("photo",width=130)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # function decleration
    def add_data(self):
        if self.var_dep.get()== "Select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="" :
            messagebox.showerror("Error","All Fields are Required, Smile please.",parent=self.root) 
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Nabin@.1?",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                                

                                                                                                              ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student Details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)


    #  fetch data to table from databasse 
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Nabin@.1?",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()    
        conn.close()    
        
        # get cursor for update data 
        
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
    # update function
    def update_data(self): 
        if self.var_dep.get()== "Select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="" :
            messagebox.showerror("Error","All Fields are Required, Smile please.",parent=self.root) 
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Nabin@.1?",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Sem=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosamplestatus=%s where Id=%s",(
                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                    self.var_std_id.get()


                                                                                                                                                                                                                                 ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("success","Student details successfully update completed",parent=self.root)    
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    #  DELETE FUNCTION 
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
            
        # elif self.var_email.get()=="":
        #     messagebox.showerror("Error","Please enter the valid email",parent=self.root)
        
        else:
            try:
                delete=messagebox.askyesno("student Delete page.","Do yo want to delete this student",parent=self.root)
                if delete>0: 
                    conn=mysql.connector.connect(host="localhost",username="root",password="Nabin@.1?",database="face_recognizer")
                    my_cursor=conn.cursor()  
                    sql="delete from student where ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()    
                messagebox.showinfo("Delete","Successfully deleted student details.",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    
    # reset functin 
    def reset_data(self): 
        self.var_dep.set("select department")
        self.var_course.set("select Course")
        self.var_year.set("select Year")
        self.var_semester.set("select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("select gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
    # generate data set or take photo 
    def generate_dataset(self):   
        if self.var_dep.get()== "Select Department" or self.var_std_name.get()==""or self.var_std_id.get()=="" :
            messagebox.showerror("Error","All Fields are Required, Smile please.",parent=self.root) 
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Nabin@.1?",database="face_recognizer")
                my_cursor=conn.cursor() 
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Sem=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photosamplestatus=%s where Id=%s",(
                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                self.var_std_id.get()==id+1

                                                                                                                                                                                                                ))  
                
                               
                           
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                # Load predefined data on face frontals from opencv 
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scalling factor =1.3
                    #minimum neighbor=5
                    
                    for ( x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))    
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/bamma." +str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()  
                messagebox.showinfo("Result","Generating data sets completed !! Thank You !")  
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
            
    # search data     
    def search_data(self):
        if self.var_searchtxt.get()=="" or self.var_search.get()=="Select Option":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password="Nabin@.1?",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.var_search.get())+" LIKE '%"+str(self.var_searchtxt.get())+"%'")
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
     
     
     
     
     
     
    def checkname(self,name):
        if name.isalnum():
            return True
        if name=='':
            return True
        else:
            messagebox.showerror('Invalid','Not allowed' +name[-1])
    def checkname(self,name):
       for char in name:
           if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
              return False
       return True 
    
    # def checkadd(self,add):
    #     if add.isalnum():
    #         return True
    #     if add=='':
    #         return True
    #     else:
    #         messagebox.showerror('Invalid','Not allowed' +add[-1])
    # def checkadd(self,name):
    #    for char in name:
    #        if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
    #           return False
    #    return True 
   
   
    def validate(self,date_text):
        try:
            datetime.datetime.strptime(date_text, '%d/%m/%Y')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")   
    # #check email
    # def checkemail(self,email):
    #     if email.isalnum():
    #         return True
    #     if email=='':
    #         return True
    #     else:
    #         messagebox.showerror('Invalid','Not Allowed' +email[-1])
    #         return False 
        
    #check studentid
    def checkID(self,ID):
        if ID.isdigit():
            return True
        if len(str(ID))==0:
            return True
        else:
            messagebox.showerror("Invalid","Invalid entry.")
            return False
    
    # #check phone no
    # def checkPhoneNo(self,PhoneNo):
    #     if PhoneNo.isdigit():
    #         return True
    #     if len(str(PhoneNo))==0:
    #         return True
    #     else:
    #         messagebox.showerror("Invalid","Invalid entry.")
    #         return False
    
    
    def checkphone(self,phone):
        if len(phone) <=10:
          if phone.isdigit():
            return True
          if len(str(phone))==0:
            return True
          else:
            messagebox.showerror('Invalid','Invalid entry')
            return False
            
        else:
            messagebox.showwarning('Alert','invalid phone enter phone (example:9869036535)')
            return False
    
    #check rollno
    def checkRollNo(self,RollNo):
        if RollNo.isdigit():
            return True
        if len(str(RollNo))==0:
            return True
        else:
            messagebox.showerror("Invalid","Invalid entry.")
            return False     
  
    
    # def checkemail(self,email):   
    #     regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'   
    #     if(re.search(regex,email)):   
    #         return True  
    #     else:   
    #         messagebox.showerror("Invalid","Invalid entry.")
    #         return False     
  
          
    # #check DOB
    # def checkDOB(self,DOB):
    #     if DOB.isdigit():
    #         return True
    #     if len(str(DOB))==0:
    #         return True
    #     else:
    #         messagebox.showerror("Invalid","Invalid entry.")
    #         return False        
                        
        

                    
                    
                                     
    # RegExp = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
    # def check(email):   
  
    #     if re.search(RegExp,email):
    #         print("Valid Email")   
    #     else:
    #         print("Invalid Email")   
      
    # if __name__ == '__main__' :   
      
    #     email = "rohit.gupta@mcnsolutions.net"  
    #     check(email)   
  
    #     email = "praveen@c-sharpcorner.com"  
    #     check(email)   
  
    #     email = "inform2atul@gmail.com"  
    #     check(email)
    # pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$' 
    # user_id=input('Enter the email id')
    # if re.search(pattern,user_id):
    #     print('valid email id')
    # else:
    #     print('invalid')
         
    
    
        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()