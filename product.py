from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class productClass:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1300x600+200+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()

        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()


        product_frame=Frame(self.root,bd=2,relief=RIDGE)
        product_frame.place(x=20,y=30,width=570,height=550)

        title=Label(product_frame,text="Manage Product Details",font=("goudy old style",20,"bold"),bg="#002b80",fg="white")
        title.pack(side=TOP,fill=X)
        
        # colums
        lbl_cat=Label(product_frame,text="Category",font=("goudy old style",20,"bold")).place(x=30,y=60)
        cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",17))
        cmb_cat.place(x=200,y=60,width=250)
        cmb_cat.current(0)

        lbl_sup=Label(product_frame,text="Supplier",font=("goudy old style",20,"bold")).place(x=30,y=120)
        cmb_sup=ttk.Combobox(product_frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",17))
        cmb_sup.place(x=200,y=120,width=250)
        
        cmb_sup.current(0)

        lbl_name=Label(product_frame,text="Name",font=("goudy old style",20,"bold")).place(x=30,y=180)
        txt_name=Entry(product_frame,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow")
        txt_name.place(x=200,y=180,width=250,height=35)
    

        lbl_price=Label(product_frame,text="Price",font=("goudy old style",20,"bold")).place(x=30,y=240)
        txt_price=Entry(product_frame,textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow")
        txt_price.place(x=200,y=240,width=250,height=35)

        lbl_quantity=Label(product_frame,text="Quantity",font=("goudy old style",20,"bold")).place(x=30,y=300)
        txt_quantity=Entry(product_frame,textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow")
        txt_quantity.place(x=200,y=300,width=250,height=35)

        lbl_status=Label(product_frame,text="Status",font=("goudy old style",20,"bold")).place(x=30,y=360)
        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",17))
        cmb_status.place(x=200,y=360,width=250)
        cmb_status.current(0)

        btn_save=Button(product_frame,text="Save",command=self.add,font=("goudy old style",15),bg="#002db3",fg="white",cursor="hand2").place(x=40,y=450,width=100,height=28)
        btn_update=Button(product_frame,text="Update",command=self.update,font=("goudy old style",15),bg="#009933",fg="white",cursor="hand2").place(x=160,y=450,width=100,height=28)
        btn_delete=Button(product_frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="#cc0000",fg="white",cursor="hand2").place(x=290,y=450,width=100,height=28)
        btn_clear=Button(product_frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="#527a7a",fg="white",cursor="hand2").place(x=410,y=450,width=100,height=28)

        # Search Frame
        searchframe=LabelFrame(self.root,text="Search Products",bg="white",bd=3,relief=RIDGE,font=("goudy old style",15,"bold"))
        searchframe.place(x=625,y=50,width=590,height=70)
        
        # Options
        cmb_search=ttk.Combobox(searchframe,textvariable=self.var_searchby,values=("Select","Category","Name","Supplier"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=15,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(searchframe,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow")
        txt_search.place(x=205,y=10)

        btn_search=Button(searchframe,text="Search",command=self.search,font=("goudy old style",15),bg="green",fg="white")
        btn_search.place(x=420,y=9,width=150,height=28)

         # Product Details

        pro_frame=Frame(self.root,bd=3,relief=RIDGE)
        pro_frame.place(x=625,y=150,width=610,height=425)
        
        scrolly=Scrollbar(pro_frame,orient=VERTICAL)
        scrollx=Scrollbar(pro_frame,orient=HORIZONTAL)

        self.ProductTable=ttk.Treeview(pro_frame,columns=("pid","category","supplier","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)

        self.ProductTable.heading("pid",text="PRO ID")
        self.ProductTable.heading("category",text="CATEGORY")
        self.ProductTable.heading("supplier",text="SUPPLIER")
        self.ProductTable.heading("name",text="NAME")
        self.ProductTable.heading("price",text="PRICE")
        self.ProductTable.heading("qty",text="QUANTITY")
        self.ProductTable.heading("status",text="STATUS")
       
        self.ProductTable["show"]="headings"
       
        self.ProductTable.column("pid",width=100)
        self.ProductTable.column("category",width=100)
        self.ProductTable.column("supplier",width=100)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("qty",width=100)
        self.ProductTable.column("status",width=100)

        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        self.fetch_cat_sup()

    
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        conn = sqlite3.connect(database='ims.db')
        cur = conn.cursor()
        try:
            cur.execute("SELECT name FROM Category")
            cat=cur.fetchall()
            if len(cat)>0:
               del self.cat_list[:]
               self.cat_list.append("Select")
               for i in cat:
                    self.cat_list.append(i[0])
            cur.execute("SELECT name FROM Supplier")
            sup=cur.fetchall()
            if len(sup)>0:
               del self.sup_list[:]
               self.sup_list.append("Select")
               for i in sup:
                    self.sup_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    def add(self):
        conn = sqlite3.connect(database='ims.db')
        cur = conn.cursor()
        try: 
            if self.var_cat.get() == "Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_name.get()=="":
                messagebox.showerror("Error", "All fields must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Product WHERE name=?", (self.var_name.get(),))
                rows = cur.fetchone()
                if rows is not None:  # Change the condition to check if row is not None
                    messagebox.showerror("Error", "Product already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO Product(category,supplier,name, price, qty,status) VALUES (?, ?, ?, ?, ?, ?)",
                                (self.var_cat.get(), self.var_sup.get(), self.var_name.get(), self.var_price.get(), self.var_qty.get(),self.var_status.get()))
                    conn.commit()
                    messagebox.showinfo("Success", "Product Details Added Successfully", parent=self.root)  # Fix the typo here
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    def update(self):
        conn = sqlite3.connect(database='ims.db')
        cur = conn.cursor()
        try: 
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Product must be selected", parent=self.root)
            else:
                cur.execute("SELECT * FROM Product WHERE pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row is None:  
                    messagebox.showerror("Error", "Invalid Product", parent=self.root)
                else:
                    cur.execute("Update Product set category=?,supplier=?,name=?,price=?,qty=?,status=? where pid=?",
                                (self.var_cat.get(), self.var_sup.get(), self.var_name.get(), self.var_price.get(),
                                self.var_qty.get(), self.var_status.get(),self.var_pid.get()))
                    conn.commit()
                    messagebox.showinfo("Success", "Product Details Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    
    def show(self):
        conn=sqlite3.connect(database='ims.db')
        cur=conn.cursor()
        try:
            cur.execute("select *from Product")
            rows=cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('',END,values=row)
        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def get_data(self,ev):
        f=self.ProductTable.focus()
        content=(self.ProductTable.item(f))
        row=content['values']
        #print(row)
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])
       
    
    def delete(self):
        conn=sqlite3.connect(database='ims.db')
        cur=conn.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror("Error", "Product  must be selected", parent=self.root)
            else:
                cur.execute("SELECT * FROM Product WHERE pid=?", (self.var_pid.get(),))
                row = cur.fetchone()
                if row is None:  
                    messagebox.showerror("Error", "Invalid Product", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Are you sure you want to delete this record?")
                    if op==True:
                        cur.execute("delete from Product where pid=?",(self.var_pid.get(),))
                        conn.commit()
                        messagebox.showinfo("Delete", "Product Details Deleted Successfully", parent=self.root)  
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear(self):
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_pid.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
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
                cur.execute("select *from Product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for row in rows:
                        self.ProductTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!",parent=self.root)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

if __name__=="__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()