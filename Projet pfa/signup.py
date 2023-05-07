from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql



#Functionality part
def clear():
   emailEntry.delete(0,END)
   usernameEntry.delete(0,END)
   passwordEntry.delete(0,END)
   confirmpasswordEntry.delete(0,END)
   check.set(0)
   signup_window.destroy()
   import login 



def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmpasswordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Error','Password Missmatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept Terms & Conditions')
    else:
      try:  
        con=pymysql.connect(host='localhost',user='root',password='omarfettal10')
        mycursor=con.cursor()        
      except:
         messagebox.showerror('Error','Database Connectivity Issue, Please try again')
         return
      
      
      try:
        query='create database userdata'
        mycursor.execute(query)
        query='use userdata'
        mycursor.execute(query)
        query='create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))'
        mycursor.execute(query)

      except:
        mycursor.execute('use userdata')
        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))
        row=mycursor.fetchone()


        if row !=None:
           messagebox.showerror('Error','Username Already exists')
        else:
              
          query='insert into data (email,username,password) values(%s,%s,%s)'
          mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
          con.commit()
          con.close()
          messagebox.showinfo('Succes','Registration is Successful')
          clear()



def login_page():
    signup_window.destroy()
    import login    

#GUI part
signup_window=Tk()
signup_window.resizable(0,0)
signup_window.title('Signup page')

bg1Image=ImageTk.PhotoImage(file='bg1.jpg')
bg1Label=Label(signup_window,image=bg1Image)
bg1Label.pack()

heading=Label(signup_window,text='CREATE AN ACCOUNT',font=('Arial Greek',23,'bold'),fg='black')
heading.place(x=110,y=0)

#email label
emailLabel=Label(text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='black',fg='white')
emailLabel.place(x=120,y=90)

emailEntry=Entry(signup_window,width=20,font=('Arial Greek',23,'bold'),fg='black') 
emailEntry.place(x=120,y=110)

#username label
usernameLabel=Label(text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='black',fg='white')
usernameLabel.place(x=120,y=170)
usernameEntry=Entry(signup_window,width=20,font=('Arial Greek',23,'bold'),fg='black') 
usernameEntry.place(x=120,y=190)

#password label
passwordLabel=Label(text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='black',fg='white')
passwordLabel.place(x=120,y=250)
passwordEntry=Entry(signup_window,width=20,font=('Arial Greek',23,'bold'),fg='black') 
passwordEntry.place(x=120,y=270)

#confirm password label

confirmpasswordLabel=Label(text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='black',fg='white')
confirmpasswordLabel.place(x=120,y=330)

confirmpasswordEntry=Entry(signup_window,width=20,font=('Arial Greek',23,'bold'),fg='black') 
confirmpasswordEntry.place(x=120,y=350)

#check button
check=IntVar()
ternsandconditions=Checkbutton(text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light',10,'bold'),cursor='hand2',
                               variable=check)
ternsandconditions.place(x=120,y=410)

#signup button

signupButton=Button(signup_window,text='Sign Up',font=('Open Sans',10,'bold'),fg='white',bg='grey13',cursor='hand2',bd=0,width=50,height=3,
                    command=connect_database)
signupButton.place(x=100,y=480)

#login button

loginButton=Button(signup_window,text='Log in',font=('Open Sans',9,'bold underline'),fg='white',bg='black',cursor='hand2',bd=0,
                   command=login_page)
loginButton.place(x=285,y=580)






    










signup_window.mainloop()