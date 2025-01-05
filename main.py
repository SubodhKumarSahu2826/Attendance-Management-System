from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import student
from train import*
from face_recognition import*
from developer import*
from attendance import*
import os


class face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Attendance Management System")
        self.root.config(bg="white")
        self.root.wm_iconbitmap("face.ico")

        #Background
        img1=Image.open(r"images\bgimg.jpg")
        img1=img1.resize((1600,900))
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img=Label(self.root,image=self.photoimg1)   
        bg_img.place(x=0,y=0,width=1600,height=900)

        #button 1
        img2=Image.open(r"images\heading.jpg")
        img2=img2.resize((619,177))
        self.photoimg2=ImageTk.PhotoImage(img2)

        b1=Button(bg_img,image=self.photoimg2)
        b1.place(x=491,y=50,width=619,height=177)

        #button 2 student
        img3=Image.open(r"images\stu.jpg")
        img3=img3.resize((190,190))
        self.photoimg3=ImageTk.PhotoImage(img3)

        b2=Button(bg_img,image=self.photoimg3,command=self.student_details,cursor="hand2")
        b2.place(x=100,y=400,width=190,height=190)

        b2_1=Button(bg_img,text="Student details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b2_1.place(x=100,y=590,width=190,height=40)

        #button 3
        
        #button 4 Face recognition
        img4=Image.open(r"images\detect.jpg")
        img4=img4.resize((190,190))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.face_recognition)
        b4.place(x=340,y=400,width=190,height=190)

        b4_1=Button(bg_img,text="Face Recognition",cursor="hand2",command=self.face_recognition,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b4_1.place(x=340,y=590,width=190,height=40)


        #button 5 Train Data
        img5=Image.open(r"images\train.png")
        img5=img5.resize((190,190))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b5=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.train_data)
        b5.place(x=580,y=400,width=190,height=190)

        b5_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b5_1.place(x=580,y=590,width=190,height=40)


        #button 6 Photos
        img6=Image.open(r"images\photos.jpg")
        img6=img6.resize((190,190))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b6=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.open_img)
        b6.place(x=820,y=400,width=190,height=190)

        b6_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b6_1.place(x=820,y=590,width=190,height=40)


        #button 7 Attendance
        img7=Image.open(r"images\attend.jpg")
        img7=img7.resize((190,190))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b7=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance)
        b7.place(x=1060,y=400,width=190,height=190)

        b7_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b7_1.place(x=1060,y=590,width=190,height=40)


        #button 8 Developers
        img8=Image.open(r"images\dev.jpg")
        img8=img8.resize((190,190))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b8=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.developer)
        b8.place(x=1300,y=400,width=190,height=190)

        b8_1=Button(bg_img,text="Developers",cursor="hand2",command=self.developer,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b8_1.place(x=1300,y=590,width=190,height=40)
    
    #========Function buttons==========

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def open_img(self):
        os.startfile("data")

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)

    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=developer(self.new_window)


if __name__=="__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()




