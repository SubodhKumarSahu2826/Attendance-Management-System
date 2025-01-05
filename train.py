from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np
import mysql.connector



class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Attendance Management System")
        self.root.config(bg="white")
        self.root.wm_iconbitmap("face.ico")

        title_lbl=Label(self.root,text="Train Data Set",cursor="hand2",font=("times new roman",30,"bold"),bg="White",fg="Red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Button
        b2_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="Blue",fg="white")
        b2_1.place(x=0,y=380,width=1580,height=60)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #=============Train the Classifier =============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Done","Training data sets completed!")
        




        

if __name__=="__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()