from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Attendance Management System")
        self.root.config(bg="white")
        self.root.wm_iconbitmap("face.ico")

        # ===========variables============
        self.var_dep=StringVar() 
        self.var_course=StringVar() 
        self.var_year=StringVar()
        self.var_sem=StringVar() 
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_phone2=StringVar()
        self.var_category=StringVar()


        #Background
        img1=Image.open(r"images\bgimg.jpg")
        img1=img1.resize((1600,900))
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg_img=Label(self.root,image=self.photoimg1)   
        bg_img.place(x=0,y=0,width=1600,height=900)

        title_lbl=Label(bg_img,text="Student's Information",cursor="hand2",font=("times new roman",30,"bold"),bg="White")
        title_lbl.place(x=0,y=0,width=1600,height=55)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=55,width=1600,height=855)

        #left label frame
        Left_label=LabelFrame(main_frame,bd=3,relief=RIDGE,text=" Student Details",font=("times new roman",20,"bold"))
        Left_label.place(x=10,y=45,width=780,height=750)

        img2=Image.open(r"images\heading.jpg")
        img2=img2.resize((770,200))
        self.photoimg2=ImageTk.PhotoImage(img2)

        leftlbl_img=Label(Left_label,image=self.photoimg2)   
        leftlbl_img.place(x=15,y=15,width=745,height=150)

        #current course
        current_course_frame=LabelFrame(main_frame,bd=3,relief=RIDGE,text=" Current Course ",font=("times new roman",20,"bold"))
        current_course_frame.place(x=25,y=260,width=750,height=130)

        #Department
        dep_label=Label(current_course_frame,text="Department: ",font=("times new roman",15))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12),state="readonly",width=20)
        dep_combo['values']=(" Select Department"," Computer"," IT"," Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,pady=10,sticky=W)

        #Course
        cor_label=Label(current_course_frame,text=" Course: ",font=("times new roman",15))
        cor_label.grid(row=0,column=2,padx=10,sticky=W)

        cor_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12),state="readonly",width=20)
        cor_combo['values']=(" Select Course"," FE"," SE"," TE"," BE")
        cor_combo.current(0)
        cor_combo.grid(row=0,column=3,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text=" Year: ",font=("times new roman",15))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12),state="readonly",width=20)
        year_combo['values']=(" Select Year"," 2023-27"," 2022-26"," 2021-25"," 2020-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,pady=10,sticky=W)

        #Semester
        sem_label=Label(current_course_frame,text=" Semester: ",font=("times new roman",15))
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("times new roman",12),state="readonly",width=20)
        sem_combo['values']=(" Select Semester"," Odd"," Even")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,pady=10,sticky=W)

        #class
        class_frame=LabelFrame(main_frame,bd=3,relief=RIDGE,text=" Class ",font=("times new roman",20,"bold"))
        class_frame.place(x=25,y=400,width=750,height=380)

        #Student ID
        id_label=Label(class_frame,text=" Student ID: ",font=("times new roman",15))
        id_label.grid(row=0,column=0,padx=10,sticky=W)

        id_entry=ttk.Entry(class_frame,width=20,textvariable=self.var_std_id,font=("times new roman",12))
        id_entry.grid(row=0,column=1,pady=10,sticky=W)

        #Student Name
        name_label=Label(class_frame,text=" Student's Name: ",font=("times new roman",15))
        name_label.grid(row=0,column=2,padx=10,sticky=W)

        name_entry=ttk.Entry(class_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12))
        name_entry.grid(row=0,column=3,pady=10,sticky=W)

        #Student rollno
        roll_label=Label(class_frame,text=" Roll no: ",font=("times new roman",15))
        roll_label.grid(row=1,column=0,padx=10,sticky=W)

        roll_entry=ttk.Entry(class_frame,textvariable=self.var_roll,width=20,font=("times new roman",12))
        roll_entry.grid(row=1,column=1,pady=10,sticky=W)

        #DOB
        dob_label=Label(class_frame,text=" Date of Birth: ",font=("times new roman",15))
        dob_label.grid(row=1,column=2,padx=10,sticky=W)
        dob_entry=ttk.Entry(class_frame,textvariable=self.var_dob,width=20,font=("times new roman",12))
        dob_entry.grid(row=1,column=3,pady=10,sticky=W)

        #Division
        div_label=Label(class_frame,text=" Division: ",font=("times new roman",15))
        div_label.grid(row=2,column=0,padx=10,sticky=W)

        div_combo=ttk.Combobox(class_frame,textvariable=self.var_div,font=("times new roman",12),state="readonly",width=20)
        div_combo['values']=(" Select Division"," A"," B"," C"," D")
        div_combo.current(0)
        div_combo.grid(row=2,column=1,pady=10,sticky=W)

        #Gender
        gen_label=Label(class_frame,text=" Gender: ",font=("times new roman",15))
        gen_label.grid(row=2,column=2,padx=10,sticky=W)

        gen_combo=ttk.Combobox(class_frame,textvariable=self.var_gender,font=("times new roman",12),state="readonly",width=20)
        gen_combo['values']=(" Select Gender"," Male"," Female"," Trans"," Rather not say")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=3,pady=10,sticky=W)

        #Category
        Category_label=Label(class_frame,text=" Category: ",font=("times new roman",15))
        Category_label.grid(row=3,column=0,padx=10,sticky=W)

        Category_combo=ttk.Combobox(class_frame,textvariable=self.var_category,font=("times new roman",12),state="readonly",width=20)
        Category_combo['values']=(" Select Category"," Open"," OBC"," SC"," ST")
        Category_combo.current(0)
        Category_combo.grid(row=3,column=1,pady=10,sticky=W)

        #email
        mail_label=Label(class_frame,text=" Email ID: ",font=("times new roman",15))
        mail_label.grid(row=3,column=2,padx=10,sticky=W)

        mail_entry=ttk.Entry(class_frame,textvariable=self.var_email,width=20,font=("times new roman",12))
        mail_entry.grid(row=3,column=3,pady=10,sticky=W)

        #phone 
        phn_label=Label(class_frame,text=" Phone no: ",font=("times new roman",15))
        phn_label.grid(row=4,column=0,padx=10,sticky=W)

        phn_entry=ttk.Entry(class_frame,textvariable=self.var_phone,width=20,font=("times new roman",12))
        phn_entry.grid(row=4,column=1,pady=10,sticky=W)

        #phone 2
        phn2_label=Label(class_frame,text=" Alternate Phone no: ",font=("times new roman",15))
        phn2_label.grid(row=4,column=2,padx=10,sticky=W)

        phn2_entry=ttk.Entry(class_frame,textvariable=self.var_phone2,width=20,font=("times new roman",12))
        phn2_entry.grid(row=4,column=3,pady=10,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="Take photo samples",value="Yes")
        radiobutton1.grid(row=5,column=0,padx=10,sticky=W)

        radiobutton2=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="Procede without photo samples",value="No")
        radiobutton2.grid(row=5,column=1,padx=10,sticky=W)

        #button frame
        btn_frame=Frame(class_frame,relief=RIDGE,bd=2)
        btn_frame.place(x=5,y=250,width=735,height=40)

        Save_btn=Button(btn_frame,text="Save",width=19,command=self.add_data,font=("times new roman",13),bg="blue",fg="white",cursor="hand2")
        Save_btn.grid(row=0,column=0)

        Update_btn=Button(btn_frame,text="Update",width=19,command=self.update_data,font=("times new roman",13),bg="blue",fg="white",cursor="hand2")
        Update_btn.grid(row=0,column=1)
        
        Delete_btn=Button(btn_frame,text="Delete",width=19,command=self.delete_data,font=("times new roman",13),bg="blue",fg="white",cursor="hand2")
        Delete_btn.grid(row=0,column=2)

        Reset_btn=Button(btn_frame,text="Reset",width=20,command=self.reset_data,font=("times new roman",13),bg="blue",fg="white",cursor="hand2")
        Reset_btn.grid(row=0,column=3)

        btn_frame2=Frame(class_frame,relief=RIDGE,bd=2)
        btn_frame2.place(x=5,y=290,width=735,height=40)

        Take_Photos_btn=Button(btn_frame2,command=self.generate_dataset,text="Take Photos",width=80,font=("times new roman",13),bg="blue",fg="white",cursor="hand2")
        Take_Photos_btn.grid(row=1,column=0)

        # Update_Photos_btn=Button(btn_frame2,text="Update Photos",width=41,font=("times new roman",13),bg="blue",fg="white",cursor="hand2")
        # Update_Photos_btn.grid(row=1,column=1)

        #right label frame
        Right_frame=LabelFrame(main_frame,bd=3,relief=RIDGE,text=" Student Details",font=("times new roman",20,"bold"))
        Right_frame.place(x=800,y=45,width=770,height=750)

        # img_right=Image.open(r"C:\Users\ahmu7\OneDrive\Desktop\Attendance Management\images\photos.jpg")
        # img_right=img_right.resize((720,130))
        # self.photoimg_right=ImageTk.PhotoImage(img_right)

        # f_lbl=Label(Right_frame,image=self.photoimg_right)
        # f_lbl.place(x=5,y=0,width=720,height=130)

        #=============== Search System ================#

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System and Data Display",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=5,width=710,height=300)

        Search_label=Label(Search_frame,text="Search by",font=("times new roman",15),bg="red",fg="white")
        Search_label.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12),state="readonly",width=20)
        search_combo["values"]=(" Select ","Roll no","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        Search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        Search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",13),bg="blue",fg="white",cursor="hand2")
        Search_btn.grid(row=0,column=3,padx=2)

        ShowAll_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",13),bg="blue",fg="white",cursor="hand2")
        ShowAll_btn.grid(row=0,column=4,padx=2)

        # ======================table frame==============================
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=70,width=710,height=615)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","phone2","category","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No:")
        self.student_table.heading("phone2",text="Alternate No:")
        self.student_table.heading("category",text="Category")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)   
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("phone2",width=100)
        self.student_table.column("category",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #========function declaration=============
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Caputdraconis7",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_sem.get(),
                                                                                                    self.var_std_id.get(),
                                                                                                    self.var_std_name.get(),
                                                                                                    self.var_div.get(),   
                                                                                                    self.var_roll.get(),   
                                                                                                    self.var_gender.get(),   
                                                                                                    self.var_dob.get(),   
                                                                                                    self.var_email.get(),       
                                                                                                    self.var_phone.get(),   
                                                                                                    self.var_phone2.get(),               
                                                                                                    self.var_category.get(),       
                                                                                                    self.var_radio1.get() 


                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #==========fetch data============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Caputdraconis7",database="face_recognizer")
        my_cursor=conn.cursor()              
        my_cursor.execute("select * from student")   
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert ("",END,values=i)
            conn. commit( )
        conn.close()                                                                          

    # ===========get cursor===========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_phone2.set(data[12]),
        self.var_category.set(data[13]),
        self.var_radio1.set(data[14])

    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update?","Do you want to update this student's details?",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Caputdraconis7",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll_No=%s,Gender=%s,Date_of_Birth=%s,Email=%s,Phone_Number=%s,Alternate_Phone_Number=%s,Category=%s,Photo_Sample=%s where Student_ID=%s",(

                                                                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                                                            self.var_phone2.get(),
                                                                                                                                                                                                                                                            self.var_category.get(),
                                                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                                                            self.var_std_id.get()                                                                                      
                                                                                                                                                                                                                                                            ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student's details have been updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
    # delete function    
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID is essential",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Update?","Are you sure you want to delete this student's details?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Caputdraconis7",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student's details have been deleted successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    # reset function
    def reset_data(self):
        self.var_dep.set(" Select Department") 
        self.var_course.set(" Select Course") 
        self.var_year.set(" Select Year")
        self.var_sem.set(" Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set(" Select Division")
        self.var_roll.set("")
        self.var_gender.set(" Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_phone2.set("")
        self.var_category.set(" Select Category")
        self.var_radio1.set("")
    

    #============Generate data set=================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Caputdraconis7",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll_No=%s,Gender=%s,Date_of_Birth=%s,Email=%s,Phone_Number=%s,Alternate_Phone_Number=%s,Category=%s,Photo_Sample=%s where Student_ID=%s",(

                                                                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                                                            self.var_phone2.get(),
                                                                                                                                                                                                                                                            self.var_category.get(),
                                                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                                                            self.var_std_id.get()                                                                                  
                                                                                                                                                                                                                                                                        ))
                self.var_std_id.get()==id+1
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ============== load pre defined data on face frontals from open cv================

                # face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                # def face_cropped(img):
                #     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                #     faces=face_classifier.detectMultiScale(gray,1.3,5)
                #     #scaling factor=1.3
                #     #Minimum Neighbor-5
                #     for (x,y,w,h) in faces:
                #         face_cropped=img[y:y+h,x:x+w]
                #         return face_cropped

                # cap=cv2.VideoCapture(0)
                # img_id=0
                # while True:
                #     ret,my_frame=cap.read()
                #     if face_cropped(my_frame) is not None:
                #         img_id+=1
                #         face=cv2.resize(face_cropped(my_frame),(450,450))
                #         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                #         file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                #         cv2.imwrite(file_name_path,face)
                #         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)                    
                #         cv2.imshow("Cropped Face",face)
                    
                #     if cv2.waitKey(1)==13 or int(img_id)==100:
                #         break
                # cap.release()
                # cv2.destroyAllWindows()   

                video=cv2.VideoCapture(0)
                facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                faces_data=[]
                i=0
                img_id=0
                while True:
                    ret,frame=video.read()
                    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces=facedetect.detectMultiScale(gray, 1.3 ,5)
                    img_id+=1
                    for (x,y,w,h) in faces:
                        crop_img=frame[y:y+h, x:x+w]
                        resized_img=cv2.resize(crop_img, (50,50))
                        # frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                        if len(faces_data)<=100 and i%10==0:
                            faces_data.append(resized_img)
                        i=i+1
                        cv2.putText(frame, str(len(faces_data)), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 1)
                        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,frame)
                    cv2.imshow("Frame",frame)
                    k=cv2.waitKey(1)
                    if k==27 or len(faces_data)==10:
                        break
                video.release()
                cv2.destroyAllWindows()
                # #user_id+=1
                messagebox.showinfo("Done","Data set has been generated",parent=self.root)      
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)










if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()
