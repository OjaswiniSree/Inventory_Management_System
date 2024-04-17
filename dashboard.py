from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
import subprocess
import sqlite3
import os
import time

class IMS:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1520x780+0+0")
        self.root.title("Inventory Management System")
        self.icon_title = PhotoImage(file="Images/icon.png")
        self.root.config(bg="white")
        
        # Title
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT, font=("times new roman", 30, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)
        
        # Logout Button
        btn_logout = Button(self.root,command=self.logout, text="Logout", font=("times new roman", 15, "bold"), bg="orange", cursor="hand2")
        btn_logout.place(x=1300, y=10, height=50, width=150)
        
        # Clock
        self.ibl_clock = Label(self.root, text="Welcome to the System\t\t Date: DD-MM-YYYY", font=("times new roman", 15), bg="#334d4d", fg="white")
        self.ibl_clock.place(x=0, y=70, relwidth=1, height=30)
        
        # Menu
        self.menulogo = Image.open("Images/menu.png")
        self.menulogo = self.menulogo.resize((200, 200))
        self.menulogo=ImageTk.PhotoImage(self.menulogo)
        menu = Frame(self.root, bd=2, relief=RIDGE,bg="white")
        menu.place(x=0, y=102, width=200, height=580)

        lbl_menulogo=Label(menu,image=self.menulogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="Images/arrow.png")
        btn_menu= Button(menu,text="Menu", font=("times new roman",20,"bold"), bg="#006699").pack(side=TOP,fill=X)
        btn_employee= Button(menu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman",20,"bold"), bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_suplier= Button(menu,text="Suplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman",20,"bold"), bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category= Button(menu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman",20,"bold"), bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_products= Button(menu,text="Products",command=self.product,image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman",20,"bold"), bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales= Button(menu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman",20,"bold"), bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit= Button(menu,text="Exit",image=self.icon_side,compound=LEFT,padx=10,anchor="w",font=("times new roman",20,"bold"), bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        # content
        self.lbl_employee=Label(self.root,text="Employes\n[ 0 ]",bg="#bb33ff",fg="white",bd=5,relief=RIDGE,cursor="hand2",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=125,width=300,height=120)
        self.lbl_supliers=Label(self.root,text="Suppliers\n[ 0 ]",bg="#ffb366",fg="white",bd=5,relief=RIDGE,cursor="hand2",font=("goudy old style",20,"bold"))
        self.lbl_supliers.place(x=700,y=125,width=300,height=120)
        self.lbl_category=Label(self.root,text="Categories\n[ 0 ]",bg="#e60073",fg="white",bd=5,relief=RIDGE,cursor="hand2",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1100,y=125,width=300,height=120)
        self.lbl_products = Label(self.root, text="Products\n[ 0 ]", bg="#39e600", fg="white", bd=5, relief=RIDGE, cursor="hand2", font=("goudy old style", 20, "bold"))
        self.lbl_products.place(x=500, y=300, width=300, height=120)
        self.lbl_sales=Label(self.root,text="Sales\n[ 0 ]",bg="#0073e6",fg="white",bd=5,relief=RIDGE,cursor="hand2",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=900,y=300,width=300,height=120)

        # Footer
        ibl_footer= Label(self.root, text="IMS Inventory Management System\nContact: 799xxxx741", font=("times new roman", 15), bg="#334d4d", fg="white").pack(side=BOTTOM,fill=X)
        self.update_content()
       
       
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
  
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
    
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def update_content(self):
        conn=sqlite3.connect(database='ims.db')
        cur=conn.cursor()
        try:
            cur.execute("select *from Product")
            product=cur.fetchall()
            self.lbl_products.config(text=f'Products\n[ {str(len(product))}]')
            
            cur.execute("select *from Supplier")
            supplier=cur.fetchall()
            self.lbl_supliers.config(text=f'Suppliers\n[ {str(len(supplier))}]')

            cur.execute("select *from Category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Categories\n[ {str(len(category))}]')

            cur.execute("select *from Employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Employees\n[ {str(len(employee))}]')
            bill=str(len(os.listdir('Bill')))
            self.lbl_sales.config(text=f'Sales [{str(bill)}]')
            
            date_=time.strftime("%d-%m-%Y")

            self.ibl_clock.config(text=f"Welcome to the System\t\t Date: {str(date_)}")
            self.ibl_clock.after(200,self.update_content)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    

    def logout(self):
        self.root.destroy()
        subprocess.Popen(["python", "login.py"])
        
        

if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
