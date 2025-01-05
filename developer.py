from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import webbrowser
import cv2
import os
import numpy as np
import mysql.connector



class developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Developer Information")
        self.root.config(bg="white")
        self.root.wm_iconbitmap("face.ico")

        title_lbl=Label(self.root,text="Developer's Information",cursor="hand2",font=("times new roman",30,"bold"),bg="White",fg="BLUE")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #Background
        img1=Image.open(r"images\bgimg.jpg")
        img1=img1.resize((1600,900))
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img=Label(self.root,image=self.photoimg1)   
        bg_img.place(x=0,y=50,width=1600,height=855)

        #button 2 Subodh
        img3=Image.open(r"images\stu.jpg")
        img3=img3.resize((190,190))
        self.photoimg3=ImageTk.PhotoImage(img3)

        b2=Button(bg_img,image=self.photoimg3,cursor="hand2",command=self.open_web1)
        b2.place(x=100,y=200,width=390,height=390)

        b2_1=Button(bg_img,text="Subodh Kumar Sahu\nSE-C-24\nTU3F2223154\nsubodhsahu@ternaengg.ac.in",cursor="hand2",command=self.open_web1,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b2_1.place(x=100,y=590,width=390,height=100)
  
        
        #button 4 Rahul
        img4=Image.open(r"images\stu.jpg")
        img4=img4.resize((190,190))
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.open_web2)
        b4.place(x=600,y=200,width=390,height=390)

        b4_1=Button(bg_img,text="Rahul Rajesh Garud\nSE-C-28\nTU3F2223158\nrahulgarud@ternaengg.ac.in",cursor="hand2",command=self.open_web2,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b4_1.place(x=600,y=590,width=390,height=100)


        #button 5 Waquar
        img5=Image.open(r"images\stu.jpg")
        img5=img5.resize((190,190))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b5=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.open_web3)
        b5.place(x=1100,y=200,width=390,height=390)

        b5_1=Button(bg_img,text="Waquar Najmul Shaikh\nSE-C-35\nTU3F2223165\nwaquarshaikh@ternaengg.ac.in",cursor="hand2",command=self.open_web3,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b5_1.place(x=1100,y=590,width=390,height=100)

    #=============function open==============
    def open_web1(self):
        webbrowser.open("https://www.instagram.com/sks_sahu_19/") 


    def open_web2(self):
        webbrowser.open("https://www.instagram.com/rahul4287452/")

    def open_web3(self):
        webbrowser.open("https://www.instagram.com/shaikh_waqar_05/")










if __name__=="__main__":
    root=Tk()
    obj=developer(root)
    root.mainloop()