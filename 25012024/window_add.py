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

from showList import *
import datetime
import mysql.connector
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox 

bdd = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='PyDo'
)
mycursor = bdd.cursor()

# AJOUT D'UNE NOUVELLE TACHE : --------------------------------------------------------------------------------------------------------------
    # Initialisation des variables :
val_new_tache_nom = ""
val_new_tache_deadline = ""
val_new_tache_etat = ""
        # date du jour = date de création, format YYYY-MM-DD
val_new_tache_date_creation = datetime.date.today()
val_new_tache_date_creation = val_new_tache_date_creation.strftime("%Y-%m-%d")

    # Fonction de redirection vers l'ajout :
def redirection_ajout():
        # On crée une nouvelle fenêtre avec la classe Tk :
    fenetre_ajout = Tk()
        # On crée un titre à notre fenêtre :
    fenetre_ajout.title("PyDo - Ajout d'une nouvelle tâche")
        # On règle la dimension de la fenêtre à 500x500px :
    fenetre_ajout.geometry("250x200")
    # Fonction d'ajout d'une nouvelle tâche :
    def add_new_tache():
            # Récupération des données saisies dans les champs et attribution aux variables :
        val_new_tache_nom = new_tache_nom.get()
        val_new_tache_deadline = new_tache_deadline.get()
            # Conversion de l'état : str > int :
        if (listeAffich.get() == "À faire") :
            val_new_tache_etat = "2"
        elif (listeAffich.get() == "En cours") :
            val_new_tache_etat = "1"
        else :
            val_new_tache_etat = "0"
            # Insertion des valeurs dans la table 'taches' :
                # Requête SQL :
                    # On vérifie bien que tous les champs soient bien remplis pour envoyer la requête, sinon on affiche une pop-up d'erreur :
        if val_new_tache_nom == "" or val_new_tache_deadline == "" :
            messagebox.showwarning("", "Tous les champs ne sont pas remplis ! Veuillez réessayer.")
            add_new_tache        
        elif val_new_tache_deadline < val_new_tache_date_creation :
            messagebox.showwarning("", "La date de fin prévue ne peut pas être inférieure à la date du jour ! Veuillez réessayer.")
            add_new_tache
        else :
            mycursor.execute("INSERT INTO taches (Nom, Creation, Deadline, Etat) VALUES (%s,%s,%s,%s)",(val_new_tache_nom,val_new_tache_date_creation,val_new_tache_deadline,val_new_tache_etat))
                    # Envoi et clôture :
            bdd.commit()
            showList()
            fenetre_ajout.destroy()    
    # Côté interface :
        # Label nom :
    label_new_tache_nom = ttk.Label(fenetre_ajout, text='Nom de la nouvelle tâche :')
    label_new_tache_nom.grid(column=0, row=0)
        # Champ nom :
    new_tache_nom = ttk.Entry(fenetre_ajout)
    new_tache_nom.grid(column=0, row=1)

        # Label deadline :
    label_new_tache_deadline = ttk.Label(fenetre_ajout, text='Date de fin prévue (YYYY-MM-DD):')
    label_new_tache_deadline.grid(column=0, row=2)
        # Champ deadline :
    new_tache_deadline = ttk.Entry(fenetre_ajout)
    new_tache_deadline.grid(column=0, row=3)

        # Label état :
    label_new_tache_etat = ttk.Label(fenetre_ajout, text='État :')
            # Différents états possibles de la liste déroulante :
    liste_etat = ["À faire","En cours","Finie"]
            # Attribution de la classe Combobox à la liste :
    listeAffich = ttk.Combobox(fenetre_ajout, values=liste_etat)
            # Valeur par défaut de la liste :
    listeAffich.current(0)
            # Affichage du label :
    label_new_tache_etat.grid(column=0, row=4)
        # Champ état :
    new_tache_etat = ttk.Entry(fenetre_ajout)
    listeAffich.grid(column=0, row=5)
        # Bouton de validation de l'envoi de la nouvelle tâche avec éxecution de la fonction d'envoi à la BDD :
    btn_add_new_tache = ttk.Button(fenetre_ajout, text="Ajouter à la To Do List", command=add_new_tache)
    btn_add_new_tache.grid(column=0, row=6)
