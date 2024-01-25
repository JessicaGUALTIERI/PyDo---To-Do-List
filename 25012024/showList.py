#############################################################################################################################################
#                                                                                                                                           #
#                                         ########    #     #   #####         ###                                                           #
#                                         #       #    #   #    #     #     #     #                                                         #
#                                         #       #     # #     #      #   #       #                                                        #
#                                         #######        #      #      #   #       #                                                        #
#                                         #              #      #      #   #       #                                                        #
#                                         #              #      #     #     #     #                                                         #
#                                         #              #      #####         ###                                                           #
#                                                                                                                                           #
#############################################################################################################################################
#       
#       Date : 25/01/2024
#
#       Bugs connus :
#               * Possibilité d'ajouter une seule tâche par session, la deuxième réouvre bien une fenêtre mais n'envoie par la requête SQL
#               * Aucune réactualisation de la liste sur l'écran de base
#
#       Bugs restants :
#               *
#
#############################################################################################################################################

import mysql.connector
from tkinter import * 
from tkinter import ttk

bdd = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='PyDo'
)
mycursor = bdd.cursor()
# RÉGLAGE DE LA FENÊTRE AVEC TKINTER : ------------------------------------------------------------------------------------------------------
    # On crée une fenêtre avec la classe Tk :
fenetre_main = Tk()
    # On crée un titre à notre fenêtre :
fenetre_main.title("PyDo - To Do List")
    # On règle la dimension de la fenêtre à 500x500px :
fenetre_main.geometry("600x400")

def showList():
    # AFFICHAGE DE LA TODOLIST : ----------------------------------------------------------------------------------------------------------------
        # Label titre :
    label_todolist= ttk.Label(fenetre_main, text='ToDoList actuelle :')
    label_todolist.grid(column=1, row=7)

        #Label tâches :
    label_todolist_nom= ttk.Label(fenetre_main, text='Tâches :')
    label_todolist_nom.grid(column=0, row=8)
        # Requête SQL de sélection des noms des tâches :
    mycursor.execute("SELECT Nom FROM taches WHERE Etat=1 OR Etat=2")
        # Affichage des résultats de la requête :
    iLignes = 0
    for tache in mycursor :
        for j in range(len(tache)):
            e = Entry(fenetre_main) 
            e.grid(row=9+iLignes, column=0) 
            e.insert(END, tache[j])
            iLignes = iLignes + 1


        # Label deadline :
    label_todolist_deadline= ttk.Label(fenetre_main, text='A faire avant le :')
    label_todolist_deadline.grid(column=1, row=8)
        # Requête SQL de sélection des deadline des tâches :
    mycursor.execute("SELECT Deadline FROM taches WHERE Etat=1 OR Etat=2")
        # Affichage des résultats de la requête :
    iLignes = 0 
    for dates in mycursor: 
        for j in range(len(dates)):
            e = Entry(fenetre_main) 
            e.grid(row=9+iLignes, column=1)
            dateDMY = dates[j]
            e.insert(END, dateDMY.strftime('%d-%m-%Y'))
        iLignes = iLignes + 1

        # Label état :
    label_todolist_etat= ttk.Label(fenetre_main, text='Etat actuel :')
    label_todolist_etat.grid(column=2, row=8)
        # Requête SQL de sélection des deadline des tâches :
    mycursor.execute("SELECT Etat FROM taches WHERE Etat=1 OR Etat=2")
        # Affichage des résultats de la requête :
    iLignes = 0 
    for etat in mycursor :
        for j in range(len(etat)):
            e = Entry(fenetre_main) 
            e.grid(row=9+iLignes, column=2) 
            if (etat[j] == 2) :
                e.insert(END, "À faire")
            else :
                e.insert(END, "En cours")
        iLignes = iLignes + 1
    