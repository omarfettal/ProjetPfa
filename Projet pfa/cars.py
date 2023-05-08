from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import pymysql
import tkinter as tk
import tkinter.ttk as ttk


def recherche():

    voitures = tk.Toplevel(cars)
    voitures.geometry("300x300")
    voitures.title('RECHERCHE')

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

    xscrollbar = ttk.Scrollbar(voitures, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=xscrollbar.set)
    xscrollbar.pack(side="bottom", fill="x")

    con= pymysql.connect(host='localhost',user='root',passwd='omarfettal10',database='cars')
    mycursor=con.cursor()
    search_query=search_entry.get()
    tree.delete(*tree.get_children())
#marque
 
    query = f"SELECT * FROM voitures WHERE marque LIKE '%{search_query}%'"
    mycursor.execute(query)
    resultat1= mycursor.fetchall()
    
    for row in resultat1:
        tree.insert("", "end",text=row[0],values=row[1:9])
       
#type carburant
    query = f"SELECT * FROM voitures WHERE type_carburant LIKE '%{search_query}%'"
    mycursor.execute(query)
    resultat1= mycursor.fetchall()
    
    for row in resultat1:
        tree.insert("", "end",text=row[0],values=row[1:9])

# nombres de places
    query = f"SELECT * FROM voitures WHERE nombres_de_places LIKE '%{search_query}%'"
    mycursor.execute(query)
    resultat1= mycursor.fetchall()
    
    for row in resultat1:
        tree.insert("", "end",text=row[0],values=row[1:9])

#transmission
   

    query = f"SELECT * FROM voitures WHERE transmission LIKE '%{search_query}%'"
    mycursor.execute(query)
    resultat1= mycursor.fetchall()
    
    for row in resultat1:
        tree.insert("", "end",text=row[0],values=row[1:9])

#prix par jour
    if search_query.isdigit():
       query = f"SELECT * FROM voitures WHERE prix_par_jour='{search_query}'"    
    else : 
       query = f"SELECT * FROM voitures WHERE prix_par_jour='{search_query}'"
    mycursor.execute(query)
    resultat1= mycursor.fetchall()
    
    for row in resultat1:
        tree.insert("", "end",text=row[0],values=row[1:9])        










    voitures.geometry("500x500")


    tree.pack()
    tree.configure(height=24)

      
    voitures.mainloop()            





def show_dacia():
  

    voitures = tk.Toplevel(cars)
    voitures.geometry("300x300")
    voitures.title('DACIA')

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



    xscrollbar = ttk.Scrollbar(voitures, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=xscrollbar.set)
    xscrollbar.pack(side="bottom", fill="x")



    con= pymysql.connect(host='localhost',user='root',passwd='omarfettal10',database='cars')
    mycursor=con.cursor()
    query="SELECT * FROM voitures WHERE marque='dacia'"
    mycursor.execute(query)
    resultat1=mycursor.fetchall()

    for row in resultat1:
        tree.insert("", "end",text=row[0],values=row[1:9]) 


    voitures.geometry("500x500")


    tree.pack()
    tree.configure(height=24)

      
    voitures.mainloop()


def show_renault():
  

    voitures = tk.Toplevel(cars)
    voitures.geometry("300x300")
    voitures.title('RENAULT')

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



    xscrollbar = ttk.Scrollbar(voitures, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=xscrollbar.set)
    xscrollbar.pack(side="bottom", fill="x")



    con= pymysql.connect(host='localhost',user='root',passwd='omarfettal10',database='cars')
    mycursor=con.cursor()
    query="SELECT * FROM voitures WHERE marque='renault'"
    mycursor.execute(query)
    resultat1=mycursor.fetchall()

    for row in resultat1:
        tree.insert("", "end",text=row[0],values=row[1:9]) 


    voitures.geometry("500x500")


    tree.pack()
    tree.configure(height=24)

      
    voitures.mainloop()



def show_ford():
  

    voitures = tk.Toplevel(cars)
    voitures.geometry("300x300")
    voitures.title('FORD')

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



    xscrollbar = ttk.Scrollbar(voitures, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=xscrollbar.set)
    xscrollbar.pack(side="bottom", fill="x")



    con= pymysql.connect(host='localhost',user='root',passwd='omarfettal10',database='cars')
    mycursor=con.cursor()
    query="SELECT * FROM voitures WHERE marque='ford'"
    mycursor.execute(query)
    resultat1=mycursor.fetchall()

    for row in resultat1:
        tree.insert("", "end",text=row[0],values=row[1:9]) 


    voitures.geometry("500x500")


    tree.pack()
    tree.configure(height=24)

      
    voitures.mainloop()


def show_landrover():
  

    voitures = tk.Toplevel(cars)
    voitures.geometry("300x300")
    voitures.title('LAND ROVER')

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



    xscrollbar = ttk.Scrollbar(voitures, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=xscrollbar.set)
    xscrollbar.pack(side="bottom", fill="x")



    con= pymysql.connect(host='localhost',user='root',passwd='omarfettal10',database='cars')
    mycursor=con.cursor()
    query="SELECT * FROM voitures WHERE marque='landrover'"
    mycursor.execute(query)
    resultat1=mycursor.fetchall()

    for row in resultat1:
        tree.insert("", "end",text=row[0],values=row[1:9]) 


    voitures.geometry("500x500")


    tree.pack()
    tree.configure(height=24)

      
    voitures.mainloop()



def show_bmw():
  

    voitures = tk.Toplevel(cars)
    voitures.geometry("300x300")
    voitures.title('BMW')

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



    xscrollbar = ttk.Scrollbar(voitures, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=xscrollbar.set)
    xscrollbar.pack(side="bottom", fill="x")



    con= pymysql.connect(host='localhost',user='root',passwd='omarfettal10',database='cars')
    mycursor=con.cursor()
    query="SELECT * FROM voitures WHERE marque='bmw'"
    mycursor.execute(query)
    resultat1=mycursor.fetchall()

    for row in resultat1:
        tree.insert("", "end",text=row[0],values=row[1:9]) 


    voitures.geometry("500x500")


    tree.pack()
    tree.configure(height=24)

      
    voitures.mainloop()



def show_mercedes():
  

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



    xscrollbar = ttk.Scrollbar(voitures, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=xscrollbar.set)
    xscrollbar.pack(side="bottom", fill="x")



    con= pymysql.connect(host='localhost',user='root',passwd='omarfettal10',database='cars')
    mycursor=con.cursor()
    query="SELECT * FROM voitures WHERE marque='mercedes'"
    mycursor.execute(query)
    resultat1=mycursor.fetchall()

    for row in resultat1:
        tree.insert("", "end",text=row[0],values=row[1:9]) 


    voitures.geometry("500x500")


    tree.pack()
    tree.configure(height=24)

      
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
bmwbutton=Button(cars,image=img1_obj,cursor='hand2',command=show_bmw)
bmwbutton.place(x=450,y=150)

#land rover button
img2=Image.open('logorange.jpg')
resized_img2=img2.resize((120,120),Image.ANTIALIAS)
img2_obj=ImageTk.PhotoImage(resized_img2)
rangebutton=Button(cars,image=img2_obj,cursor='hand2',command=show_landrover)
rangebutton.place(x=670,y=150)

#ford button
img3=Image.open('logoford.jpg')
resized_img3=img3.resize((120,120),Image.ANTIALIAS)
img3_obj=ImageTk.PhotoImage(resized_img3)
rangebutton=Button(cars,image=img3_obj,cursor='hand2',command=show_ford)
rangebutton.place(x=230,y=400)

#renault button
img4=Image.open('logorenault.jpg')
resized_img4=img4.resize((120,120),Image.ANTIALIAS)
img4_obj=ImageTk.PhotoImage(resized_img4)
rangebutton=Button(cars,image=img4_obj,cursor='hand2',command=show_renault)
rangebutton.place(x=450,y=400)

#dacia button
img5=Image.open('logodacia.jpg')
resized_img5=img5.resize((120,120),Image.ANTIALIAS)
img5_obj=ImageTk.PhotoImage(resized_img5)
rangebutton=Button(cars,image=img5_obj,cursor='hand2',command=show_dacia)
rangebutton.place(x=670,y=400)

#search button

search_entry = tk.Entry(cars)
search_entry.place(x=90,y=0)
search_button = tk.Button(cars, text="Rechercher",command=recherche)
search_button.place(x=200,y=0)


cars.mainloop()
