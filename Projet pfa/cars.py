from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql
import tkinter as tk
import tkinter.ttk as ttk





conn= pymysql.connect(host="localhost", user="root", password="omarfettal10", database="cars")
cursor =conn.cursor()



def show_voitures():
  

    voitures = tk.Toplevel(cars)
    voitures.geometry("300x300")
    voitures.title('MERCEDES')

    # treeview
    tree = ttk.Treeview(voitures, columns=("Marque", "Modèle", "Image","Type Carburant","Nombre de places","Transmission","Prix par jour","Disponibilité"))

    tree.heading("#0", text="ID")
    tree.heading("Marque", text="Marque")
    tree.heading("Modèle", text="Modèle")
    tree.heading("Image", text="Image")
    tree.heading("Type Carburant", text="Type Carburant")
    tree.heading("Nombre de places", text="Nombre de places")
    tree.heading("Transmission", text="Transmission")
    tree.heading("Prix par jour", text="Prix par jour")
    tree.heading("Disponibilité", text="Disponibilité")

    con= pymysql.connect(host='localhost',user='root',passwd='omarfettal10',database='cars')
    mycursor=con.cursor()
    query='SELECT * from mercedes'
    mycursor.execute(query)
    rows=mycursor.fetchall()
    for row in rows:
        tree.insert("",END,text=row[0],values=row[1:])

    xscrollbar = ttk.Scrollbar(voitures, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=xscrollbar.set)
    xscrollbar.pack(side="bottom", fill="x")

    voitures.geometry("500x500")



   

    tree.pack()

      

    voitures.mainloop()



#GUI part

cars=Tk()
cars.resizable(0,0)
cars.geometry("1000x750")
cars.title('Voitures')

bgImage=ImageTk.PhotoImage(file='parking.jpeg')
bgLabel=Label(cars,image=bgImage)
bgLabel.pack()

#mercedes button
img=Image.open('logomercedes.jpg')
resized_img=img.resize((120,120),Image.ANTIALIAS)
img_obj=ImageTk.PhotoImage(resized_img)
mercedesbutton=Button(cars,image=img_obj,command=show_mercedes,cursor='hand2')
mercedesbutton.place(x=230,y=150)

#bmw button
img1=Image.open('logobmw.jpg')
resized_img1=img1.resize((120,120),Image.ANTIALIAS)
img1_obj=ImageTk.PhotoImage(resized_img1)
bmwbutton=Button(cars,image=img1_obj,command=show_bmw,cursor='hand2')
bmwbutton.place(x=450,y=150)

#land rover button
img2=Image.open('logorange.jpg')
resized_img2=img2.resize((120,120),Image.ANTIALIAS)
img2_obj=ImageTk.PhotoImage(resized_img2)
rangebutton=Button(cars,image=img2_obj,command=show_landrover,cursor='hand2')
rangebutton.place(x=670,y=150)

#ford button
img3=Image.open('logoford.jpg')
resized_img3=img3.resize((120,120),Image.ANTIALIAS)
img3_obj=ImageTk.PhotoImage(resized_img3)
rangebutton=Button(cars,image=img3_obj,command=show_ford,cursor='hand2')
rangebutton.place(x=230,y=400)

#renault button
img4=Image.open('logorenault.jpg')
resized_img4=img4.resize((120,120),Image.ANTIALIAS)
img4_obj=ImageTk.PhotoImage(resized_img4)
rangebutton=Button(cars,image=img4_obj,command=show_renault,cursor='hand2')
rangebutton.place(x=450,y=400)

#dacia button
img5=Image.open('logodacia.jpg')
resized_img5=img5.resize((120,120),Image.ANTIALIAS)
img5_obj=ImageTk.PhotoImage(resized_img5)
rangebutton=Button(cars,image=img5_obj,command=show_dacia,cursor='hand2')
rangebutton.place(x=670,y=400)

#search button

search_entry = tk.Entry(cars)
search_entry.place(x=90,y=0)
search_button = tk.Button(cars, text="Rechercher",command=search)
search_button.place(x=200,y=0)


cars.mainloop()