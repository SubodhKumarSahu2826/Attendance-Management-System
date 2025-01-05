from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
import csv
from datetime import datetime
import mysql.connector
import cv2
import numpy as np


class face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")
        self.root.config(bg="white")
        self.root.wm_iconbitmap("face.ico")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #2nd image
        img_top=Image.open(r"images\face.jpg")
        img_top=img_top.resize((1232,821))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1600,height=800)

        #button
        b1_1=Button(f_lbl, text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=350,y=600,width=200,height=40)
    
    #================Attendance=======================
    
    def mark_attendance(self,i,r,n,d):
        with open("attendance_report/record.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[] 
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            # if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
            print(name_list)
            if i not in name_list: 
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")  
                dtString=now.strftime("%H:%M:%S") 
                f.writelines(f"{i},{r},{n},{d},{dtString},{d1},Present\n")
                

                
            




    #================================Face Recognition================================

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="Caputdraconis7",database="face_recognizer")
                my_cursor=conn.cursor()


                my_cursor.execute("select Name from student where Student_ID="+str(id))
                n=my_cursor.fetchone()
                n="".join(n)

                my_cursor.execute("select Roll_No from student where Student_ID="+str(id))
                r=my_cursor.fetchone()
                r="".join(r)

                my_cursor.execute("select Department from student where Student_ID="+str(id))
                d=my_cursor.fetchone()
                d="".join(d)

                my_cursor.execute("select Student_ID from student where Student_ID="+str(id))
                i=my_cursor.fetchone()
                i="".join(i)
                
                if confidence>82:
                    cv2.putText(img,f"ID:{i}",(x,y-70),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                    break
            
                else:   
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        cap=cv2.VideoCapture(0)

        while True:
            ret,img=cap.read()

            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==27:
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__ =="__main__":
    root=Tk()
    obj=face_recognition(root)
    root.mainloop()

