# Configuration de la liaison entre Python et la BDD
import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
  'database': 'test',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='PyDo'
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")
    # La ligne suivante permet de voir si la liaison fonctionne bien, la boucle doit nous retourner la liste des tables de la BDD
for x in mycursor:
    print(x)


# La fenêtre avec tkinter :
    # On importe le module
from tkinter import * 
    # On crée une fenêtre avec la classe Tk :
fenetre = Tk()
    # On crée un titre à notre fenêtre :
fenetre.title("PyDo - To Do List")
    # On règle la dimension de la fenêtre à 500x500px :
fenetre.geometry("500x500")
    # On ajoute une icône :
fenetre.iconbitmap('/Users/gualtierijessica/Desktop/Documents/MNS/CDA/Projets GAMORY/PyDo/15012023/icone.ico')
    # On affiche notre fenêtre :
fenetre.mainloop()