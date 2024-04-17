from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os

class salesClass:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1300x600+200+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        self.var_invoice=StringVar()
        self.bill_List=[]


        # Title
        title=Label(self.root,text="Customer Billing Reports",font=("goudy old style",35,"bold"),bg="#00004d",fg="white",relief=RIDGE)
        title.place(x=20,y=10,width=1260,height=60)

        lbl_invoice=Label(self.root,text="Invoice No.",bg="white",bd=3,font=("goudy old style",20,"bold"))
        lbl_invoice.place(x=50,y=105)
        

        txt_search=Entry(self.root,textvariable=self.var_invoice,font=("goudy old style",18),bg="lightyellow")
        txt_search.place(x=210,y=105,width=250)

        btn_search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="green",fg="white",cursor="hand2")
        btn_search.place(x=500,y=105,width=150,height=30)

        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),bg="#669999",fg="white",cursor="hand2")
        btn_clear.place(x=675,y=105,width=150,height=30)
        
        # Bill List
        sales_frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=60,y=180,width=280,height=400)

        scrolly=Scrollbar(sales_frame,orient=VERTICAL)
        self.sales_list=Listbox(sales_frame,font=("goudy old style",15),bg="white",yscrollcommand=scrolly)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH,expand=1)
        self.sales_list.bind("<ButtonRelease-1>",self.get_data)

        # Bill Area
        bill_frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=365,y=180,width=460,height=400)

        title2=Label(bill_frame,text="Customer Billing Area",font=("goudy old style",22,"bold"),bg="#339980")
        title2.pack(side=TOP,fill=X)

        scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area=Text(bill_frame,yscrollcommand=scrolly2)
        scrolly2.pack(side=RIGHT,fill=Y)
        scrolly2.config(command=self.sales_list.yview)
        self.bill_area.pack(fill=BOTH,expand=1)

        #Image
        self.img = Image.open("Images/billing.png")
        self.img = self.img.resize((300, 400))
        self.img=ImageTk.PhotoImage(self.img)

        self.lbl_img=Label(self.root,image=self.img,bd=0,relief=RAISED)
        self.lbl_img.place(x=900,y=130)
        
        self.show()

    def show(self):
        self.bill_List[:]
        self.sales_list.delete(0,END)
        for i in os.listdir('Bill'):
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_List.append(i.split('.')[0])
                 
    def get_data(self,ev):
        index_=self.sales_list.curselection()
        file_name=self.sales_list.get(index_)
        print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'Bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice No. should be required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_List:
               fp=open(f'Bill/{self.var_invoice.get()}.txt','r')
               self.bill_area.delete('1.0',END)
               for i in fp:
                   self.bill_area.insert(END,i)
               fp.close()
            else:
                messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)
            

if __name__=="__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()