from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import traceback

#Functionality part

def forget_pass():
  def change_password():
   if usernameEnter.get()=='' or passwordEnter.get()=='' or confirmpasswordEnter.get()=='':
    messagebox.showerror('Error','All Fields Are Required',parent=window)
   elif passwordEnter.get()!=confirmpasswordEnter.get():
    messagebox.showerror('Error','Password and confirm password are not matching',parent=window)
   else:
    con=pymysql.connect(host='localhost',user='root',passwd='omarfettal10',database='userdata')
    mycursor=con.cursor()
    query='select * from data where username=%s'
    mycursor.execute(query,(usernameEnter.get()))
    row=mycursor.fetchone()
    if row==None:
       messagebox.showerror('Error','Incorrect username',parent=window)
    else:
       query='update data set password=%s where username=%s'
       mycursor.execute(query,(confirmpasswordEnter.get(),usernameEnter.get()))
       con.commit()
       con.close()
       messagebox.showinfo('Succes','Password resset,Login again',parent=window)
       window.destroy()   
 
  window=Toplevel()
  window.resizable(0,0)
  window.title('Resset Password')

  bg3=ImageTk.PhotoImage(file='bg3.jpg')
  bg3Label=Label(window,image=bg3)
  bg3Label.pack()
  
  heading_Label=Label(window,text='Resset Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='darkkhaki',fg='black')
  heading_Label.place(x=110,y=0)
 
  #username label
  usernameLabel=Label(window,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='darkkhaki',fg='black')
  usernameLabel.place(x=120,y=170)
  usernameEnter=Entry(window,width=20,font=('Arial Greek',23,'bold'), fg='black') 
  usernameEnter.place(x=120,y=190)
 
  #password label
  passwordLabel=Label(window,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='darkkhaki',fg='black')
  passwordLabel.place(x=120,y=250)
  passwordEnter=Entry(window,width=20,font=('Arial Greek',23,'bold'),fg='black') 
  passwordEnter.place(x=120,y=270)
 
  #confirmpassword label
  confirmpasswordLabel=Label(window,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='darkkhaki',fg='black')
  confirmpasswordLabel.place(x=120,y=330)
  confirmpasswordEnter=Entry(window,width=20,font=('Arial Greek',23,'bold'),fg='black') 
  confirmpasswordEnter.place(x=120,y=350)
 
  #submit button
  submitButton=Button(window,text='SUBMIT',font=('Open Sans',10,'bold'),fg='black',bg='white',cursor='hand2',bd=0,width=50,height=3,command=change_password)
  submitButton.place(x=90,y=480)
 
 
  window.mainloop()


   
  
       

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    else: 

      try: 
       con=pymysql.connect(host='localhost',user='root',passwd='omarfettal10') 
       mycursor=con.cursor()
       query='use userdata'
       mycursor.execute(query)
       query='select * from data where username=%s and password=%s'
       mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
       row=mycursor.fetchone()
       if row==None:
        messagebox.showerror('Error','Invalude username or password')
       else:
        messagebox.showinfo('Welcome','Login is successful')
        login_window.destroy()
        import cars 
      except:
        messagebox.showerror('Error','Connection Is Not Estabilished Try again')
        traceback.print_exc()
        return
      
    
   


def hide():
    openeye.config(file='closeeye.png')
    passwordEntry.config(show='*')
    eyebutton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyebutton.config(command=hide)


def user_enter(event):
    if usernameEntry.get()=='Username':
       usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
       passwordEntry.delete(0,END)

def signup_window():
    login_window.destroy()
    import signup




#GUI part
login_window=Tk()
login_window.resizable(0,0)
login_window.title('Login page')



bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(login_window,image=bgImage)
bgLabel.pack()



heading=Label(login_window,text='USER LOGIN',font=('Arial Greek',23,'bold'),fg='grey38')
heading.place(x=200,y=0)

 #username Entry
usernameEntry=Entry(login_window,width=25,font=('Arial Greek',23,'bold'),fg='grey38') 
usernameEntry.place(x=80,y=150)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)


#password entry
passwordEntry=Entry(login_window,width=25,font=('Arial Greek',23,'bold'),fg='grey38') 
passwordEntry.place(x=80,y=250)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',password_enter)



 #eye button
openeye=PhotoImage(file='openeye.png') 
eyebutton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyebutton.place(x=480,y=255)


 #forget button
forgetbutton=Button(login_window,text='Forgot password ?',bd=0,bg='white',activebackground='white',cursor='hand2'
                    ,font=('Calibri',9,'bold'),command=forget_pass)
forgetbutton.place(x=410,y=295)

#login button
loginButton=Button(login_window,text='Login',font=('Open Sans',10,'bold'),fg='black',bg='white',cursor='hand2',bd=0,width=50,height=3,
                   command=login_user)
loginButton.place(x=90,y=390)


#signup

signupLabel=Label(login_window,text='Dont have an account ?',font=('Open Sans',9,'bold'),fg='white',bg='black')
signupLabel.place(x=220,y=590)

#newaccount button

newaccountButton=Button(login_window,text='Create new one',font=('Open Sans',9,'bold underline'),fg='white',bg='black',cursor='hand2',bd=0,
                        command=signup_window)
newaccountButton.place(x=240,y=620)



login_window.mainloop()