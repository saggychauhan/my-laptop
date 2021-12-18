from tkinter import messagebox as msg
from tkinter import *
import mysql.connector 

class resume(Frame):
   


    def __init__(self,m):
        super().__init__(m)
        #self.con=mysql.connector.connect(db='db1', user='root', passwd='root', host='localhost')
        #self.cursor=self.con.cursor()
        self.menubar=Menu(self)

        self.filemenu=Menu(self.menubar,tearoff=0)
        self.editmenu=Menu(self.menubar,tearoff=0)
        self.helpmenu=Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label='New')
        self.filemenu.add_command(label='Open')
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit')
        self.menubar.add_cascade(label='File',
        underline=0,menu=self.filemenu)
        self.editmenu.add_command(label='Cut')
        self.editmenu.add_command(label='Copy')
        self.editmenu.add_separator()
        self.editmenu.add_command(label='Paste')
        self.menubar.add_cascade(label='Edit',
        underline=1,menu=self.editmenu)
        self.helpmenu.add_command(label='FAQs')
        self.helpmenu.add_command(label='Info')
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label='Contact Us')
        self.menubar.add_cascade(label='Help',
        underline=1,menu=self.helpmenu)
        
        #self.posts = ("Junior Engineer", "Senior Engineer", "Software Developer", "Manager")
        self.fullname=StringVar()
        self.mobile=StringVar()
        self.mail=StringVar()
        self.address=StringVar()
        self.qualification=StringVar()
        self.DOB=StringVar()
        self.post=StringVar()
        self.gender = StringVar(value='none')
        self.decleared = IntVar(value=0)

        self.l1=Label(self, text="Full Name" , fg='yellow' , bg='red' , font=('Times New Roman' ,14))
        self.t1=Entry(self, textvariable=self.fullname, fg='yellow' ,bg='red' , font=('Times New Roman' ,12))
        self.l2=Label(self, text="Mobile No." , fg='yellow' , bg='red' , font=('Times New Roman' ,14))
        self.t2=Entry(self, textvariable=self.mobile ,fg='yellow' ,bg='red' , font=('Times New Roman' ,12))
        self.l3=Label(self,  text="Mail ID" , fg='yellow' , bg='red' , font=('Times New Roman' ,14))
        self.t3=Entry(self, textvariable=self.mail , fg='yellow' ,bg='red' , font=('Times New Roman' ,12))
        self.l4=Label(self, text="Address" , fg='yellow' , bg='red' , font=('Times New Roman' ,14))
        self.t4=Entry(self, textvariable=self.address , fg='yellow' ,bg='red' , font=('Times New Roman' ,12))
        self.l5=Label(self, text="Qualification" , fg='yellow' , bg='red' , font=('Times New Roman' ,14))
        self.t5=Entry(self, textvariable=self.qualification , fg='yellow' ,bg='red' , font=('Times New Roman' ,12))
        self.l6=Label(self, text="D.O.B" , fg='yellow' , bg='red' , font=('Times New Roman' ,14))
        self.t6=Entry(self, textvariable=self.DOB , fg='yellow' ,bg='red' , font=('Times New Roman' ,12))
        self.l7=Label(self, text="Applying for" , fg='yellow' , bg='red' , font=('Times New Roman' ,14))
        self.t7=Entry(self, textvariable=self.post , fg='yellow' ,bg='red' , font=('Times New Roman' ,12))

        self.r1=Radiobutton(self, text="Male" , variable=self.gender,value='male')
        self.r2=Radiobutton(self, text="Female" , variable=self.gender,value='female' )

        self.ch1=Checkbutton(self, text="Self Declaration" , font=('Times New Roman' ,14) , variable=self.decleared, onvalue=1, offvalue=0) 
        
        self.b1=Button(self, text = "Submit", fg='yellow' ,bg='red' , font=('Times New Roman' ,14), bd=6 , justify="center" , command=self.show)

        self.l1.grid(row=0 , column=0)
        self.t1.grid(row=0 , column=1)
        self.l2.grid(row=1 , column=0)
        self.t2.grid(row=1 , column=1)
        self.l3.grid(row=2 , column=0)
        self.t3.grid(row=2 , column=1)
        self.l3.grid(row=3 , column=0)
        self.t3.grid(row=3 , column=1)
        self.l4.grid(row=4 , column=0)
        self.t4.grid(row=4 , column=1)
        self.l5.grid(row=5 , column=0)
        self.t5.grid(row=5 , column=1)
        self.l6.grid(row=6 , column=0)
        self.t6.grid(row=6 , column=1)
        self.l7.grid(row=7 , column=0)
        self.t7.grid(row=7 , column=1)
        self.r1.grid(row=8 , column=0)
        self.r2.grid(row=8 , column=1)
        self.ch1.grid(row=9 , column=1)
        self.b1.grid(row=10 , column=1)

        self.rowconfigure(index=0 , pad=10)
        self.rowconfigure(index=1 , pad=10)
        self.rowconfigure(index=2 , pad=10)
        self.rowconfigure(index=3 , pad=10)
        self.rowconfigure(index=4 , pad=10)
        self.rowconfigure(index=5 , pad=10)
        self.rowconfigure(index=6 , pad=10)
        self.rowconfigure(index=7 , pad=10)

        self.pack()
        
    def show(self):
        fullname= self.fullname.get()
        mobile = self.mobile.get()
        mail = self.mail.get()
        address = self.address.get()
        education = self.qualification.get()
        DOB = self.DOB.get()
        post = self.post.get()
        gender = self.gender.get()[0].upper()
        print(fullname, mobile, mail, address, education, DOB, post, gender)
        
        #self.cursor.execute("insert into application values (%s,%s,%s,%s,%s,%s,%s,%s)")

        # uname=self.t1.get()
        # role=self.t7.get()
        # gender=self.c2.get()
        # if self.c1.get():
        #     msg.showinfo('Greeting' , 'Thanks ' +uname+"\n Your application for " +role+ " has been submitted !! ")
        # else:
        #     msg.showerror('Error', 'Not agreed with the above information provided by you')

root=Tk()
ob=resume(root)
root.title('Job Application')
root.geometry('550x450')
root.config(menu=ob.menubar)
root.mainloop()

