from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
import os
import csv
from tkinter import filedialog
from datetime import datetime
import mysql.connector
import cv2
import numpy as np

mydata=[]
class attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Attendance")
        self.root.config(bg="white")
        self.root.wm_iconbitmap("face.ico")

        # ========== variables ==============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        title_lbl=Label(self.root,text="Attendance record",font=("times new roman",35),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1600,height=45)

        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1600,height=800)

        #left label
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance",font=("times new roman",20,"bold"))
        left_frame.place(x=10,y=10, width=770,height=750)
        
        img_left=Image.open(r"images\heading.jpg") 
        img_left=img_left.resize((720,130)) 
        self.photoimg_left=ImageTk. PhotoImage(img_left)
        f_lbl=Label(left_frame, image=self.photoimg_left) 
        f_lbl.place(x=5,y=0,width=720,height=230)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white",)
        left_inside_frame.place(x=5,y=255,width=755,height=455)

        #label and entry
        #Attendance ID
        attendance_id_label=Label(left_inside_frame,text=" Attendance ID: ",font=("times new roman",15))
        attendance_id_label.grid(row=0,column=0,padx=10,sticky=W)

        attendance_id_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",12))
        attendance_id_entry.grid(row=0,column=1,pady=10,sticky=W)

        #Student rollno
        roll_label=Label(left_inside_frame,text=" Roll no: ",font=("times new roman",15))
        roll_label.grid(row=0,column=2,padx=10,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,font=("times new roman",12))
        roll_entry.grid(row=0,column=3,pady=10,sticky=W)

        #Name
        Name_label=Label(left_inside_frame,text=" Name: ",font=("times new roman",15))
        Name_label.grid(row=1,column=0,padx=10,sticky=W)
        
        Name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",12))
        Name_entry.grid(row=1,column=1,pady=10,sticky=W)

        #Department
        dep_label=Label(left_inside_frame,text="Department: ",font=("times new roman",15))
        dep_label.grid(row=1,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_dep,font=("times new roman",12),state="readonly",width=20)
        dep_combo['values']=(" Select Department"," Computer"," IT"," Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,pady=10,sticky=W)

        #Date
        date_label=Label(left_inside_frame,text=" Date: ",font=("times new roman",15))
        date_label.grid(row=2,column=0,padx=10,sticky=W)
        
        date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",12))
        date_entry.grid(row=2,column=1,pady=10,sticky=W)

        #Time
        Time_label=Label(left_inside_frame,text=" Time: ",font=("times new roman",15))
        Time_label.grid(row=2,column=2,padx=10,sticky=W)
        
        Time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",12))
        Time_entry.grid(row=2,column=3,pady=10,sticky=W)

        #Attendance
        atten_label=Label(left_inside_frame,text="Attendance: ",font=("times new roman",15))
        atten_label.grid(row=3,column=0,padx=10,sticky=W)

        atten_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",12),state="readonly",width=20)
        atten_combo['values']=(" Status","Present","Absent")
        atten_combo.current(0)
        atten_combo.grid(row=3,column=1,pady=10,sticky=W)

        #button frame
        btn_frame=Frame(left_inside_frame,relief=RIDGE,bd=2)
        btn_frame.place(x=5,y=395,width=735,height=40)

        import_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=26,font=("times new roman",13),bg="blue",fg="white",cursor="hand2")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=26,font=("times new roman",13),bg="blue",fg="white",cursor="hand2")
        export_btn.grid(row=0,column=1)
        
        Reset_btn=Button(btn_frame,text="Reset",width=26,command=self.reset_data,font=("times new roman",13),bg="blue",fg="white",cursor="hand2")
        Reset_btn.grid(row=0,column=2) 



        #right label
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Data",font=("times new roman",20,"bold"))
        Right_frame.place(x=790,y=10,width=760,height=750)
    
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=7,y=10,width=740,height=685)

        # ============== scroll bar table========================    
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id",text="Attendance ID")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("department",text="Department")
        self.student_table.heading("time",text="Time")
        self.student_table.heading("date",text="Date")
        self.student_table.heading("attendance",text="Attendance")
        self.student_table["show"]="headings"

        self.student_table.column("id",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("department",width=100)
        self.student_table.column("time",width=100)
        self.student_table.column("date",width=100)
        self.student_table.column("attendance",width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)


    # ============ fetch data =================
    def fetchData(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("",END,values=i)  

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)        

    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])     

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")           









if __name__ =="__main__":
    root=Tk()
    obj=attendance(root)
    root.mainloop()