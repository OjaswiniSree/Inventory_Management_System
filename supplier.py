from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class supplierClass:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1300x550+200+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # all variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        
        #--title--
        title=Label(self.root,text="Supplier Details",font=("goudy old style",20,"bold"),bg="#004d99",fg="white")
        title.place(x=50,y=10,width=1200,height=50)


        # Options
        lbl_search=Label(self.root,text="Invoice No.",bg="white",bd=3,font=("goudy old style",15,"bold"))
        lbl_search.place(x=840,y=95)
        

        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow")
        txt_search.place(x=950,y=95,width=150)

        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="green",fg="white",cursor="hand2")
        btn_search.place(x=1125,y=95,width=100,height=28)

        
        # Contaent 
        # ROW 1
        lbl_sup_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=50,y=100)
        txt_sup_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=200,y=100,width=250)
        
         # ROW 2
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=160)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=200,y=160,width=250)
        
        # ROW 3
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=220)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=200,y=220,width=250)
        
        # ROW 4
        lbl_address=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=280)
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=200,y=280,width=550,height=120)
  
        btn_save=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#002db3",fg="white",cursor="hand2").place(x=200,y=450,width=115,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#009933",fg="white",cursor="hand2").place(x=345,y=450,width=115,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#cc0000",fg="white",cursor="hand2").place(x=490,y=450,width=115,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#527a7a",fg="white",cursor="hand2").place(x=635,y=450,width=115,height=28)

        # Supplier Details

        sup_frame=Frame(self.root,bd=3,relief=RIDGE)
        sup_frame.place(x=840,y=170,width=400,height=300)
        
        scrolly=Scrollbar(sup_frame,orient=VERTICAL)
        scrollx=Scrollbar(sup_frame,orient=HORIZONTAL)

        self.SupplierTable=ttk.Treeview(sup_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("invoice",text="INVOICE NO.")
        self.SupplierTable.heading("name",text="NAME")
        self.SupplierTable.heading("contact",text="CONTACT")
        self.SupplierTable.heading("desc",text="DESCRIPTION")

        self.SupplierTable["show"]="headings"
       
        self.SupplierTable.column("invoice",width=100)
        self.SupplierTable.column("name",width=100)
        self.SupplierTable.column("contact",width=100)
        self.SupplierTable.column("desc",width=100)


        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
    # sqlite
    def add(self):
        conn = sqlite3.connect(database='ims.db')
        cur = conn.cursor()
        try: 
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                rows = cur.fetchone()
                if rows is not None:  # Change the condition to check if row is not None
                    messagebox.showerror("Error", "Invoice No. already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO Supplier(invoice, name,  contact, desc) VALUES (?, ?, ?, ?)",
                                (self.var_sup_invoice.get(), self.var_name.get(), self.var_contact.get(),
                                self.txt_desc.get('1.0', END)))
                    conn.commit()
                    messagebox.showinfo("Success", " Supplier Added Successfully", parent=self.root)  # Fix the typo here
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    def update(self):
        conn = sqlite3.connect(database='ims.db')
        cur = conn.cursor()
        try: 
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is None:  
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    cur.execute("Update Supplier set name=?, contact=?, desc=? where invoice=?",
                                (self.var_name.get(), self.var_contact.get(),
                                self.txt_desc.get('1.0', END),
                                self.var_sup_invoice.get()))
                    conn.commit()
                    messagebox.showinfo("Success", "Supplier Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    
    def show(self):
        conn=sqlite3.connect(database='ims.db')
        cur=conn.cursor()
        try:
            cur.execute("select *from Supplier")
            rows=cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        #print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0', END)
        self.txt_desc.insert(END,row[3])
        
    def delete(self):
        conn=sqlite3.connect(database='ims.db')
        cur=conn.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No.must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Employee WHERE eid=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is None:  
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Are you sure you want to delete this record?")
                    if op==True:
                        cur.execute("delete from Supplier where invoice=?",(self.var_sup_invoice.get(),))
                        conn.commit()
                        messagebox.showinfo("Delete", "Supplier Details Deleted Successfully", parent=self.root)  
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END)
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        conn=sqlite3.connect(database='ims.db')
        cur=conn.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice No. should be required",parent=self.root)
            else:
                cur.execute("select *from Supplier where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!",parent=self.root)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

if __name__=="__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()