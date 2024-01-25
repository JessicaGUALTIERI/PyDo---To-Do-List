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
#               1. Possibilité d'ajouter une seule tâche par session, la deuxième réouvre bien une fenêtre mais n'envoie par la requête SQL
#               2. Aucune réactualisation de la liste sur l'écran de base
#
#       Corrections :
#               1. Retrait de la ligne 'bdd.close()' dans window_add.py qui empêchait le renouvellement des requêtes SQL
#
#       Bugs restants :
#               * Aucune réactualisation de la liste sur l'écran de base
#
#############################################################################################################################################

from window_add import *
from showList import *
import mysql.connector
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox 


# CONFIGURATION DE LA LIAISON AVEC LA BDD : -------------------------------------------------------------------------------------------------
bdd = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='PyDo'
)
mycursor = bdd.cursor()




# AJOUT DES BOUTONS DE REDIRECTION SUR LA FENÊTRE MAIN : ------------------------------------------------------------------------------------------------------
btn_redirection_ajout = Button(fenetre_main, text="Ajouter une tâche", command=redirection_ajout)
btn_redirection_ajout.grid(column=0, row=0)
btn_quitter = Button(fenetre_main, text="Quitter", command=fenetre_main.destroy)
btn_quitter.grid(column=2, row=0)

mycursor.execute("SELECT COUNT(*) AS total FROM taches")
countList = mycursor.fetchone()
if (countList[0] > 0) :
    showList()


# AFFICHAGE DE LA FENÊTRE : -----------------------------------------------------------------------------------------------------------------
fenetre_main.mainloop()