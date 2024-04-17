from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class employeeClass:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1300x600+200+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # all variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_emp_id=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_pass=StringVar()
        self.var_usrtyp=StringVar()
        self.var_adress=StringVar()
        self.var_salary=StringVar()

        # Search Frame
        searchframe=LabelFrame(self.root,text="Search Employee",bg="white",bd=3,relief=RIDGE,font=("goudy old style",15,"bold"))
        searchframe.place(x=300,y=20,width=590,height=70)
        
        # Options
        cmb_search=ttk.Combobox(searchframe,textvariable=self.var_searchby,values=("Select","Name","Email","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=15,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(searchframe,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow")
        txt_search.place(x=205,y=10)

        btn_search=Button(searchframe,text="Search",command=self.search,font=("goudy old style",15),bg="green",fg="white")
        btn_search.place(x=420,y=9,width=150,height=28)

        #--title--
        title=Label(self.root,text="Employee Details",font=("goudy old style",15),bg="#004d99",fg="white")
        title.place(x=50,y=100,width=1200)

        # Contaent 
        # ROW 1
        lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=450,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=850,y=150)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=250)
        #txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="lightyellow").place(x=550,y=150,width=200)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=550,y=150,width=250)
        cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=950,y=150,width=250)

        # ROW 2
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=200)
        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=450,y=200)
        lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=850,y=200)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=200,width=250)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=550,y=200,width=250)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=950,y=200,width=250)

        # ROW 3
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=250)
        lbl_pswd=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=450,y=250)
        lbl_usrtyp=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=850,y=250)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=250,width=250)
        txt_pswd=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow").place(x=550,y=250,width=250)
        cmb_usrtyp=ttk.Combobox(self.root,textvariable=self.var_usrtyp,values=("Select","Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_usrtyp.place(x=950,y=250,width=250)
        cmb_usrtyp.current(0)
        #txt_usrtyp=Label(self.root,textvariable=self.var_usrtyp,font=("goudy old style",15),bg="lightyellow").place(x=950,y=250,width=250)
 
        # ROW 4
        lbl_address=Label(self.root,text="Adress",font=("goudy old style",15),bg="white").place(x=50,y=300)
        lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=700,y=300)
        
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=150,y=300,width=450,height=100)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="lightyellow").place(x=800,y=300,width=250)
 
        btn_save=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#002db3",fg="white",cursor="hand2").place(x=700,y=370,width=115,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#009933",fg="white",cursor="hand2").place(x=830,y=370,width=115,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#cc0000",fg="white",cursor="hand2").place(x=960,y=370,width=115,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#527a7a",fg="white",cursor="hand2").place(x=1090,y=370,width=115,height=28)

        # Employee Details

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=425,relwidth=1,height=175)
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","usrtyp","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="NAME")
        self.EmployeeTable.heading("email",text="EMAIL")
        self.EmployeeTable.heading("gender",text="GENDER")
        self.EmployeeTable.heading("contact",text="CONTACT")
        self.EmployeeTable.heading("dob",text="DOB")
        self.EmployeeTable.heading("doj",text="DOJ")
        self.EmployeeTable.heading("pass",text="PWSD")
        self.EmployeeTable.heading("usrtyp",text="USRTYP")
        self.EmployeeTable.heading("address",text="ADDRESS")
        self.EmployeeTable.heading("salary",text="SALARY")
       
        self.EmployeeTable["show"]="headings"
       

        self.EmployeeTable.column("eid",width=100)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("usrtyp",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)

        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
    # sqlite
    def add(self):
        conn = sqlite3.connect(database='ims.db')
        cur = conn.cursor()
        try: 
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Employee WHERE eid=?", (self.var_emp_id.get(),))
                rows = cur.fetchone()
                if rows is not None:  # Change the condition to check if row is not None
                    messagebox.showerror("Error", "This employee ID already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO Employee(eid, name, email, gender, contact, dob, doj, pass, usrtyp, address, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (self.var_emp_id.get(), self.var_name.get(), self.var_email.get(), self.var_gender.get(), self.var_contact.get(),
                                self.var_dob.get(), self.var_doj.get(), self.var_pass.get(), self.var_usrtyp.get(), self.txt_address.get('1.0', END),
                                self.var_salary.get()))
                    conn.commit()
                    messagebox.showinfo("Success", "Employee Details Added Successfully", parent=self.root)  # Fix the typo here
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    def update(self):
        conn = sqlite3.connect(database='ims.db')
        cur = conn.cursor()
        try: 
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is None:  
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    cur.execute("Update Employee set name=?, email=?, gender=?, contact=?, dob=?, doj=?, pass=?, usrtyp=?, address=?, salary=? where eid=?",
                                (self.var_name.get(), self.var_email.get(), self.var_gender.get(), self.var_contact.get(),
                                self.var_dob.get(), self.var_doj.get(), self.var_pass.get(), self.var_usrtyp.get(), self.txt_address.get('1.0', END),
                                self.var_salary.get(),self.var_emp_id.get()))
                    conn.commit()
                    messagebox.showinfo("Success", "Employee Details Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    
    def show(self):
        conn=sqlite3.connect(database='ims.db')
        cur=conn.cursor()
        try:
            cur.execute("select *from Employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)
        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        #print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7]) 
        self.var_usrtyp.set(row[8])
        self.txt_address.delete('1.0', END)
        self.txt_address.insert(END,row[9])
        self.var_salary.set(row[10])
    
    def delete(self):
        conn=sqlite3.connect(database='ims.db')
        cur=conn.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is None:  
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Are you sure you want to delete this record?")
                    if op==True:
                        cur.execute("delete from Employee where eid=?",(self.var_emp_id.get(),))
                        conn.commit()
                        messagebox.showinfo("Delete", "Employee Details Deleted Successfully", parent=self.root)  
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("") 
        self.var_usrtyp.set("Select")
        self.txt_address.delete('1.0', END)
        self.var_salary.set("")
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        conn=sqlite3.connect(database='ims.db')
        cur=conn.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("select *from Employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!",parent=self.root)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

if __name__=="__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()