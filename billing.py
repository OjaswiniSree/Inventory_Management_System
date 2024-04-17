from tkinter import *
from PIL import Image, ImageTk
import subprocess
from tkinter import ttk,messagebox
import sqlite3
import time
import tempfile
import os

class billingClass:
    def __init__(self, root):
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Inventory Management System")
        self.icon_title = PhotoImage(file="Images/icon.png")
        self.root.config(bg="white")
        
        self.cart_list=[]
        self.chk_print=0

        # Title
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT, font=("times new roman", 30, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)
        
        # Logout Button
        btn_logout = Button(self.root,command=self.logout, text="Logout", font=("times new roman", 15, "bold"), bg="orange", cursor="hand2")
        btn_logout.place(x=1300, y=10, height=50, width=150)
        
        # Clock
        self.ibl_clock = Label(self.root, text="Welcome to the System\t\t Date: DD-MM-YYYY", font=("times new roman", 15), bg="#334d4d", fg="white")
        self.ibl_clock.place(x=0, y=70, relwidth=1, height=30)
        
        # product frame
        product_frame=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        product_frame.place(x=6,y=110,width=450,height=590)

        ptitle=Label(product_frame,text="All Products",font=("goudy old style",25,"bold"),bg="#1f1f2e",fg="white").pack(sid=TOP,fill=X)
        # Product search frame
        self.var_search=StringVar()
        product_frame1=Frame(product_frame,bd=2,relief=RIDGE,bg="white")
        product_frame1.place(x=2,y=48,width=441,height=110)

        lbl_search=Label(product_frame1,text="Search By Product | By Name",font=("times new roman",16,"bold"),bg="white",fg="green").place(x=2,y=8)
        btn_show_all = Button(product_frame1,command=self.show, text="Show All", font=("times new roman", 17, "bold"), bg="#083531",fg="white", cursor="hand2")
        btn_show_all.place(x=310, y=8, height=30, width=120)

        lbl_name=Label(product_frame1,text="Product Name",font=("times new roman",16,"bold"),bg="white").place(x=2,y=58)
        txt_name_search=Entry(product_frame1,textvariable=self.var_search,font=("times new roman",17,"bold"),bg="lightyellow").place(x=135,y=58,width=170,height=28)

        btn_search = Button(product_frame1,command=self.search, text="Search", font=("times new roman", 17, "bold"), bg="#2196f3",fg="white", cursor="hand2")
        btn_search.place(x=310, y=58, height=28, width=120)
   
        # product details frame     
        product_frame2=Frame(product_frame,bd=3,relief=RIDGE)
        product_frame2.place(x=2,y=170,width=441,height=370)
        
        scrolly=Scrollbar(product_frame2,orient=VERTICAL)
        scrollx=Scrollbar(product_frame2,orient=HORIZONTAL)

        self.productTable=ttk.Treeview(product_frame2,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)

        self.productTable.heading("pid",text="PID")
        self.productTable.heading("name",text="NAME")
        self.productTable.heading("price",text="PRICE")
        self.productTable.heading("qty",text="QTY")
        self.productTable.heading("status",text="STATUS")

        self.productTable["show"]="headings"
       
        self.productTable.column("pid",width=40)
        self.productTable.column("name",width=100)
        self.productTable.column("price",width=100)
        self.productTable.column("qty",width=40)
        self.productTable.column("status",width=90)


        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        
        #self.show() 
        lbl_note=Label(product_frame,text="Note: 'Enter 0 Quantity to remove product from the Cart'",font=("goudy old style",14),bg="white",fg="red",anchor="w").pack(side=BOTTOM,fill=X)

        #customerFrame
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        
        customer_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        customer_frame.place(x=460,y=110,width=600,height=110)

        cTitle=Label(customer_frame,text="Customer Details",font=("goudy old style",20,"bold"),bg="lightgray").pack(side=TOP,fill=X)
        lbl_cname=Label(customer_frame,text="Name",font=("times new roman",16),bg="white").place(x=5,y=55)
        txt_csearch=Entry(customer_frame,textvariable=self.var_cname,font=("times new roman",17,"bold"),bg="lightyellow").place(x=80,y=55,width=190,height=28)
        lbl_cusname=Label(customer_frame,text="Contact No.",font=("times new roman",16),bg="white").place(x=280,y=55)
        txt_cussearch=Entry(customer_frame,textvariable=self.var_contact,font=("times new roman",17,"bold"),bg="lightyellow").place(x=400,y=55,width=170,height=28)
        
        # cal cart frame
        cal_car_frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        cal_car_frame.place(x=460,y=225,width=600,height=360)
        
        # caluclator frame
        self.var_cal_input = StringVar()

        cal_frame = Frame(cal_car_frame, bd=4, relief=RIDGE, bg="white")
        cal_frame.place(x=5, y=7, width=284, height=342)

        txt_cal_input = Entry(cal_frame, textvariable=self.var_cal_input, font=("arial", 15, "bold"), width=23, bd=10, relief=GROOVE, state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0, column=0, columnspan=4, padx=2, pady=2)

        button7 = Button(cal_frame, text='7', font=("arial", 15, "bold"),command=lambda:self.get_input(7), bd=5, width=3, padx=10,pady=10,cursor="hand2")
        button7.grid(row=1, column=0)
        button8 = Button(cal_frame, text='8', font=("arial", 15, "bold"),command=lambda:self.get_input(6), bd=5, width=3, padx=10,pady=10,cursor="hand2")
        button8.grid(row=1, column=1)        
        button9 = Button(cal_frame, text='9', font=("arial", 15, "bold"),command=lambda:self.get_input(8), bd=5, width=3, padx=10,pady=10,cursor="hand2")
        button9.grid(row=1, column=2)
        btn_sum = Button(cal_frame, text='+', font=("arial", 15, "bold"),command=lambda:self.get_input('+'), bd=5, width=3, padx=10,pady=10,cursor="hand2")
        btn_sum.grid(row=1, column=3)

        button4 = Button(cal_frame, text='4', font=("arial", 15, "bold"),command=lambda:self.get_input(4), bd=5, width=3, padx=10,pady=10,cursor="hand2")
        button4.grid(row=2, column=0)
        button5 = Button(cal_frame, text='5', font=("arial", 15, "bold"),command=lambda:self.get_input(5), bd=5, width=3, padx=10,pady=10,cursor="hand2")
        button5.grid(row=2, column=1)        
        button6 = Button(cal_frame, text='6', font=("arial", 15, "bold"),command=lambda:self.get_input(6), bd=5, width=3, padx=10,pady=10,cursor="hand2")
        button6.grid(row=2, column=2)
        btn_minus = Button(cal_frame, text='-', font=("arial", 15, "bold"),command=lambda:self.get_input('-'), bd=5, width=3, padx=10,pady=10,cursor="hand2")
        btn_minus.grid(row=2, column=3)

        button1 = Button(cal_frame, text='1', font=("arial", 15, "bold"),command=lambda:self.get_input(1), bd=5, width=3, padx=10,pady=10,cursor="hand2")
        button1.grid(row=3, column=0)
        button2 = Button(cal_frame, text='2', font=("arial", 15, "bold"),command=lambda:self.get_input(2), bd=5, width=3, padx=10,pady=10,cursor="hand2")
        button2.grid(row=3, column=1)        
        button3 = Button(cal_frame, text='3', font=("arial", 15, "bold"),command=lambda:self.get_input(3), bd=5, width=3, padx=10,pady=10,cursor="hand2")
        button3.grid(row=3, column=2)
        btn_mul = Button(cal_frame, text='*', font=("arial", 15, "bold"),command=lambda:self.get_input('*'), bd=5, width=3, padx=10,pady=10,cursor="hand2")
        btn_mul.grid(row=3, column=3)

        button0 = Button(cal_frame, text='0', font=("arial", 15, "bold"),command=lambda:self.get_input(0), bd=5, width=3, padx=10,pady=17,cursor="hand2")
        button0.grid(row=4, column=0)
        btn_clear = Button(cal_frame, text='C', font=("arial", 15, "bold"),command=self.clear_cal, bd=5, width=3, padx=10,pady=17,cursor="hand2")
        btn_clear.grid(row=4, column=1)        
        btn_equ= Button(cal_frame, text='=', font=("arial", 15, "bold"),command=self.perform_cal, bd=5, width=3, padx=10,pady=17,cursor="hand2")
        btn_equ.grid(row=4, column=2)
        btn_divi = Button(cal_frame, text='/', font=("arial", 15, "bold"),command=lambda:self.get_input('/'), bd=5, width=3, padx=10,pady=17,cursor="hand2")
        btn_divi.grid(row=4, column=3)


       
        #Cart Frame
        cart_frame=Frame(cal_car_frame,bd=3,relief=RIDGE)
        cart_frame.place(x=295,y=7,width=295,height=342)
        self.cartTitle=Label(cart_frame,text="Cart \t Total Product: [0]",font=("goudy old style",15,"bold"),bg="lightgray")
        self.cartTitle.pack(side=TOP,fill=X)


        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.cartTable=ttk.Treeview(cart_frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cartTable.xview)
        scrolly.config(command=self.cartTable.yview)

        self.cartTable.heading("pid",text="PID")
        self.cartTable.heading("name",text="NAME")
        self.cartTable.heading("price",text="PRICE")
        self.cartTable.heading("qty",text="QTY")

        self.cartTable["show"]="headings"
       
        self.cartTable.column("pid",width=40)
        self.cartTable.column("name",width=90)
        self.cartTable.column("price",width=90)
        self.cartTable.column("qty",width=60)

        self.cartTable.pack(fill=BOTH,expand=1)
        self.cartTable.bind("<ButtonRelease-1>",self.get_data_cart)


        # Add cart widget frame
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        self.var_instock=StringVar()

        widget_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        widget_frame.place(x=460,y=590,width=600,height=110)

        p_name=Label(widget_frame,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=10,y=8)
        txt_pname=Entry(widget_frame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=10,y=38,width=200,height=22)

        lbl_price=Label(widget_frame,text="Price per Qty",font=("times new roman",15,"bold"),bg="white").place(x=240,y=8)
        txt_price=Entry(widget_frame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=240,y=38,width=180,height=22)

        lbl_quantity=Label(widget_frame,text="Quantity",font=("times new roman",15,"bold"),bg="white").place(x=440,y=8)
        txt_quantity=Entry(widget_frame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=440,y=38,width=145,height=22)

        self.stock_name=Label(widget_frame,text="In Stock",font=("times new roman",15,"bold"),bg="white")
        self.stock_name.place(x=10,y=70)

        btn_clear_cart=Button(widget_frame,text="Clear",font=("times new roman",15,"bold"),command=self.clear_cart,bg="lightgray",cursor="hand2").place(x=200,y=70,width=150,height=30)
        btn_add_cart=Button(widget_frame,text="Add/Update Cart",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=370,y=70,width=200,height=30)

        # Billing area
        bill_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bill_frame.place(x=1063,y=110,width=460,height=425)

        Btitle=Label(bill_frame,text="Customer Billing Area",font=("goudy old style",25,"bold"),bg="#ff6633",fg="white").pack(sid=TOP,fill=X)
        scrolly=Scrollbar(bill_frame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.txt_bill_area=Text(bill_frame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        # Billing Buttons
        bill_menu_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bill_menu_frame.place(x=1063,y=540,width=460,height=160)

        self.lbl_amt=Label(bill_menu_frame,text="Bill Amount\n[0]",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amt.place(x=2,y=5,width=140,height=80)

        self.lbl_discount=Label(bill_menu_frame,text="Discount\n[5%]",font=("goudy old style",15,"bold"),bg="#77b300",fg="white")
        self.lbl_discount.place(x=145,y=5,width=140,height=80)

        self.lbl_net_pay=Label(bill_menu_frame,text="Net Pay\n[0]",font=("goudy old style",15,"bold"),bg="#5c5c8a",fg="white")
        self.lbl_net_pay.place(x=288,y=5,width=170,height=80)


        btn_print=Button(bill_menu_frame,text="Print",command=self.print_bill,cursor="hand2",font=("goudy old style",15,"bold"),bg="lightgreen",fg="white",bd=3,relief=RIDGE)
        btn_print.place(x=2,y=90,width=140,height=60)

        btn_clear_all=Button(bill_menu_frame,text="Clear",command=self.clear_all,cursor="hand2",font=("goudy old style",15,"bold"),bg="gray",fg="white",bd=3,relief=RIDGE)
        btn_clear_all.place(x=145,y=90,width=140,height=60)

        btn_generate=Button(bill_menu_frame,text="Generate/Save Bill",command=self.generate_bill,cursor="hand2",font=("goudy old style",15,"bold"),bg="#009688",fg="white",bd=3,relief=RIDGE)
        btn_generate.place(x=288,y=90,width=170,height=60)
        # Footer
        ibl_footer= Label(self.root, text="IMS Inventory Management System\nContact: 799xxxx741", font=("times new roman", 15), bg="#334d4d", fg="white").pack(side=BOTTOM,fill=X)

        self.show()
        self.update_date()
        
        
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        conn = sqlite3.connect(database='ims.db')
        cur = conn.cursor()
        try:
            cur.execute("SELECT pid, name, price, qty, status FROM Product WHERE status='Active'")
            rows = cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def search(self):
        conn = sqlite3.connect(database='ims.db')
        cur = conn.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                cur.execute("SELECT pid, name, price, qty, status FROM Product WHERE name LIKE ? AND status='Active'", ('%' + self.var_search.get() + '%',))
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    def get_data(self,ev):
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        #print(row)
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.stock_name.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')
    
    def get_data_cart(self,ev):
        f=self.cartTable.focus()
        content=(self.cartTable.item(f))
        row=content['values']
        #print(row)
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.stock_name.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
        self.var_qty.set(row[3])


    def add_update_cart(self):
        if self.var_pid.get=='':
            messagebox.showerror("Error","Select Product from the List",parent=self.root)
        elif self.var_qty.get()=='':
            messagebox.showerror("Error","Quantity is Required",parent=self.root)
        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror("Error","Invalid Quantity",parent=self.root)
        else:
            #price_cal=int(self.var_qty.get())*float(self.var_price.get())
            #price_cal=float(price_cal)
            price_cal=self.var_price.get()
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
        
        # Update cart
            present='no'
            index_=-1
            for row in  self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_+=1
            if present=='yes':
                op=messagebox.askyesno('confirm',"Product already exists\nDo you want to update| Remove the product")
                if op==True:
                    if self.var_qty.get()=='0':
                        self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2]=price_cal
                        self.cart_list[index_][3]=self.var_qty.get()

            else:
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_update()

    def bill_update(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amnt=self.bill_amnt+(float(row[2]))*int(row[3])

        self.discount=(self.bill_amnt*5)/100
        self.net_pay=self.bill_amnt-self.discount
        self.lbl_amt.config(text=f'Bill Amount\n{str(self.bill_amnt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
        self.cartTitle.config(text=f'Cart \t Total Product: [{str(len(self.cart_list))}]')


    def show_cart(self):

        try:
            self.cartTable.delete(*self.cartTable.get_children())
            for row in self.cart_list:
                self.cartTable.insert('',END,values=row)
        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error",f"Customer Details are required",parent=self.root)
        elif len(self.cart_list)==0:
           messagebox.showerror("Error",f"Please Add Products to the cart!!",parent=self.root)
        else:
            # Bill Top
            # Bill Middle
            # Bill Bottom
            self.bill_top()
            self.middle_cart()
            self.bill_bottom()

            fp=open(f'Bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo('Saved',"Bill has been generated",parent=self.root)
            self.chk_print=1

    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\t\tXYZ-Inventory
\t Phone No. 98725***** , Delhi-125001
 {str("="*52)}
 Customer Name: {self.var_cname.get()}
 Ph no. {str(self.var_contact.get())}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
 {str("="*52)}
 Product Name\t\t\tQTY\tPrice
 {str("="*52)}
'''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp=f'''
 {str("="*52)}
 Bill Amount\t\t\t\tRs.{self.bill_amnt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
 {str("="*52)}
'''
        self.txt_bill_area.insert(END,bill_bottom_temp)

    def middle_cart(self):
        conn = sqlite3.connect(database='ims.db')
        cur = conn.cursor()
        try:
            for row in self.cart_list:
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status='Inactive'
                if int(row[3])!=int(row[4]):
                    status='Active'
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tRs."+price)

                cur.execute('Update product set qty=?,status=? where pid=?',(
                   qty,status,pid 
                ))
                self.stock_name.config(text=f"In Stock [{str(qty)}]")

                conn.commit()
            conn.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.stock_name.config(text=f"In Stock")
        self.var_stock.set('')
        self.var_qty.set('')
   
    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.cartTitle.config(text=f"Cart \t Total Product: [0]")
        self.var_search()
        self.clear_cart()
        self.show()
        self.show_cart()

    def update_date(self):
        
        date_=time.strftime("%d-%m-%Y")

        self.ibl_clock.config(text=f"Welcome to the System\t\t Date: {str(date_)}")
        self.ibl_clock.after(200,self.update_date)

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("Print","Please wait while printing",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')

        else:
            messagebox.showerror("Print","Please generate bill to print the receipt",parent=self.root)

        
    def logout(self):
        self.root.destroy()
        subprocess.Popen(["python", "login.py"])


if __name__=="__main__":
    root = Tk()
    obj = billingClass(root)
    root.mainloop()