from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class categoryClass:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1200x600+200+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        # variables
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        # Title
        title=Label(self.root,text="Manage Product Category",font=("goudy old style",20,"bold"),bg="#204060",fg="white",relief=RIDGE)
        title.place(x=50,y=10,width=1200,height=60)
        
        lbl_name=Label(self.root,text="Enter Category Name",bg="white",bd=3,font=("goudy old style",20,"bold"))
        lbl_name.place(x=80,y=105)

        txt_search=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow")
        txt_search.place(x=380,y=110,width=250)

        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="#2eb82e",fg="white",cursor="hand2").place(x=200,y=190,width=115,height=28)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",15),bg="#cc0000",fg="white",cursor="hand2").place(x=450,y=190,width=115,height=28)
    
        # Category Details

        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=75,y=300,width=550,height=250)
        
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.CategoryTable=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)

        self.CategoryTable.heading("cid",text="CAT ID")
        self.CategoryTable.heading("name",text="NAME")
        
        self.CategoryTable["show"]="headings"
       

        self.CategoryTable.column("cid",width=100)
        self.CategoryTable.column("name",width=100)
        

        self.CategoryTable.pack(fill=BOTH,expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
        # Images
        self.im1 = Image.open("Images/category.png")
        self.im1 = self.im1.resize((400, 200))
        self.im1=ImageTk.PhotoImage(self.im1)

        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=700,y=110)

        self.im2 = Image.open("Images/cat.png")
        self.im2 = self.im2.resize((400, 200))
        self.im2=ImageTk.PhotoImage(self.im2)

        self.lbl_im2=Label(self.root,image=self.im2,relief=RAISED,bd=2)
        self.lbl_im2.place(x=700,y=350)

    def add(self):
        conn = sqlite3.connect(database='ims.db')
        cur = conn.cursor()
        try: 
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Category Name must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM Category WHERE name=?", (self.var_name.get(),))
                rows = cur.fetchone()
                if rows is not None:  # Change the condition to check if row is not None
                    messagebox.showerror("Error", "Category already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO Category(name) VALUES (?)",(self.var_name.get(),))
                    conn.commit()
                    messagebox.showinfo("Success", " Category Added Successfully", parent=self.root)  # Fix the typo here
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


      
    def show(self):
        conn=sqlite3.connect(database='ims.db')
        cur=conn.cursor()
        try:
            cur.execute("select *from Category")
            rows=cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('',END,values=row)
        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self,ev):
        f=self.CategoryTable.focus()
        content=(self.CategoryTable.item(f))
        row=content['values']
        print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])
        
    def delete(self):
        conn = sqlite3.connect(database='ims.db')
        cur = conn.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Error", "Select Category name", parent=self.root)
            else:
                cur.execute("SELECT * FROM Category WHERE cid=?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row is None:  
                    messagebox.showerror("Error", "Try Again.", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Are you sure you want to delete this record?")
                    if op:
                        cur.execute("DELETE FROM Category WHERE cid=?", (self.var_cat_id.get(),))
                        conn.commit()
                        messagebox.showinfo("Delete", "Category Deleted Successfully", parent=self.root)  
                        self.show()
                       # print("Before resetting var_cat_id:", self.var_cat_id.get())  # Debug print
                        self.var_cat_id.set("")  # Reset the category ID after successful deletion
                      #  print("After resetting var_cat_id:", self.var_cat_id.get())  # Debug print
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

            

if __name__=="__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()