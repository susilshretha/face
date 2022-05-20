from ntpath import join
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import cv2 as cv
import os
import numpy as np
from time import strftime
from datetime import datetime




class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="FACE RECONGNITION",font=("times new roman",22,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1366,height=35)
        
        #first image
        img_top=Image.open(r"college_images\ss.jpg")
        img_top=img_top.resize((630, 650),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=630,height=650)
        
        # second image
        img_bottom=Image.open(r"college_images\face_re.jpg")
        img_bottom=img_bottom.resize((712, 650),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=640,y=45,width=712,height=650)
        
        # Button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",15,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=10,y=405,width=190,height=35)
        
    # attendance
    def mark_attendance(self,i,r,n,d):
        with open("Bamma.csv","w+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split(",")     #yesari lekhda ni hunxa   entry=line.split(( ", "))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) ) : 
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")



        

        
    # face recognition
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
        
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)  # size color and thikness
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))     # formula  for confidance 
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Nabin@.1?",database="face_recognizer")
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Id from student where Id="+ str(id))
                i=my_cursor.fetchone()
                # i="+".join(i)
                i=str(i)
                
                my_cursor.execute("select Roll from student where Id="+ str(id))
                r=my_cursor.fetchone()
                # r="+".join(r)
                r=str(r)   # second methood                
                     
                my_cursor.execute("select Name from student where Id="+ str(id))
                n=my_cursor.fetchone()
                # n="+".join(n)
                n=str(n) 
                
                
                my_cursor.execute("select Dep from student where Id="+ str(id))
                d=my_cursor.fetchone()
                # d="+".join(d)
                d=str(d)
                
                if predict < 500:
                    # if result[1] < 500:
                    confidence=int((100*(1-predict/300)))
                    # str2 = str(confidence)
                    # confidence = int(100 * (1 - (result[1])/300))
                    # display_string = str(confidence)+'% confidence it is user'
                # cv2.putText(img,display_string(250, 250), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
                    cv2.putText(img,f"Accuracy:{confidence}%",(x, y-95), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),3)
                
                
                
                
                if confidence>77:
                    cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord        

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)   
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        # video_cap=cv2.VideoCapture(0)  # laptop camera vayera 0 otherwise 1
        video_cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
        
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)   
            cv2.imshow("Welcome to face Recognition",img)

            if cv2.waitKey(1)==13:
                break;
        video_cap.release()
        cv2.destroyAllWindows()
        
        # # repeat
        # captureDevice = cv2.VideoCapture(0) #captureDevice = camera

        # while True:
        #     ret, frame = captureDevice.read() 

        #     cv2.imshow('my frame', frame)
        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break

        # captureDevice.release()
        # cv2.destroyAllWindows()
            

        
                        
                    
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()