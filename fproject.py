import MySQLdb
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk,Image
import datetime
import time
from tkinter import messagebox
import sys
import math

class Admin():
    def __init__(self,win,uid):
        win.configure(background="black")
        p=PhotoImage(file='emiImages//logo7.png')
        win.iconphoto(False,p)
        win.state('zoomed')

        lbl0=Label(win,text="EMI Loan Calculator",font=("Helvetica",60,"bold"))
        lbl0.config(background="gold",foreground="black",anchor="center",width=700)
        lbl0.pack(fill=BOTH,pady=4)
        
        photo=Image.open("emiImages//loan11.png")
        photo=photo.resize((1362,570),Image.ANTIALIAS)
        image0=ImageTk.PhotoImage(photo)
        label0=Label(win,image=image0)
        label0.image=image0
        label0.place(x=0,y=106)

        def menu():
        
        #___________MENUS______________
            chooser=Menu(win,relief=FLAT,bg="deep pink",fg="black",activebackground="black",font=("Verdana",10,"bold"))
            chooser.bg=("purple")
            #chooser.configure(bg="deep pink",fg="black",activebackground="black",activeforeground="deep pink",cursor="right_ptr")
            item1=Menu(chooser,tearoff=0,activebackground="navy",activeforeground="white")
            item1.add_command(label='Add user',command=lambda:addaUser(win))
            item1.add_command(label='Edit user',command=lambda:editUser(win))
            item1.add_command(label='Delete user',command=lambda:deleteUser(win))
            chooser.add_cascade(label='User Manager',menu=item1)

            item2=Menu(chooser,tearoff=0,activebackground="navy",activeforeground="white")
            item2.add_command(label='User Account Detail',command=lambda:userAccDet(win,uid))
            item2.add_command(label='User Personal Detail',command=lambda:userPerDet(win,uid))
            chooser.add_cascade(label="User Profile",menu=item2)

            item3=Menu(chooser,tearoff=0,activebackground="navy",activeforeground="white")
            item3.add_command(label='Client Personal Detail',command=lambda:cPerDet(win))
            item3.add_command(label='Client Professional Detail',command=lambda:cProfDet(win))
            item3.add_command(label='Client Responsibility Detail',command=lambda:cResDet(win))
            chooser.add_cascade(label="Client Manager",menu=item3)

            item4=Menu(chooser,tearoff=0,activebackground="navy",activeforeground="white")
            item4.add_command(label='Loan Plan Detail',command=lambda:lPlanDet(win))
            item4.add_command(label='Loan File Detail',command=lambda:lFileDet(win))
            item4.add_command(label='Loan Issue Detail',command=lambda:lIssueDet(win))
            chooser.add_cascade(label="Loan Manager",menu=item4)

            chooser.add_cascade(label="Reports",command=lambda:report(win))
            chooser.add_cascade(label="Exit",command=lambda:exitin(win))
            win.config(menu=chooser)
        menu()

class Employ(Admin):
    def __init__(self,win,uid):
        super().__init__(win,uid)
        
        #___________MENUS______________
        chooser=Menu()
        item2=Menu(tearoff=0,activebackground="navy",activeforeground="white")
        item2.add_command(label='User Account Detail',command=lambda:userAccDet(win,uid))
        item2.add_command(label='User Personal Detail',command=lambda:userPerDet(win,uid))
        chooser.add_cascade(label="User Profile",menu=item2)

        item3=Menu(tearoff=0,activebackground="navy",activeforeground="white")
        item3.add_command(label='Client Personal Detail',command=lambda:cPerDet(win))
        item3.add_command(label='Client Professional Detail',command=lambda:cProfDet(win))
        item3.add_command(label='Client Responsibility Detail',command=lambda:cResDet(win))
        chooser.add_cascade(label="Client Manager",menu=item3)

        item4=Menu(tearoff=0,activebackground="navy",activeforeground="white")
        item4.add_command(label='Loan Plan Detail',command=lambda:lPlanDet(win))
        item4.add_command(label='Loan File Detail',command=lambda:lFileDet(win))
        item4.add_command(label='Loan Issue Detail',command=lambda:lIssueDet(win))
        chooser.add_cascade(label="Loan Manager",menu=item4)

        chooser.add_cascade(label="Reports",command=lambda:report(win))
        chooser.add_cascade(label="Exit",command=lambda:exitin(win))
        win.config(menu=chooser)

def exitin(win):
    msg=messagebox.askquestion("Exit","Do you really want to exit?")
    if msg=="yes":
        win.destroy()

#------------Adding User---------------  
class addaUser():
    def __init__(self,win):
        top=Toplevel(win)
        top.geometry('1000x560+140+100')
        top.title('AddUser')
        top.configure(background="cyan")
        p=PhotoImage(file='emiImages//ulogo1.png')
        top.iconphoto(False,p)

        frame1=tk.LabelFrame(top,background="cyan")
        frame2=tk.LabelFrame(top,text='User list',background="cyan")
        
        frame1.pack(fill="both",expand="yes",padx=20,pady=10)
        frame2.pack(fill="both",expand="yes",padx=20,pady=10)
        
        self.trv=ttk.Treeview(frame2,columns=(1,2,3,4,5,6,7),show="headings",height="10")
        self.trv.pack()
        
        self.trv.heading(1,text="User_ID")
        self.trv.heading(2,text="Username")
        self.trv.heading(3,text="Password")
        self.trv.heading(4,text="UserType")
        self.trv.heading(5,text="UserStatus")
        self.trv.heading(6,text="SecurityQues")
        self.trv.heading(7,text="SecurityAns")

        c=0
        db=MySQLdb.connect('localhost','root','root','emiloancalculator')
        cursor = db.cursor()
        query= "select * from user"
        cursor.execute(query)
        rows=cursor.fetchall()
        for row in rows:
            c+=1
        self.update(rows)

        tk.Label(frame1,text='Add Record',bg="cyan",fg="black",font=("Verdana",20,"bold")).grid(row=1,column=4 , padx=10, pady=10,columnspan=3)
        tk.Label(frame1,text='            ',bg="cyan",fg="cyan").grid(row=2,column=4 , padx=10, pady=10)
        tk.Label(frame1,text='            ',bg="cyan",fg="cyan").grid(row=2,column=7 , padx=10, pady=10)
        #tk.Label(frame1,text='            ',bg="cyan",fg="cyan").grid(row=2,column=6 , padx=10, pady=10)
        tk.Label(frame1,text='          ',bg="cyan",fg="cyan").grid(row=15,column=1 , padx=10, pady=10)
        img=ImageTk.PhotoImage(Image.open("emiImages//min11.jpg"))
        pic=Label(frame1,image=img).grid(row=2,column=8,rowspan=14,columnspan=2)
        
        tk.Label(frame1,text='User No.',bg="cyan").grid(row=2,column=2 , padx=10, pady=10)
        self.User_ID=Entry(frame1, width=28)
        self.User_ID.insert(0,c+1)
        self.User_ID.config(background="light gray",state=DISABLED)
        self.User_ID.grid(row=2,column=3)
        
        tk.Label(frame1,text='Username *',bg="cyan").grid(row=4,column=2 , padx=10, pady=10)
        self.username=Entry(frame1, width=28)
        self.username.grid(row=4,column=3)
        
        tk.Label(frame1,text='Name',bg="cyan").grid(row=4,column=5 , padx=10, pady=10)
        self.rlname=Entry(frame1, width=28)
        self.rlname.grid(row=4,column=6)

        tk.Label(frame1,text='Password *',bg="cyan").grid(row=6,column=2, padx=10, pady=10)
        self.password=Entry(frame1, width=28)
        self.password.grid(row=6,column=3)
        
        tk.Label(frame1,text='DOB',bg="cyan").grid(row=6,column=5, padx=10, pady=10)
        self.dob=Entry(frame1, width=28)
        self.dob.grid(row=6,column=6)

        tk.Label(frame1,text='User_Type *',bg="cyan").grid(row=8,column=2,padx=10, pady=10)
        self.usertype=Entry(frame1, width=28)
        self.usertype.grid(row=8,column=3)

        tk.Label(frame1,text='Address',bg="cyan").grid(row=8,column=5,padx=10, pady=10)
        self.address=Entry(frame1, width=28)
        self.address.grid(row=8,column=6)
        
        tk.Label(frame1,text='User_Status *',bg="cyan").grid(row=10,column=2, padx=10, pady=10)
        self.userstatus=Entry(frame1, width=28)
        self.userstatus.grid(row=10,column=3)

        tk.Label(frame1,text='Phone',bg="cyan").grid(row=10,column=5, padx=10, pady=10)
        self.phone=Entry(frame1, width=28)
        self.phone.grid(row=10,column=6)

        tk.Label(frame1,text='Security_Question *',bg="cyan").grid(row=12,column=2, padx=10, pady=10)
        self.course=("What is your pet's name?",'What is your favourite color?','What is your First school name?','What is your Hobby?','Which country you were born in?')
        self.securityq=Combobox(frame1,values=self.course,width=25)
        self.securityq.grid(row=12,column=3)

        tk.Label(frame1,text='Mobile',bg="cyan").grid(row=12,column=5, padx=10, pady=10)
        self.mobile=Entry(frame1, width=28)
        self.mobile.grid(row=12,column=6)

        tk.Label(frame1,text='Security_Answer *',bg="cyan").grid(row=14,column=2, padx=10, pady=10)
        self.securitya=Entry(frame1, width=28)
        self.securitya.grid(row=14,column=3)

        tk.Label(frame1,text='E-mail',bg="cyan").grid(row=14,column=5, padx=10, pady=10)
        self.email=Entry(frame1, width=28)
        self.email.grid(row=14,column=6)
        
        ttk.Button(frame1,text='Add Record',command=self.addUser ).grid(row=16,column=4)

        top.mainloop()

    def update(self,rows):
        self.trv.delete(*self.trv.get_children())
        for i in rows:
            self.trv.insert('','end',values=i)

    def clear(self):
        db=MySQLdb.connect('localhost','root','root','emiloancalculator')
        cursor = db.cursor()
        query= "select * from user "
        cursor.execute(query)
        rows=cursor.fetchall()
        self.update(rows)

    def addUser(self):
        #self.uid=self.User_ID.get()
        self.name=self.username.get()
        self.pas=self.password.get()
        self.ut=self.usertype.get()
        self.us=self.userstatus.get()
        self.sq=self.securityq.get()
        self.sa=self.securitya.get()
        self.rname=self.rlname.get()
        self.dobr=self.dob.get()
        self.addr=self.address.get()
        self.pho=self.phone.get()
        self.mob=self.mobile.get()
        self.mail=self.email.get()
        
        
        if(len(self.name) == 0 or len(self.pas) == 0 or len(self.ut) == 0 or len(self.us) == 0 or len(self.sq) == 0 or len(self.sa) == 0):
            messagebox.showerror("Error", "Empty field error!")
            return
        elif (self.ut !='administrator' and self.ut != 'employee'):
            messagebox.showerror("Error", "Invalid UserType!")
            '''elif self.email:
            if('@' not in self.email or '.' not in self.email):
                messagebox.showerror("Error","Enter valid E-mail!")'''
        else:
            try:
                db=MySQLdb.connect("localhost","root","root","emiloancalculator")
                cursor = db.cursor()
                data=cursor.execute("select * from user where Username like %s",(self.name,))
                if data:
                    messagebox.showerror("Error","Username already exists!")
                #sqlquery = "create table User(User_ID int, Name varchar(45),Contact varchar(45),Email varchar(80),Location varchar(45))"
                else:
                    sqlquery1="insert into user(Username,Password,User_Type,User_Status,Security_Question,Security_Answer) values(%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sqlquery1,(self.name,self.pas,self.ut,self.us,self.sq,self.sa))
                    sqlquery2="insert into user_personal(Name,Date_of_birth,Address,Phone,Mobile,Gmail) values(%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sqlquery2,(self.rname,self.dobr,self.addr,self.pho,self.mob,self.mail))
                    db.commit()
                    messagebox.showinfo("Success","User added successfully!")
                    rows=cursor.fetchall()
                    self.clear()
            except Exception as error:
                db.rollback()
                print(error)
                messagebox.showerror("Error","Record not Added!")

#---------------Editing User----------------
class editUser():
    def update(self,rows):
        self.trv.delete(*self.trv.get_children())
        for i in rows:
            self.trv.insert('','end',values=i)

    def clear(self):
        db=MySQLdb.connect('localhost','root','root','emiloancalculator')
        cursor = db.cursor()
        query= "select * from user "
        cursor.execute(query)
        rows=cursor.fetchall()
        self.update(rows)

    def updateUser(self):
        self.uid=self.User_ID.get()
        self.pas=self.password.get()
        self.sq=self.securityq.get()
        self.sa=self.securitya.get()
        self.rname=self.rlname.get()
        self.dobr=self.dob.get()
        self.addr=self.address.get()
        self.pho=self.phone.get()
        self.mob=self.mobile.get()
        self.mail=self.email.get()
        
        if(len(self.pas) == 0 or len(self.sq) == 0 or len(self.sa) == 0 or len(self.rname) == 0 or len(self.mobile) == 0 or len(self.email) == 0):
            messagebox.showerror("Error", "Empty field error!")
            return
        elif ('@' not in self.email or '.com' not in self.email):
            messagebox.showerror("Error", "Invalid email address!")
        
        else:
            try:
                db=MySQLdb.connect('localhost','root','root','emiloancalculator')
                cursor = db.cursor()
                sqlquery1="update user set Password='"+self.pas+"', Security_Question='"+self.sq+"',Security_Answer='"+self.sa+"' where User_ID='"+self.uid+"'"
                cursor.execute(sqlquery1)
                sqlquery1="update user set Name='"+self.rname+"', Date_of_birth='"+self.dobr+"',Address='"+self.addr+"',Phone='"+self.pho+"',Mobile='"+self.mob+"',Gmail='"+self.mail+"' where User_ID='"+self.uid+"'"
                cursor.execute(sqlquery1)
                db.commit()
                messagebox.showinfo("Success","User Updated successfully....!")
                rows=cursor.fetchall()
                self.clear()
            except Exception as error:
                db.rollback()
                print(error)
                messagebox.showerror("Error","Failed to update record!")

    def __init__(self,win):
        top1=Toplevel(win)
        top1.geometry('1000x560+200+100')
        #top1.config(background="sky blue")
        top1.title('EditUser')
        top1.configure(background="cyan")
        p=PhotoImage(file='emiImages//ulogo1.png')
        top1.iconphoto(False,p)

        frame1=tk.LabelFrame(top1,background="cyan")
        frame2=tk.LabelFrame(top1,text='User list',background="cyan")
        frame1.pack(fill="both",expand="yes",padx=20,pady=10)
        frame2.pack(fill="both",expand="yes",padx=20,pady=10)
        
        self.trv=ttk.Treeview(frame2,columns=(1,2,3,4,5,6,7),show="headings",height="10")
        self.trv.pack()
        
        self.trv.heading(1,text="User_ID")
        self.trv.heading(2,text="Username")
        self.trv.heading(3,text="Password")
        self.trv.heading(4,text="UserType")
        self.trv.heading(5,text="UserStatus")
        self.trv.heading(6,text="SecurityQues")
        self.trv.heading(7,text="SecurityAns")

        c=0
        db=MySQLdb.connect('localhost','root','root','emiloancalculator')
        cursor = db.cursor()
        query= "select * from user"
        cursor.execute(query)
        rows=cursor.fetchall()
        
        for row in rows:
            c+=1
        self.update(rows)


        tk.Label(frame1,text='Edit Record',bg="cyan",fg="black",font=("Verdana",20,"bold")).grid(row=1,column=1 , padx=10, pady=10,columnspan=3)
        tk.Label(frame1,text='            ',bg="cyan",fg="cyan").grid(row=2,column=4 , padx=10, pady=10)
        tk.Label(frame1,text='            ',bg="cyan",fg="cyan").grid(row=2,column=7 , padx=10, pady=10)
        #tk.Label(frame1,text='            ',bg="cyan",fg="cyan").grid(row=2,column=6 , padx=10, pady=10)
        tk.Label(frame1,text='          ',bg="cyan",fg="cyan").grid(row=15,column=1 , padx=10, pady=2)
        img=ImageTk.PhotoImage(Image.open("emiImages//min5.jpg"))
        pic=Label(frame1,image=img).grid(row=2,column=8,rowspan=14,columnspan=2)

        tk.Label(frame1,text='User ID',bg="cyan").grid(row=2,column=2,padx=10, pady=10)
        self.num=[]
        for i in range(c):
            self.num.append(i+1)
        self.User_ID=Combobox(frame1,values=self.num)
        self.User_ID.grid(row=2,column=3)
        
        tk.Label(frame1,text='Username',bg="cyan").grid(row=4,column=2 , padx=10, pady=10)
        self.username=Entry(frame1, width=28)
        self.username.grid(row=4,column=3)
        
        tk.Label(frame1,text='Name',bg="cyan").grid(row=4,column=5, padx=10, pady=10)
        self.rlname=Entry(frame1, width=28)
        self.rlname.grid(row=4,column=6)

        tk.Label(frame1,text='Password',bg="cyan").grid(row=6,column=2, padx=10, pady=10)
        self.password=Entry(frame1, width=28)
        self.password.grid(row=6,column=3)
        
        tk.Label(frame1,text='DOB',bg="cyan").grid(row=6,column=5, padx=10, pady=10)
        self.dob=Entry(frame1, width=28)
        self.dob.grid(row=6,column=6)

        tk.Label(frame1,text='User_Type',bg="cyan").grid(row=8,column=2,padx=10, pady=10)
        self.usertype=Entry(frame1, width=28)
        self.usertype.grid(row=8,column=3)

        tk.Label(frame1,text='Address',bg="cyan").grid(row=8,column=5,padx=10, pady=10)
        self.address=Entry(frame1, width=28)
        self.address.grid(row=8,column=6)
        
        tk.Label(frame1,text='User_Status',bg="cyan").grid(row=10,column=2, padx=10, pady=10)
        self.userstatus=Entry(frame1, width=28)
        self.userstatus.grid(row=10,column=3)

        tk.Label(frame1,text='Phone',bg="cyan").grid(row=10,column=5, padx=10, pady=10)
        self.phone=Entry(frame1, width=28)
        self.phone.grid(row=10,column=6)

        tk.Label(frame1,text='Security_Question',bg="cyan").grid(row=12,column=2, padx=10, pady=10)
        self.course=("What is your pet's name?",'What is your favourite color?','What is your First school name?','What is your Hobby?','Which country you were born in?')
        self.securityq=Combobox(frame1,values=self.course,width=25)
        self.securityq.grid(row=12,column=3)

        tk.Label(frame1,text='Mobile',bg="cyan").grid(row=12,column=5, padx=10, pady=10)
        self.mobile=Entry(frame1, width=28)
        self.mobile.grid(row=12,column=6)

        tk.Label(frame1,text='Security_Answer',bg="cyan").grid(row=14,column=2, padx=10, pady=10)
        self.securitya=Entry(frame1, width=28)
        self.securitya.grid(row=14,column=3)

        tk.Label(frame1,text='E-mail',bg="cyan").grid(row=14,column=5, padx=10, pady=10)
        self.email=Entry(frame1, width=28)
        self.email.grid(row=14,column=6)

        ttk.Button(frame1,text='Update Record',command=lambda:self.updateUser).grid(row=16,column=4)

        top1.mainloop()

#---------------Deleting User-----------------
class deleteUser():
    def update(self,rows):
        self.trv.delete(*self.trv.get_children())
        for i in rows:
            self.trv.insert('','end',values=i)

    def clear(self):
        db=MySQLdb.connect('localhost','root','root','emiloancalculator')
        cursor = db.cursor()
        query= "select * from user "
        cursor.execute(query)
        rows=cursor.fetchall()
        self.update(rows)

    def deleteUser(self):
        self.uid=self.User_ID.get() 
        
        if(len(self.User_ID.get()) == 0):
            messagebox.showerror("Error", "Empty field error!")
        
        else:
            try:
                db=MySQLdb.connect('localhost','root','root','emiloancalculator')
                cursor = db.cursor()
                query="select * from user where User_ID='"+self.uid+"'"
                res=cursor.execute(query)
                if res:
                    ans=messagebox.askyesno("Confirm Delete?","Do you want to delete this record?")
                    if ans=="True":
                        query1="delete from user where User_ID='"+ self.uid+"'"
                        cursor.execute(query1)
                        query2="delete from user_personal where User_ID='"+ self.uid+"'"
                        cursor.execute(query2)
                        db.commit()
                        messagebox.showinfo("Delete Status","Deleted successfully")
                        rows=cursor.fetchall()
                        self.clear()
                else:
                    messagebox.showinfo("Error","Record doesn't exist!")
            except Exception as error:
                db.rollback()
                print(error)
                messagebox.showerror("Error","Failed to delete record!")

    def __init__(self,win):
        top2=Toplevel(win)
        top2.geometry('900x400+200+130')
        top2.title('DeleteUser')
        top2.configure(background="cyan")
        p=PhotoImage(file='emiImages//ulogo1.png')
        top2.iconphoto(False,p)

        frame1=tk.LabelFrame(top2,text="Delete user Record",background="cyan",width=500)
        frame2=tk.LabelFrame(top2,text='user list',background="cyan")
        
        frame1.pack(fill="both",padx=20,pady=10)
        frame2.pack(fill="both",expand="yes",padx=20,pady=20)
        
        self.trv=ttk.Treeview(frame2,columns=(1,2,3,4,5,6,7),show="headings",height="10")
        self.trv.pack()
        
        self.trv.heading(1,text="User_ID")
        self.trv.heading(2,text="Username")
        self.trv.heading(3,text="Password")
        self.trv.heading(4,text="UserType")
        self.trv.heading(5,text="UserStatus")
        self.trv.heading(6,text="SecurityQues")
        self.trv.heading(7,text="SecurityAns")

        db=MySQLdb.connect('localhost','root','root','emiloancalculator')
        cursor = db.cursor()
        query= "select * from user"
        cursor.execute(query)
        rows=cursor.fetchall()
        self.update(rows)

        tk.Label(frame1,text='    ',bg="cyan",fg="cyan").grid(row=1,column=1)
        tk.Label(frame1,text='    ',bg="cyan",fg="cyan").grid(row=1,column=2)
        tk.Label(frame1,text='         ',bg="cyan",fg="cyan").grid(row=1,column=6)
        tk.Label(frame1,text='         ',bg="cyan",fg="cyan").grid(row=1,column=7)
        tk.Label(frame1,text='User_ID',bg="cyan").grid(row=2,column=3 , padx=10, pady=10)
        self.User_ID=Entry(frame1, width=25)
        self.User_ID.grid(row=2,column=4, padx=10, pady=10)
        
        ttk.Button(frame1,text='Delete Record',command=self.deleteUser).grid(row=2,column=5,padx=10)
        img=ImageTk.PhotoImage(Image.open("emiImages//min9.jpg"))
        tk.Label(frame1,image=img).grid(row=1,column=8,rowspan=3,columnspan=3)
        
        top2.mainloop()
    
#-----------Updating User_Account_Details----------
class userAccDet():    
    def __init__(self,win,uid):
        top3=Toplevel(win)
        top3.geometry('740x410+200+100')
        top3.title('User Account Details')
        top3.configure(background="cyan")
        p=PhotoImage(file='emiImages//ulogo2.png')
        top3.iconphoto(False,p)

        self.lbl=tk.Label(top3,text="User Account Detail",font=("arial",20,'bold'),bg="cyan")
        self.lbl.place(x=110,y=20)

        self.lbl1=tk.Label(top3,text="User ID",font=("arial",12,"bold"),bg="cyan")
        self.lbl1.place(x=20,y=100)
        self.uid=Entry(top3,width=25)
        self.uid.place(x=180,y=100)
        self.uid.insert(0,uid)
        self.uid.config(background="light gray",state=DISABLED)

        self.lbl2=tk.Label(top3,text="Username *",font=('arial',12,"bold"),bg="cyan")
        self.lbl2.place(x=20,y=150)
        self.uname=Entry(top3,width=25)
        self.uname.place(x=180,y=150)

        self.lbl3=tk.Label(top3,text="Password *",font=("arial",12,"bold"),bg="cyan")
        self.lbl3.place(x=20,y=200)
        self.password=Entry(top3,width=25)
        self.password.place(x=180,y=200)
        
        path = "emiImages//min4.jpg"
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.panel = tk.Label(top3, image = self.img)
        self.panel.place(x=485,y=125)

        self.lbl4=tk.Label(top3,text="Security Question *",font=('ariel',12,"bold"),bg="cyan")
        self.lbl4.place(x=20,y=250)
        self.course=("What is your pet's name?",'What is your favourite color?','What is your First school name?','What is your Hobby?','Which country you were born in?')
        self.securityQues=Combobox(top3,values=self.course)
        self.securityQues.place(x=180,y=250,width=200)

        self.lbl5=tk.Label(top3,text="Security Answer *",font=('arial',12,"bold"),bg="cyan")
        self.lbl5.place(x=20,y=300)
        self.securityans=Entry(top3,width=25)
        self.securityans.place(x=180,y=300)

        self.btn=Button(top3,text="Update",command=lambda:self.updateData(uid))#
        self.btn.place(x=180,y=350)
        #self.btn=Button(top3,text="Save",command=self.insertData)#
        #self.btn.place(x=300,y=350)
                
        dbcon = MySQLdb.connect('localhost','root','root','emiloancalculator')
        cursorobj = dbcon.cursor()
        cursorobj.execute("select Username,Password,Security_Question,Security_Answer from user where User_ID=%s",(uid,))
        #print(self.username)
        data = cursorobj.fetchall()
        #print(data)     
        count = 1
        if count > 0:
                for row in data:       
                    #self.uid.insert(END,(row[0]))
                    self.uname.insert(0,row[0])
                    self.password.insert(0,row[1])
                    self.securityQues.insert(0,row[2])
                    self.securityans.insert(0,row[3])

        else:
                messagebox.showinfo("Record not found!")
        dbcon.close()

        top3.mainloop()
    
    def updateData(self,uid):
        #self.uid=self.uid.get()
        self.uname=self.uname.get()
        self.password=self.password.get()
        self.securityQues=self.securityQues.get()
        self.securityans=self.securityans.get()
        
        if (len(self.uname)==0 or len(self.password)==0 or len(self.securityQues)==0 or len(self.securityans)==0):
            messagebox.showerror("Error","Fill fields marked with *")
        else:
            try:       
                db=MySQLdb.connect('localhost','root','root','emiloancalculator')
                cursor=db.cursor()
                sqlquery="update user set Username=%s , Password=%s,Security_Question=%s,Security_Answer=%s where User_ID=%s"
                cursor.execute(sqlquery,(self.uname,self.password,self.securityQues,self.securityans,uid))
                db.commit()
                #print("Record update successfully.....!")
                messagebox.showinfo("Success","Record has been update succesfully.")
            except MySQLdb.Error as error:
                db.rollback()            
                print('Fail to insert the record',error)
                messagebox.showerror("Error","Some Error Occured!")

#----------Updating User_Personal_Details---------------
class userPerDet():
    def __init__(self,win,uid):
        top4=Toplevel(win)
        top4.geometry('900x560+170+80')
        top4.title('User Personal Details')
        top4.configure(background="cyan")
        p=PhotoImage(file='emiImages//ulogo2.png')
        top4.iconphoto(False,p)

        self.lbl=tk.Label(top4,text="Profile Personal Detail",font=("arial",20,'bold'),bg="cyan")
        self.lbl.place(x=110,y=20)

        self.lbl1=tk.Label(top4,text="User ID",font=("arial",12,"bold"),bg="cyan")
        self.lbl1.place(x=20,y=100)
        self.uid=Entry(top4)
        self.uid.insert(0,uid)
        self.uid.config(background="light gray",state=DISABLED)
        self.uid.place(x=180,y=100)

        self.lbl2=tk.Label(top4,text="Name *",font=('arial',12,"bold"),bg="cyan")
        self.lbl2.place(x=20,y=150)
        self.name=Entry(top4)
        self.name.place(x=180,y=150)
                
        path = "emiImages//min3.jpg"
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.panel = tk.Label(top4, image = self.img)
        self.panel.place(x=650,y=170)

        self.lbl3=tk.Label(top4,text="Date Of Birth",font=("arial",12,"bold"),bg="cyan")
        self.lbl3.place(x=20,y=200)
        self.course=[]
        for i in range(1,32):
            self.course.append(i)
        self.Date_of_birth1=Combobox(top4,values=self.course)
        self.Date_of_birth1.place(x=180,y=200,width=30)

        self.course2 = (' January',' February', ' March',' April',' May',' June',' July',' August',' September',' October', ' November', ' December') 

        self.Date_of_birth2=Combobox(top4,values=self.course2)
        self.Date_of_birth2.place(x=230,y=200,width=90)

        self.course1=[]
        for i in range(1950,2021):
            self.course1.append(i)

        self.Date_of_birth3=Combobox(top4,values=self.course1)
        self.Date_of_birth3.place(x=340,y=200,width=55)
        
        self.lbl4=tk.Label(top4,text="Address *",font=('ariel',12,"bold"),bg="cyan")
        self.lbl4.place(x=20,y=250)

        self.lbl4=tk.Label(top4,text="Street Address",font=('ariel',10),bg="cyan")
        self.lbl4.place(x=320,y=250)
        self.Address1=Entry(top4)
        self.Address1.place(x=180,y=250)

        self.lbl41=tk.Label(top4,text="Pincode",font=('ariel',10),bg="cyan")
        self.lbl41.place(x=320,y=280)
        self.Address2=Entry(top4)
        self.Address2.place(x=180,y=280)

        self.lbl411=tk.Label(top4,text="City",font=('ariel',10),bg="cyan")
        self.lbl411.place(x=560,y=280)
        self.Address3=Entry(top4)
        self.Address3.place(x=400,y=280)

        self.lbl42=tk.Label(top4,text="State",font=('ariel',10),bg="cyan")
        self.lbl42.place(x=320,y=310)
        self.Address4=Entry(top4)
        self.Address4.place(x=180,y=310)

        self.lbl43=tk.Label(top4,text="Country",font=('ariel',10),bg="cyan")
        self.lbl43.place(x=560,y=310)
        self.countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua And Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia And Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', 'Croatia', 'Curacao', 'Cyprus', 'Czech Republic', 'Democratic Republic Of The Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Estonia', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle Of Man', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Libyan Arab Jamahiriya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Russian Federation', 'Rwanda', 'Saint Kitts And Nevis', 'Saint Lucia', 'Saint Martin', 'Saint Pierre And Miquelon', 'Saint Vincent And The Grenadines', 'Samoa', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Taiwan', 'Tajikistan', 'Tanzania', 'Tanzania, United Republic Of', 'Thailand', 'Togo', 'Tonga', 'Trinidad And Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks And Caicos Islands', 'U.S. Virgin Islands', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Wallis And Futuna', 'Yemen', 'Zambia', 'Zimbabwe']

        self.Address5=Combobox(top4,values=self.countries)
        self.Address5.place(x=400,y=310,width=150)

        self.lbl5=tk.Label(top4,text="Phone",font=('ariel',12,"bold"),bg="cyan")
        self.lbl5.place(x=20,y=360)
        self.phone=Entry(top4)
        self.phone.place(x=180,y=360)

        self.lbl6=tk.Label(top4,text="Mobile *",font=('ariel',12,"bold"),bg="cyan")
        self.lbl6.place(x=20,y=410)
        self.mobile=Entry(top4)
        self.mobile.place(x=180,y=410)
        
        self.lbl7=tk.Label(top4,text='Email *',font=('ariel',12,"bold"),bg="cyan")
        self.lbl7.place(x=20,y=460)
        self.gmail=Entry(top4)
        self.gmail.place(x=180,y=460)

        self.btn=Button(top4,text="Update",command=lambda:self.updateData1(uid))#
        self.btn.place(x=180,y=510)
        '''self.btn=Button(top4,text="Save",command=self.insertData1)#
        self.btn.place(x=300,y=550)'''

        dbcon = MySQLdb.connect('localhost','root','root','emiloancalculator')
        cursorobj = dbcon.cursor()
        cursorobj.execute("select * from user_personal where User_ID=%s",(uid,))
        #print(self.usernwiname)
        data = cursorobj.fetchall()
        #print(data)
        
        count = 1
        if count > 0:
                for row in data:

                    #self.uid.insert(END,(row[0]))
                    self.name.insert(END,row[1])
                    row1=row[2].split()
                    #print(row1)
                    self.Date_of_birth1.insert(END,row1[0])
                    self.Date_of_birth2.insert(END,row1[1])
                    self.Date_of_birth3.insert(END,row1[2])
                    row2=row[3].split(',')
                    self.Address1.insert(END,row2[0])
                    self.Address2.insert(END,row2[1])
                    self.Address3.insert(END,row2[2])
                    self.Address4.insert(END,row2[3])
                    self.Address5.insert(END,row2[4])
                    self.phone.insert(END,row[4])
                    self.mobile.insert(END,row[5])
                    self.gmail.insert(END,row[6])
        else:
                messagebox.showinfo("record not found")
        dbcon.close()

        top4.mainloop()

    def updateData1(self,uid):
        self.uid=self.uid.get()
        self.name=self.name.get()
        self.Date_of_birth=(self.Date_of_birth1.get() + " " + self.Date_of_birth2.get()+ " " + self.Date_of_birth3.get())
        self.Address=self.Address1.get() + "," + self.Address2.get()+ "," + self.Address3.get()+ "," + self.Address4.get()+ "," + self.Address5.get()
        self.phone=self.phone.get()
        self.mobile=self.mobile.get()
        self.gmail=self.gmail.get()

        if(len(self.name)==0 or len(self.Address)==0 or len(self.mobile)==0 or len(self.gmail)==0):
            messagebox.showerror("Error","Fill fields marked with *")
        else:
            try:
                db=MySQLdb.connect('localhost','root','root','emiloancalculator')
                cursor=db.cursor()
                sqlquery="update user_personal set Name=%s ,Date_of_birth=%s,Address=%s, Phone=%s,Mobile=%s,Gmail=%s where User_ID=%s"
                cursor.execute(sqlquery,(self.name,self.Date_of_birth,self.Address,self.phone,self.mobile,self.gmail,self.uid))
                db.commit()
                print('record has been update successfully ')
                messagebox.showinfo("Success","Record has been update succesfully.")
            except MySQLdb.Error as error:
                db.rollback()            
                print('Fail to insert the record',error)

#___________Client Personal Details_____________
class cPerDet():
    
    def __init__(self,win):
        top5=Toplevel(win)
        top5.geometry('700x450+220+100')
        top5.title('Client Personal Details')
        top5.configure(background="cyan")
        p=PhotoImage(file='emiImages//ulogo3.png')
        top5.iconphoto(False,p)

        self.lbl=tk.Label(top5,text="Client Personal Details ",font=("arial",20,'bold'),bg="cyan").pack(pady=20)
        self.ID=tk.Label(top5,text="Client ID  ",bg="cyan")
        self.ID.place(x=50,y=80)
        self.Client_id=Entry(top5)
        self.Client_id.place(x=180,y=80)

        db=MySQLdb.connect('localhost','root','root','emiloancalculator')
        cursor=db.cursor()
        c=0
        sqlquery="select * from client_personal"
        cursor.execute(sqlquery,)
        res=cursor.fetchall()
        for row in res:
            c+=1
        db.close()
        self.Client_id.insert(0,c+1)

        path = "emiImages//min10.jpg"
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.panel = tk.Label(top5, image = self.img)
        self.panel.place(x=400,y=100)

        self.name=tk.Label(top5,text="Client Name * ",bg="cyan")
        self.name.place(x=50,y=120)
        self.Client_name=Entry(top5)
        self.Client_name.place(x=180,y=120)
        self.add=tk.Label(top5,text="Address * ",bg="cyan")
        self.add.place(x=50,y=160)
        self.Address=Entry(top5)
        self.Address.place(x=180,y=160)
        self.num=tk.Label(top5,text="Phone  ",bg="cyan")
        self.num.place(x=50,y=200)
        self.Number=Entry(top5)
        self.Number.place(x=180,y=200)
        self.mob=tk.Label(top5,text="Mobile * ",bg="cyan")
        self.mob.place(x=50,y=240)
        self.Mobile=Entry(top5)
        self.Mobile.place(x=180,y=240)
        self.pancard=tk.Label(top5,text="Pan * ",bg="cyan")
        self.pancard.place(x=50,y=280)
        self.Pancard=Entry(top5)
        self.Pancard.place(x=180,y=280)

        '''self.buttonA=Button(top5,text="First")
        self.buttonA.place(x=100,y=300)
        self.buttonB=Button(top5,text="Previous")
        self.buttonB.place(x=180,y=300)'''
        self.buttonC=ttk.Button(top5,text="Next" , command=lambda:cProfDet(win))
        self.buttonC.place(x=100,y=330)
        self.buttonD=ttk.Button(top5,text="Last", command=lambda:cResDet(win))
        self.buttonD.place(x=180,y=330)
        '''self.buttonE=Button(top5,text="Add")
        self.buttonE.place(x=100,y=340)'''

        self.buttonF=ttk.Button(top5,text="Update",command=self.updateData)
        self.buttonF.place(x=60,y=370)
        self.buttonG=ttk.Button(top5,text="Save", command=self.insertData)
        self.buttonG.place(x=140,y=370)
        self.buttonH=ttk.Button(top5,text="Cancel",command=top5.destroy)
        self.buttonH.place(x=220,y=370)

        top5.mainloop()

    def insertData(self):
        self.Cid=self.Client_id.get()
        self.Cname= self.Client_name.get()
        self.Ads=self.Address.get()
        self.Ner=self.Number.get()
        self.Mle=self.Mobile.get()
        self.Pard=self.Pancard.get()
        
        db=MySQLdb.connect('localhost','root','root','emiloancalculator')
        cursor=db.cursor()
        print("hello")
        try:
            print("Hi")
            sqlquery='insert into client_personal(Client_id, Client_name, Address, Number,Mobile,Pancard ) values(%s,%s,%s,%s,%s,%s)'
    
            cursor.execute(sqlquery,(self.Cid, self.Cname, self.Ads, self.Ner,self.Mle,self.Pard ))
            res=cursor.fetchall()
            db.commit()
            print('Record has been saved successfully ')
            messagebox.showinfo("Success","Record has been saved succesfully.")
        except MySQLdb.Error as error:
            print('Fail to insert the record',error)

    def updateData(self):
        self.Client_id=self.Client_id.get()
        self.Client_name= self.Client_name.get()
        self.Address=self.Address.get()
        self.Number=self.Number.get()
        self.Mobile=self.Mobile.get()
        self.Pancard=self.Pancard.get()
        
        try:
            db=MySQLdb.connect('localhost','root','root','emiloancalculator')
            cursor=db.cursor()
        
            sqlquery="update client_personal set Client_name=%s, Address=%s, Number=%s,Mobile=%s,Pancard=%s where Client_id=%s"
    
            res = cursor.execute(sqlquery,(self.Client_name, self.Address, self.Number,self.Mobile,self.Pancard,self.Client_id ))
            db.commit()
            print('Record has been updated successfully ')
            messagebox.showinfo("Success","Record has been updated succesfully.")
    
        except MySQLdb.Error as error:
            db.rollback()
            print('Fail to update the record',error)

#__________Client Professional Details___________
class cProfDet():
    
    def __init__(self,win):
        top6=Toplevel(win)
        top6.geometry('700x450+150+100')
        top6.title('Client Professional Details')
        top6.configure(background="cyan")
        p=PhotoImage(file='emiImages//ulogo3.png')
        top6.iconphoto(False,p)

        self.lbl1=tk.Label(top6,text="Client Professional Details" ,font=("arial",20,'bold'),bg="cyan").pack()
        self.clientID=tk.Label(top6,text="Client ID  *",bg="cyan")
        self.clientID.place(x=50,y=55)
        self.Client_id=Entry(top6)
        self.Client_id.place(x=180,y=55)
    
        db=MySQLdb.connect('localhost','root','root','emiloancalculator')
        cursor=db.cursor()
        c=0
        sqlquery="select * from client_professional"
        cursor.execute(sqlquery,)
        res=cursor.fetchall()
        for row in res:
            c+=1
        db.close()
        self.Client_id.insert(0,c+1)

        path = "emiImages//min1.jpg"
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.panel = tk.Label(top6, image = self.img)
        self.panel.place(x=400,y=80)
    
        self.profession=tk.Label(top6,text="Profession  *",bg="cyan")
        self.profession.place(x=50,y=95)
        self.profession1=Entry(top6)
        self.profession1.place(x=180,y=95)
        self.designation=tk.Label(top6,text="Designation  *",bg="cyan")
        self.designation.place(x=50,y=135)
        self.designation1=Entry(top6)
        self.designation1.place(x=180,y=135)
        self.phonenum=tk.Label(top6,text="Office Phone  *",bg="cyan")
        self.phonenum.place(x=50,y=175)
        self.phone_num=Entry(top6)
        self.phone_num.place(x=180,y=175)
        self.address1=tk.Label(top6,text="Office Address  *",bg="cyan")
        self.address1.place(x=50,y=215)
        self.address=Entry(top6)
        self.address.place(x=180,y=215)
        self.income=tk.Label(top6,text="Annual Income  *",bg="cyan")
        self.income.place(x=50,y=255)
        self.annual_income=Entry(top6)
        self.annual_income.place(x=180,y=255)
        self.other=tk.Label(top6,text="Other Income *",bg="cyan")
        self.other.place(x=50,y=295)
        self.other_income=Entry(top6)
        self.other_income.place(x=180,y=295)

        '''self.buttonA=Button(top6,text="First",command=lambda: cPerDet(win))
        self.buttonA.place(x=100,y=360)'''
        self.buttonB=Button(top6,text="Previous",command=lambda:cPerDet(win))
        self.buttonB.place(x=100,y=365)
        self.buttonC=Button(top6,text="Next",command=lambda:cResDet(win))
        self.buttonC.place(x=180,y=365)
        '''self.buttonD=Button(top6,text="Last",command=lambda:cResDet(win))
        self.buttonD.place(x=340,y=360)
        self.buttonE=Button(top6,text="Add")
        self.buttonE.place(x=100,y=400)'''

        self.buttonF=Button(top6,text="Update", command=self.updateDataA)
        self.buttonF.place(x=60,y=405)
        self.buttonG=Button(top6,text="Save",command=self.insertDataA)
        self.buttonG.place(x=140,y=405)
        self.buttonH=Button(top6,text="Cancel",command=top6.destroy)
        self.buttonH.place(x=220,y=405)

        top6.mainloop()

    def updateDataA(self):
        self.Client_id=self.Client_id.get()
        self.profession1= self.profession1.get()
        self.designation1=self.designation1.get()
        self.phone_num=self.phone_num.get()
        self.address=self.address.get()
        self.annual_income=self.annual_income.get()
        self.other_income=self.other_income.get()
   
        if(len(self.Client_id)==0 or len(self.profession1)==0 or len(self.designation1)==0 or len(self.phone_num)==0 or len(self.address)==0 or len(self.annual_income)==0 or len(self.other_income)==0):
            messagebox.showerror("Error","Fill fields marked with *")
        else:
            try:
                db=MySQLdb.connect('localhost','root','root','emiloancalculator')
                cursor=db.cursor()
            
                sqlquery="update client_professional set profession1=%s, designation1=%s,phone_num=%s,address=%s,annual_income=%s,other_income=%s where Client_id=%s"
        
                res = cursor.execute(sqlquery,(self.profession1, self.designation1, self.phone_num,self.address,self.annual_income,self.other_income,self.Client_id))
                db.commit()
                print('record has been updated successfully ')
                messagebox.showinfo("Success","Record has been updated succesfully.")
            except MySQLdb.Error as error:
                db.rollback()
                print('Fail to update the record',error)

    def insertDataA(self):
        self.Client_id=self.Client_id.get()
        self.profession1= self.profession1.get()
        self.designation1=self.designation1.get()
        self.phone_num=self.phone_num.get()
        self.address=self.address.get()
        self.annual_income=self.annual_income.get()
        self.other_income=self.other_income.get()

        try:
            db=MySQLdb.connect('localhost','root','root','emiloancalculator')
            cursor=db.cursor()
        
            sqlquery='insert into client_professional(Client_id, profession1, designation1,phone_num,address,annual_income,other_income) values(%s,%s,%s,%s,%s,%s,%s)'
    
            res = cursor.execute(sqlquery,(self.Client_id, self.profession1, self.designation1, self.phone_num,self.address,self.annual_income,self.other_income))
            db.commit()
            print('record has been saved successfully ')
            messagebox.showinfo("Success","Record has been saved succesfully.")
    
        except MySQLdb.Error as error:
            print('Fail to insert the record',error)

#________Client Responsibility Details___________
class cResDet():
    
    def __init__(self,win):
        top7=Toplevel(win)
        top7.geometry('700x470+150+100')
        top7.title('Client Responsibility Details')
        top7.configure(background="cyan")
        p=PhotoImage(file='emiImages//ulogo3.png')
        top7.iconphoto(False,p)

        self.lbl2=tk.Label(top7,text="Client Responsibility Details" ,font=("arial",18,'bold'),bg="cyan").pack()
        self.ClientId=tk.Label(top7,text="Client ID *",bg="cyan")
        self.ClientId.place(x=50,y=50)
        self.Client_id=Entry(top7)
        self.Client_id.place(x=180,y=50)

        db=MySQLdb.connect('localhost','root','root','emiloancalculator')
        cursor=db.cursor()
        c=0
        sqlquery="select * from client_responsibility"
        cursor.execute(sqlquery,)
        res=cursor.fetchall()
        for row in res:
            c+=1
        db.close()
        self.Client_id.insert(0,c+1)
    
        path = "emiImages//min7.jpg"
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.panel = tk.Label(top7, image = self.img)
        self.panel.place(x=400,y=100)

        self.tax=tk.Label(top7,text="Tax Deduction * ",bg="cyan")
        self.tax.place(x=50,y=90)
        self.tax1=Entry(top7)
        self.tax1.place(x=180,y=90)
        self.loan=tk.Label(top7,text="loan  ",bg="cyan")
        self.loan.place(x=50,y=130)
        self.emi1=Entry(top7)
        self.emi1.place(x=180,y=130)
        self.insurance=tk.Label(top7,text="Insurance EMI  ",bg="cyan")
        self.insurance.place(x=50,y=170)
        self.insurance1=Entry(top7)
        self.insurance1.place(x=180,y=170)
        self.rent=tk.Label(top7,text="House Rent ",bg="cyan")
        self.rent.place(x=50,y=210)
        self.rent1=Entry(top7)
        self.rent1.place(x=180,y=210)
        self.depend=tk.Label(top7,text="Dependents  ",bg="cyan")
        self.depend.place(x=50,y=250)
        self.depend1=Entry(top7)
        self.depend1.place(x=180,y=250)
        self.expenditure=tk.Label(top7,text=" Personal Expenditure ",bg="cyan")
        self.expenditure.place(x=50,y=290)
        self.personal_expenditure1=Entry(top7)
        self.personal_expenditure1.place(x=180,y=290)
        self.healthexpenditure1=tk.Label(top7,text=" Health Expenditure ",bg="cyan")
        self.healthexpenditure1.place(x=50,y=330)
        self.health_expenditure1=Entry(top7)
        self.health_expenditure1.place(x=180,y=330)
        self.buttonA=Button(top7,text="First",command=lambda:cPerDet(win))
        self.buttonA.place(x=100,y=390)
        self.buttonB=Button(top7,text="Previous",command=lambda:cProfDet(win))
        self.buttonB.place(x=180,y=390)
        '''self.buttonC=Button(top7,text="Next")
        self.buttonC.place(x=260,y=430)
        self.buttonD=Button(top7,text="Last")
        self.buttonD.place(x=340,y=400)
        self.buttonE=Button(top7,text="Add")
        self.buttonE.place(x=100,y=440)'''
    
        self.buttonF=Button(top7,text="Update", command=self.updateDataB)
        self.buttonF.place(x=60,y=430)
        self.buttonG=Button(top7,text="Save", command=self.insertDataB)
        self.buttonG.place(x=140,y=430)
        self.buttonH=Button(top7,text="Cancel",command=top7.destroy)
        self.buttonH.place(x=220,y=430)

        top7.mainloop()

    def updateDataB(self):
        self.Cid=self.Client_id.get()
        self.ta= self.tax1.get()
        self.emi=self.emi1.get()
        self.ins=self.insurance1.get()
        self.ren=self.rent1.get()
        self.dep=self.depend1.get()
        self.pex=self.personal_expenditure1.get()
        self.hex=self.health_expenditure1.get()
        
        try:
            db=MySQLdb.connect('localhost','root','root','emiloancalculator')
            cursor=db.cursor()
        
            sqlquery="update client_responsibility set tax1=%s, emi1=%s, insurance1=%s,rent1=%s,depend1=%s,personal_expenditure=%s,health_expenditure=%s where Client_id=%s"
    
            res = cursor.execute(sqlquery,(self.ta, self.emi, self.ins,self.ren,self.dep,self.pex,self.hex,self.Client_id))
            db.commit()
            print('record has been updated successfully ')
            messagebox.showinfo("Success","Record has been updated succesfully.")
        except MySQLdb.Error as error:
            db.rollback()
            print('Fail to update the record',error)

    def insertDataB(self):
        self.Client_id=self.Client_id.get()
        self.tax1= self.tax1.get()
        self.emi1=self.emi1.get()
        self.insurance1=self.insurance1.get()
        self.rent1=self.rent1.get()
        self.depend1=self.depend1.get()
        self.personal_expenditure1=self.personal_expenditure1.get()
        self.health_expenditure1=self.health_expenditure1.get()
        
        try:
            db=MySQLdb.connect('localhost','root','root','emiloancalculator')
            cursor=db.cursor()
        
            sqlquery='insert into client_responsibility(Client_id, tax1, emi1, insurance1,rent1,depend1,personal_expenditure,health_expenditure ) values(%s,%s,%s,%s,%s,%s,%s,%s)'
    
            res = cursor.execute(sqlquery,(self.Client_id, self.tax1, self.emi1, self.insurance1,self.rent1,self.depend1,self.personal_expenditure1,self.health_expenditure1))
            db.commit()
            print('record has been saved successfully ')
            messagebox.showinfo("Success","Record has been saved succesfully.")
        except MySQLdb.Error as error:
            print('Fail to insert the record',error)

#_________Loan Plan Details__________
class lPlanDet():
    def __init__(self,win):
        top8=Toplevel(win,bg = "#FFFFFF")
        top8.geometry('600x450+270+100')
        top8.title('Loan Plan Details')
        top8.configure(background="cyan")
        p=PhotoImage(file='emiImages//llogo.png')
        top8.iconphoto(False,p)

        db = MySQLdb.connect("127.0.0.1","root","root","emiloancalculator")
        cursor = db.cursor()
        cursor.execute("Select PlanType from loan_plans")
        data = cursor.fetchall()
        loan_options = []
        for i in data:
            loan_options.append(i[0])
            
        self.loan_id = StringVar()
        self.loan_id.set("")
        self.interest = StringVar()
        self.interest.set("")
        self.description = StringVar()
        self.description.set("")
        
        title = tk.Label(top8, text = "Loan Plan Detail", font = 80,bg="cyan",anchor="center")
        title.pack(pady = 20, ipadx = 10, ipady = 10)
        
        frame = tk.Frame(top8, width = 800 ,bg="cyan")
        frame.configure(padx = 10, pady = 20)
        frame.pack()
        
        tk.Label(frame, text="Plan Id",font=("arial",12,"bold"),bg="cyan").grid(row=0,  pady = 10, sticky = "W")
        tk.Label(frame, text="Plan Name", font = ("arial",12,"bold"),bg="cyan").grid(row=1, pady = 10, sticky = "W")
        tk.Label(frame,text="Interest Rate", font = ("arial",12,"bold"),bg="cyan").grid(row=2, pady = 10, sticky = "W")
        tk.Label(frame,text="Description", font = ("arial",12,"bold"),bg="cyan").grid(row=3, pady = 10, sticky = "W")
        tk.Label(frame,text="    ",bg="cyan",fg="cyan").grid(row=0,column=4)

        e1 = tk.Entry(frame, textvariable = self.loan_id, width = 23)
        
        loan_plans=tuple(loan_options)
        loan_type=StringVar()
        loan_type.set("Select a loan plan")
        loan_type.trace('w', lambda a, b, c: self.populate_fields(cursor, loan_type.get()))
        cb1=Combobox(frame, values = loan_plans, textvariable = loan_type, width = 20)
        cb1.grid(row = 1, column = 1, columnspan = 3)
        
        e3 = tk.Entry(frame, textvariable = self.interest, width = 23)
        e4=tk.Entry(frame, textvariable = self.description, width = 23)
        
        e1.grid(row=0, column=1, columnspan = 3)
        e3.grid(row=2, column=1, columnspan = 3)
        e4.grid(row=3, column=1, columnspan = 3)
        
        label = tk.Label(frame, text="", height = 2,bg="cyan",fg="cyan")
        label.grid(row = 5)
        
        '''Firstbt = tk.Button(frame, text="First",fg="BLUE", relief = "raised", width = 10)
        Firstbt.grid( row= 6, column=0)
        previousbt = tk.Button(frame, text="Previous",fg="BLUE", relief = "raised", width = 10)
        previousbt.grid( row= 6, column=1)
        nextbt = tk.Button(frame, text="Next",fg="BLUE", relief = "raised", width = 10)
        nextbt.grid( row= 6, column=2, padx = 2, pady = 5)
        lastbt = tk.Button(frame, text="Last",fg="BLUE", relief = "raised", width = 10)
        lastbt.grid( row= 6, column=3, padx = 2, pady = 5)'''
        addbt = tk.Button(frame, text="Add",fg="BLUE", relief = "raised", width = 10)
        addbt.grid( row= 7, column=0, padx = (2, 0), pady = (5, 0))
        updatebt = tk.Button(frame, text="Update",fg="BLUE", relief = "raised", width = 10)
        updatebt.grid( row= 7, column=1, padx = 2, pady = (5, 0))
        savebt = tk.Button(frame, text="Save",fg="BLUE", relief = "raised", width = 10)
        savebt.grid( row= 7, column=2, padx = 2, pady = (5, 0))
        cancelbt = tk.Button(frame, text="Cancel",fg="BLUE", relief = "raised", width = 10)#
        cancelbt.grid( row= 7, column=3, padx = 2, pady = (5, 0))

        '''path = "emiImages//min12.jpg"
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.panel = tk.Label(top8, image = self.img)
        self.panel.place(x=550,y=80)'''

        top8.mainloop()

    def populate_fields(self, cursor, loan_type):
        sql = "SELECT ID, Description, InterestRate from loan_plans where PlanType = '%s'" % (loan_type)
        cursor.execute(sql)
        data = cursor.fetchall()
        self.loan_id.set(str(data[0][0]))
        self.interest.set(str(data[0][2])+"%")
        self.description.set(data[0][1])

#_______Loan File Details___________
LARGEFONT =("Verdana", 13)
class lFileDet():

    def __init__(self,win):
        self.top9=Toplevel(win)
        self.top9.geometry('1040x675+100+10')
        self.top9.title('Loan File Details')
        self.top9.configure(background="cyan")
        p=PhotoImage(file='emiImages//llogo.png')
        self.top9.iconphoto(False,p)

        self.db = MySQLdb.connect("127.0.0.1","root","root","emiloancalculator")
        self.cursor = self.db.cursor()
        self.cursor.execute("select PlanType from loan_plans")
        data = self.cursor.fetchall()
        loan_options = []
        for i in data:
            loan_options.append(i[0])
            
        self.cursor.execute("select Client_name from client_personal")
        data= self.cursor.fetchall()
        clients = []
        for i in data:
            clients.append(i[0])
            
        self.cursor.execute("SELECT ID FROM loan_details ORDER BY ID DESC LIMIT 1")
        data = self.cursor.fetchone()
        if data != None:
            file_id = data[0] + 1
        else:
            file_id = 1
        title1 = tk.Label(self.top9, text = "Loan File Detail", font = 80, relief = "solid",bg="cyan")
        title1.grid(row = 0,column = 0, ipadx = 30, ipady = 10)
    
        title2 = tk.Label(self.top9, text = "Loan Evaluation Detail", font = 80, relief = "solid",bg="cyan")
        title2.grid(row = 0,column = 1, ipadx = 30, ipady = 10)
        
        #Loan File Detail Frame
        frame1 = tk.Frame(self.top9,bg="cyan")
        frame1.configure(width = 400, height = 600)
        frame1.grid(row = 1,column = 0, padx = 10, pady = 15)
        
        tk.Label(frame1, text="File Id", font = LARGEFONT,bg="cyan").grid(row=0, sticky = "W" )
        
        self.file_id = IntVar()
        self.file_id.set(file_id)
        self.file_id.trace("w", lambda name, index, mode, id : self.populate_previous_details())
        self.e1 = tk.Entry(frame1, textvariable = self.file_id, width = 25)
        self.e1.grid(row=0, column=1, sticky = "")
        
        tk.Label(frame1, text = "Plan", font  = LARGEFONT,bg="cyan").grid(row = 1, padx = 0, pady = 10,sticky="W")
        
        self.loan_type = StringVar()
        self.loan_type.set("Select loan type")
        self.loan_type.trace('w', lambda a, b, c: self.populate_interest())
        self.cb1=Combobox(frame1, values = loan_options, textvariable = self.loan_type, width = 22)
        self.cb1.grid(row = 1, column = 1)
        
        tk.Label(frame1, text = "Client", font  = LARGEFONT,bg="cyan").grid(row = 2, padx = 0, pady = 10, sticky = "W")
        
        self.client=StringVar()
        self.client.set("Select client name")
        self.client.trace('w', lambda a, b, c: self.populate_client())

        self.cb2=Combobox(frame1, values = clients, textvariable = self.client, width = 22)
        self.cb2.grid(row = 2, column = 1)
        
        self.amount = IntVar()
        self.amount.set(0)
        tk.Label(frame1, text="Loan amount", font = LARGEFONT,bg="cyan").grid(row = 3, padx = 0, pady = 10, sticky = "W")
        self.e2 = tk.Entry(frame1, textvariable= self.amount, width = 25)
        self.e2.grid(row=3, column=1)
        self.IdProof = IntVar()
        tk.Label(frame1, text = "ID Proof", font  = LARGEFONT,bg="cyan").grid(row = 4, padx = 0, pady = 10, sticky = "W")
        
        c1 = Checkbutton(frame1, variable = self.IdProof, command = self.check_status).grid(row = 4, column = 1)
        self.ResidenceProof = IntVar()
        tk.Label(frame1, text = "Residence Proof", font  = LARGEFONT,bg="cyan").grid(row = 5, padx = 0, pady = 10, sticky = "W")
        c2 = Checkbutton(frame1, variable = self.ResidenceProof, command = self.check_status).grid(row = 5, column = 1)
        
        self.IncomeProof = IntVar()
        tk.Label(frame1, text = "Income Proof", font  = LARGEFONT,bg="cyan").grid(row = 6, padx = 0, pady = 10, sticky = "W")
        c3 = Checkbutton(frame1, variable = self.IncomeProof, command = self.check_status).grid(row = 6, column = 1)
        self.BankStatement = IntVar()
        tk.Label(frame1, text = "Bank Statement", font  = LARGEFONT,bg="cyan").grid(row = 7, padx = 0, pady = 10, sticky = "W")
        c4 = Checkbutton(frame1, variable = self.BankStatement, command = self.check_status).grid(row = 7, column = 1)
        
        tk.Label(frame1, text="Remarks", font = LARGEFONT,bg="cyan").grid(row=8, padx = 0, pady = 0, sticky = "W")
        self.e3=tk.Text(frame1, width = 20, height = 6)
        self.e3.grid(row=8, column=1, padx = 50)
        
        tk.Label(frame1, text="Status", font = LARGEFONT,bg="cyan").grid(row=9, padx = 0, pady = 10, sticky = "W")
        self.statusLabel = tk.Label(frame1, font = 10, width = 15, relief = "solid")
        self.statusLabel.grid(row=9, column = 1, padx = 10, pady = 10)
        frame1.grid_propagate(0)

        #loan Evaluation Detail Frame
        frame2 = tk.Frame(self.top9, highlightbackground="black", highlightthickness = 1, width = 600, height = 600, padx = 20, pady = 15,background="cyan")
        frame2.grid(row = 1,column = 1, padx = 10, pady = 15)
        frame2.grid_propagate(0)
        
        tk.Label(frame2, text="Loan amount",bg="cyan").grid(row = 0, column = 0, padx = 0, pady = 10, sticky = "W")
        self.value=StringVar()
        self.value.set("")
        self.e4 = tk.Entry(frame2,textvariable = self.value, width = 17)
        self.e4.grid(row=0, column=1)
        
        tk.Label(frame2, text="Rate Of Interest",bg="cyan").grid(row = 0, column = 2, padx = 2, pady = 10, sticky = "W")
        self.interest=StringVar()
        self.interest.set("")
        self.e5 = tk.Entry(frame2,textvariable = self.interest, width = 17)
        self.e5.grid(row=0, column=3)
        
        tk.Label(frame2, text="Client Monthly Income",bg="cyan").grid(row = 1, column = 0, padx = 0, pady = 10, sticky = "W")
        self.salary = StringVar()
        self.salary.set("")
        self.e6 = tk.Entry(frame2,textvariable = self.salary, width = 17)
        self.e6.grid(row=1, column=1)
        tk.Label(frame2, text="Client Monthly Expenses",bg="cyan").grid(row = 1, column = 2, padx = 2, pady = 10, sticky = "W")
        self.monthlyexpense = StringVar()
        self.monthlyexpense.set("")
        self.e7 = tk.Entry(frame2,textvariable = self.monthlyexpense, width = 17)
        self.e7.grid(row=1, column=3)
        
        tk.Label(frame2, text="Number of years",bg="cyan").grid(row = 2, column = 0 , padx = 0, pady = 10, sticky = "W")
        self.years = IntVar()
        self.years.set("")
        self.e8 = tk.Entry(frame2,textvariable = self.years, width = 20)
        self.e8.grid(row=2, column=1)
        
        evalbt = Button(frame2, text="Evaluate", command = self.evaluate_emi)
        evalbt.grid( row= 2, column=2) 
        
        self.issuebtn = Button(frame2, text="Issue", command = self.save_details)
        self.issuebtn.grid( row= 2, column=3)
        self.issuebtn["state"] = "disabled"
        
        tk.Label(frame2, text="Loan Evaluation Result:", font = 10,bg="cyan").grid(row = 3, column = 0, columnspan = 2, padx = 0, pady = 10, sticky = "W")
        self.table = tk.Frame(frame2, highlightbackground="black", highlightthickness = 1, width = 550, height = 380, padx = 20, pady = 15)
        self.table.grid(row = 4, column = 0, columnspan = 4, padx = 10, pady = 15)
        self.table.grid_propagate(0)
        
        self.top9.mainloop()

    def populate_previous_details(self):
        file_data = ""
        try:
            self.id = self.file_id.get()
            sql = "SELECT ID, Client_id, PlanType, LoanAmount, IdProof, ResidenceProof, IncomeProof, BankStatement, Remarks, Duration FROM loan_details WHERE ID = %d" % (id)
            self.cursor.execute(sql)
            file_data = self.cursor.fetchone()
            self.id=file_data[1]
            sql = "SELECT Name FROM client_details WHERE ID = %s" % (file_data[1])
            self.cursor.execute(sql)
            client_name = self.cursor.fetchone()
            client_name = client_name[0]
            sql = "SELECT InterestRate FROM loan_plans WHERE PlanType = '%s'" % (file_data[2])
            self.cursor.execute(sql)
            interest = self.cursor.fetchone()
            interest = interest[0]
            if(file_data != None):
                self.loan_type.set(file_data[2])
                self.client.set(client_name)
                self.amount.set(file_data[3])
                self.IdProof.set(file_data[4])
                self.ResidenceProof.set(file_data[5])
                self.IncomeProof.set(file_data[6])
                self.BankStatement.set(file_data[7])
                self.years.set(file_data[9])
                self.interest.set(interest)
                self.e2["state"] = "disabled"
                self.cb1["state"] = "disabled"
                self.cb2["state"] = "disabled"
                self.e5["state"] = "disabled"
                self.e8["state"] = "disabled"
                self.check_status()
                self.issuebtn["state"] = "disabled"
        except:
            if(file_data == "" or file_data == None):
                self.loan_type.set("")
                self.client.set("")
                self.amount.set("")
                self.IdProof.set(0)
                self.ResidenceProof.set(0)
                self.IncomeProof.set(0)
                self.BankStatement.set(0)
                self.years.set("")
                self.interest.set("")
                self.monthlyexpense.set("")
                self.salary.set("")
                self.loan_type.set("Select loan type")
                self.client.set("Select client name")
                self.e2["state"] = "normal"
                self.cb1["state"] = "normal"
                self.cb2["state"] = "normal"
                self.e5["state"] = "normal"
                self.e8["state"] = "normal"
                self.issuebtn["state"] = "disabled"
                self.check_status()


    def populate_interest(self):
        sql = "SELECT InterestRate FROM loan_plans WHERE PlanType ='%s'"%(self.loan_type.get())
        self.cursor.execute(sql)
        interest = self.cursor.fetchone()
        self.interest.set(str(interest[0]) + "%")
        
    def populate_client(self):
        sql = "SELECT annual_income,other_income from client_professional where Client_id = '%s'"%(self.id)
        self.cursor.execute(sql)
        sal,ary= self.cursor.fetchone()
        salary=int(sal)+int(ary)
        msal=salary//12
        self.salary.set(msal)
        #self.monthlyexpense.set(salary[1])
        sql = "SELECT * from client_responsibility where Client_id = '%s'"%(self.id)
        self.cursor.execute(sql)
        exp= self.cursor.fetchone()
        expense=int(exp[1])+int(exp[2])+int(exp[3])+int(exp[4])+int(exp[6])+int(exp[7])+int(exp[5])*int(exp[6])
        self.monthlyexpense.set(expense)

    def check_status(self):
        if(bool(self.IdProof.get()) and bool(self.ResidenceProof.get()) and bool(self.IncomeProof.get()) and bool(self.BankStatement.get())):
            self.statusLabel.configure(text = "Approved",fg = "red")
            self.issuebtn["state"] = "normal"
        else:
            self.statusLabel.configure(text = "")
            self.issuebtn["state"] = "disabled"
        
    def save_details(self):
        self.cursor.execute("SELECT ID FROM client_details WHERE Name = '%s'" %(self.client.get()))
        client_id = self.cursor.fetchone()
        client_id = client_id[0]
        #Calculate EMI for filled in duration to save in DB
        amount = self.amount.get()
        interest = int(self.interest.get().replace("%","").strip()) / (12 * 100)
        duration = self.years.get() * 12
        emi = math.ceil((amount * interest * pow(1 + interest, duration)) / (pow(1 + interest, duration) - 1))
        sql = "INSERT INTO loan_details (Client_Id, PlanType, IdProof, ResidenceProof, IncomeProof, BankStatement, Remarks, LoanAmount, Duration, EMI) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql,(client_id, self.loan_type.get(), bool(self.IdProof.get()), bool(self.ResidenceProof.get()),bool(self.IncomeProof.get()), bool(self.BankStatement.get()), "Empty Remarks", self.amount.get(), self.years.get(), emi))
            self.db.commit()
            self.top9.destroy()
            #self.parent.show_window(win, LoanIssueDetail)
        except:
            print("Rolling back from Loan Plan Detail")
            self.db.rollback()
            
    def evaluate_emi(self):
        salary = int(self.salary.get().strip())
        expense = int(self.monthlyexpense.get().strip())
        interest = int(self.interest.get().replace("%","").strip())
        amount = int(self.value.get().strip())
        emi_details = [("Years", "Installment", "Status")]
        interest = interest / (12 * 100) # one month interest
        for years in range(1, 12):
            duration = years * 12 # one month period 
            emi = math.ceil((amount * interest * pow(1 + interest, duration)) / (pow(1 + interest, duration) - 1))
            if salary - expense > emi:
                conclusion = "Ok"
            else:
                conclusion = "No"
            emi_details.append((years, emi, conclusion))
            
            self.create_table(emi_details)
            
    def create_table(self, emi_details):
        total_rows = len(emi_details) 
        total_columns = len(emi_details[0]) 
        # code for creating table 
        for i in range(total_rows): 
            for j in range(total_columns): 
                self.e = Entry(self.table, width = 13, font = ('Arial',16)) 
                self.e.grid(row = i, column = j) 
                self.e.insert(END, emi_details[i][j]) 
                self.e["state"] = "disabled"

#_____________Loan Issue Details_____________
class lIssueDet():
    def __init__(self,win):
        self.top10=Toplevel(win)
        self.top10.geometry('620x500+200+100')
        self.top10.title('Loan Issue Details')
        self.top10.configure(background="cyan")
        p=PhotoImage(file='emiImages//llogo.png')
        self.top10.iconphoto(False,p)

        self.db = MySQLdb.connect("127.0.0.1","root","root","emiloancalculator")
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT ID FROM loan_details ORDER BY ID DESC LIMIT 1")
        data = self.cursor.fetchone()
        if data != None:
            file_id = data[0]
        else:
            file_id = ""
        
        title = tk.Label(self.top10, text = "Loan Issue Detail", font = 80, relief = "solid",bg="cyan")
        title.pack(pady = 20, ipadx = 10, ipady = 10)
        
        frame = tk.Frame(self.top10, highlightbackground="black", highlightthickness = 1, width = 800, padx = 10, pady = 50,bg="cyan")
        frame.pack()
        
        tk.Label(frame, text="Loan Id", font = 20,bg="cyan").grid(row=0, padx = 10, pady = 10, sticky = "W")
        tk.Label(frame, text="Issue Date", font = 20,bg="cyan").grid(row=1, padx = 10, pady = 10, sticky = "W")
        tk.Label(frame,text="Loan Duration", font = 20,bg="cyan").grid(row=2, padx = 10, pady = 10, sticky = "W")
        tk.Label(frame,text="EMI", font = 20,bg="cyan").grid(row=3, padx = 10, pady = 10, sticky = "W")
        tk.Label(frame,text="Cheque Number", font = 20,bg="cyan").grid(row=4, padx = 10, pady = 10, sticky = "W")
        #Entry for Loan ID
        self.loan_id = IntVar()
        self.loan_id.set(file_id)
        self.loan_id.trace("w", lambda name, index, mode, id : self.populate_fields())
        e1 = tk.Entry(frame, textvariable = self.loan_id, width = 27)
        #Entry for Issue date
        self.issue_date = StringVar()
        self.issue_date.set("")
        e2 = tk.Entry(frame, textvariable = self.issue_date, width = 27)
        #Entry for Duration
        self.duration = IntVar()
        self.duration.set("")
        e3 = tk.Entry(frame, textvariable = self.duration, width = 27)
        #Entry for EMI
        self.emi = IntVar()
        self.emi.set("")
        e4 = tk.Entry(frame, textvariable = self.emi, width = 27)
        #Entry for Cheque Number
        self.cheque_no = IntVar()
        self.cheque_no.set("")
        e5 = tk.Entry(frame, textvariable = self.cheque_no, width = 27)

        e1.grid(row=0, column=1, columnspan = 3)
        e2.grid(row=1, column=1, columnspan = 3)
        e3.grid(row=2, column=1, columnspan = 3)
        e4.grid(row=3, column=1, columnspan = 3)
        e5.grid(row=4, column=1, columnspan = 3)
        
        label = tk.Label(frame, text="", height = 2,bg="cyan")
        label.grid(row = 5, sticky = "W")
        
        '''Firstbt = tk.Button(frame, text="First")
        Firstbt.grid( row= 6, column=0, padx = 2, pady = 5)
        
        previousbt = tk.Button(frame, text="Previous")
        previousbt.grid( row= 6, column=1, padx = 2, pady = 5)
        
        nextbt = tk.Button(frame, text="Next")
        nextbt.grid( row= 6, column=2, padx = 2, pady = 5)
        
        lastbt = tk.Button(frame, text="Last")
        lastbt.grid( row= 6, column=3, padx = 2, pady = 5)'''
        
        addbt = Button(frame, text="Add")
        addbt.grid( row= 7, column=0, padx = 2, pady = (5, 0))
        updatebt = Button(frame, text="Update")
        updatebt.grid( row= 7, column=1, padx = 2, pady = (5, 0))
        savebt = Button(frame, text="Save", command = lambda: self.issue_loan(self.top10))
        savebt.grid( row= 7, column=2, padx = 2, pady = (5, 0))
        cancelbt = Button(frame, text="Cancel", command = lambda: self.top10.destroy())
        cancelbt.grid( row= 7, column=3, padx = 2, pady = (5, 0))

        '''path = "emiImages//smi1.jpg"
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.panel = tk.Label(self.top10, image = self.img)
        self.panel.place(x=500,y=120)'''

        self.top10.mainloop()

    def populate_fields(self):
        try:
            self.id = self.loan_id.get()
            sql = "SELECT Duration, EMI FROM loan_details WHERE ID = %d" % (id)
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            if(id != None):
                self.duration.set(data[0])
                self.emi.set(data[1])
        except:
            pass

    def issue_loan(self, loanIssueWindow):
        emi = self.emi.get()
        duration = self.duration.get()
        issue_date = self.issue_date.get()
        cheque_no = self.cheque_no.get()
        try:
            sql = "UPDATE loan_details SET Duration = %s, ChequeNo = %s, IssueDate = '%s', EMI = %s WHERE ID = %s" % (duration, cheque_no, issue_date, emi, self.loan_id.get())
            self.cursor.execute(sql)
            self.db.commit()
            loanIssueWindow.destroy()
        except:
            print("Rolling back from Loan Issue Detail")
            self.db.rollback()

"""class report():
    def __init__(self,win):
        top11=Toplevel(win)
        top11.geometry('400x400+200+150')
        top11.title('REPORTS')
        top11.configure(background="cyan")
        p=PhotoImage(file='emiImages//rlogo.png')
        top11.iconphoto(False,p)
        lbl=tk.Label(top11,text="Report Type",font=('arial',12,"bold"),bg="cyan")
        lbl.place(x=50,y=30)
        types=("User Report","Client Report","Loan Issue Report")
        report=Combobox(top11,values=types)
        report.place(x=200,y=30,width=110)

        self.trv=ttk.Treeview(top11,columns=(1,2,3,4,5,6,7),show="headings",height="10")
        self.trv.pack()
        
        self.trv.heading(1,text="User_ID")
        self.trv.heading(2,text="Username")
        self.trv.heading(3,text="Password")
        self.trv.heading(4,text="UserType")
        self.trv.heading(5,text="UserStatus")
        self.trv.heading(6,text="SecurityQues")
        self.trv.heading(7,text="SecurityAns")

    def update(self,rows):
        self.trv.delete(*self.trv.get_children())
        for i in rows:
            self.trv.insert('','end',values=i)


        top11.mainloop()
"""
    
        

if __name__=='__main__':
    #___________SPLASH _SCREEN_______________
    splash=Tk()
    splash.title("EMI Loan Calculator")
    splash.geometry("661x560+50+50")
    p=PhotoImage(file='emiImages//logo7.png')
    splash.iconphoto(False,p)
    
    image1=ImageTk.PhotoImage(Image.open("emiImages//loan_3.jpg"))
    labl=Label(splash,image=image1)
    label=Label(splash,text="EMI Loan Calculator",font=("Helvetica",25,"bold"))
    label.config(background="navy",foreground="white",anchor="center")
    label.pack(fill=BOTH,expand=True)
    labl.pack(fill=BOTH)
    label1=Label(splash,text="Developed by: PyCoders",font=("Courier",18,"bold"))
    label2=Label(splash,text="Copyright 2020 EMI Loan Calculator. All Rights Reserved",font=("calibri",10))
    label1.config(background="navy",foreground="white")
    label2.config(background="navy",foreground="white",anchor="e")

    pro=ttk.Progressbar(splash,orient=HORIZONTAL,length=500,mode='determinate',value=0)
    pro.pack(fill=BOTH)
    label1.pack(fill=BOTH)
    label2.pack(fill=BOTH)
    while pro['value']<100:
        pro['value']+=20
        labl.update()
        time.sleep(1)
    
    
    def main_win():
        splash.destroy()
        #___________MAIN_win________________
        win=Tk()
        win.title('EMI Calculator')
        p=PhotoImage(file='emiImages//logo7.png')
        win.iconphoto(False,p) 
        width=win.winfo_screenwidth()
        height=win.winfo_screenheight()
        win.geometry('%dx%d+0+0'%(width,height))
        win.iconify()
        
        #_______________LOGIN_SCREEN_________________
        top=Toplevel(win)
        top.geometry('524x224+200+100')
        top.title('LOGIN SCREEN')
        p=PhotoImage(file='emiImages//logo7.png')
        top.iconphoto(False,p)
        image1=ImageTk.PhotoImage(Image.open("emiImages//login3.jpg"))
        labl=Label(top,image=image1)
        labl.pack()
        top.configure(background="turquoise")
        lbl1=Label(top,text="Username",font=("Helvetica",15,"bold"))
        lbl1.config(background="sea green")
        entry1=Entry(top)
        lbl2=Label(top,text="Password",font=("Helvetica",15,"bold"))
        lbl2.config(background="cornflower blue")
        entry2=Entry(top,show="*")

        def valid():
            uname=entry1.get()
            #print(uname)
            try:
                db=MySQLdb.connect('localhost','root','root','emiloancalculator')
                cursor=db.cursor()
                sql="select User_ID,Password,User_Type from user where Username = %s"
                cursor.execute(sql,(uname,))
                #print(res)
                uid,pas,ut=cursor.fetchone()
                #print(pas,ut)
                
            except Exception as e:
                print(e)
                messagebox.showerror("Error","Invalid Credentials!")
            finally:
                db.close()
            if pas==entry2.get():
                win.deiconify()
                top.destroy()
                if ut=="administrator":
                    Admin(win,uid)
                elif ut=="employee":
                    Employ(win,uid)
            else:
                messagebox.showerror("Error","Invalid Password")

        def comm1():
            top.destroy()
            win.destroy()
            sys.exit()

        def comm2():
            entry1.delete(0,"end")
            entry2.delete(0,"end")

        btn0=tk.Button(top,text="Sign In",bg="lime green",activebackground="cyan",font=("Verdana",10,"bold"),command=valid)
        btn1=tk.Button(top,text="Cancel",bg="lime green",activebackground="cyan",font=("Verdana",10,"bold"),command=comm1)
        btn2=tk.Button(top,text="Reset",bg="lime green",activebackground="cyan",font=("Verdana",10,"bold"),command=comm2)
        image=ImageTk.PhotoImage(Image.open("emiImages//loan_2.jpg"))
        lbl=Label(top,image=image)
        lbl.config(background="black",borderwidth=4,relief="ridge")
        
        lbl1.place(x=30,y=40)
        entry1.place(x=140,y=43)
        lbl2.place(x=30,y=100)
        entry2.place(x=140,y=103)
        btn0.place(x=110,y=160)
        btn1.place(x=197,y=160)
        btn2.place(x=32,y=160)
        lbl.place(x=285,y=30)
        top.mainloop()

    splash.after(500,main_win)
mainloop()
   