from tkinter import*
from PIL import ImageTk 
from tkinter import ttk,messagebox
import sqlite3
import subprocess
import os
import time

class login_system:
    def __init__(self,root) -> None:
           self.root=root
           self.root.title("Login System")
           self.root.geometry("1520x780+0+0")
           self.root.config(bg="#fafafa")

           self.otp=''

           self.employee_id=StringVar()
           self.password=StringVar()
           # Images
           self.photo_img=ImageTk.PhotoImage(file="Images/login.png")
           self.lbl_login=Label(self.root,image=self.photo_img,bd=0).place(x=300,y=150)

           self.img1=ImageTk.PhotoImage(file="Images/login1.png")
           self.img2=ImageTk.PhotoImage(file="Images/login2.png")
           self.img3=ImageTk.PhotoImage(file="Images/login3.png")


           self.lbl_change_img=Label(self.root,bg="white")
           self.lbl_change_img.place(x=394,y=222,width=207,height=365)


           login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
           login_frame.place(x=725,y=160,width=370,height=450)

           title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)
           
           lbl_usr=Label(login_frame,text="Employee ID",font=("Andalus",15),fg="#767171",bg="white").place(x=30,y=130)
           txt_usr=Entry(login_frame,textvariable=self.employee_id,font=("time new roman",15),bg="#ECECEC").place(x=150,y=130,width=180)
           
           lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),fg="#767171",bg="white").place(x=30,y=200)
           txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("time new roman",15),bg="#ECECEC").place(x=150,y=200,width=180)

           btn_login=Button(login_frame,command=self.login,text="Login",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#80e5ff",fg="white",activeforeground="black").place(x=60,y=270,width=250,height=40)

           hr=Label(login_frame,bg="lightgray").place(x=60,y=340,width=250,height=2)
           or_=Label(login_frame,text="OR",bg="white",font=("times new roman",15,"bold")).place(x=165,y=325)

           btn_forget=Button(login_frame,command=self.forget,text="Forget Password?",font=("times new roman",13),bg="white",activebackground="white",fg="#00759E",activeforeground="#00769E",bd=0).place(x=100,y=370,width=170)


           self.animate()
           
    def animate(self):
         self.im=self.img1
         self.img1=self.img2
         self.img2=self.img3
         self.img3=self.im
         self.lbl_change_img.config(image=self.im)
         self.lbl_change_img.after(2000,self.animate)
    def login(self):
            con=sqlite3.connect(database='ims.db')
            cur=con.cursor()
            try:
                if self.employee_id.get()=="" or self.password.get()=="":
                    messagebox.showerror("Error","All fields are required",parent=self.root)
                else:
                    cur.execute("select usrtyp from Employee where eid=? and pass=?",(self.employee_id.get(),self.password.get()))
                    user=cur.fetchone()
                    if user==None:
                         messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
                    else:  
                         user_type = user[0]  # Extract user type from the tuple
                         if user_type == "Admin":
                            subprocess.Popen(["python", "dashboard.py"])
                            self.root.destroy()
                         else:
                              self.root.destroy()
                              subprocess.Popen(["python", "billing.py"])

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def forget(self):
        messagebox.showinfo("Informatuon","You need to consult you administrator",parent=self.root)
    

root=Tk()
obj=login_system(root)
root.mainloop()
