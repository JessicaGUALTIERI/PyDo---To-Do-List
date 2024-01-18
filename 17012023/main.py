import datetime
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


# RÉGLAGE DE LA FENÊTRE AVEC TKINTER : ------------------------------------------------------------------------------------------------------
    # On crée une fenêtre avec la classe Tk :
fenetre_main = Tk()
    # On crée un titre à notre fenêtre :
fenetre_main.title("PyDo - To Do List")
    # On règle la dimension de la fenêtre à 500x500px :
fenetre_main.geometry("500x500")


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
    fenetre_ajout.geometry("500x500")
    # Fonction d'ajout d'une nouvelle tâche :
    def add_new_tache():
            # Récupération des données saisies dans les champs et attribution aux variables :
        val_new_tache_nom = new_tache_nom.get()
        val_new_tache_deadline = new_tache_deadline.get()
        print(val_new_tache_date_creation)
            # Conversion de l'état : str > int :
        if (listeAffich.get() == "A faire") :
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
            bdd.close()
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
    


# # AFFICHAGE DE LA TODOLIST : ----------------------------------------------------------------------------------------------------------------
#     # Label titre :
# label_todolist= ttk.Label(fenetre_main, text='ToDoList actuelle :')
# label_todolist.grid(column=0, row=7)

#     #Label tâches :
# label_todolist_nom= ttk.Label(fenetre_main, text='Tâches :')
# label_todolist_nom.grid(column=0, row=8)
#     # Requête SQL de sélection des noms des tâches :
# mycursor.execute("SELECT Nom FROM taches WHERE Etat=1 OR Etat=2")
#     # Affichage des résultats de la requête :
# i=0 
# for taches in mycursor: 
#     for j in range(len(taches)):
#         e = Entry(fenetre_main) 
#         e.grid(row=9+i, column=0) 
#         e.insert(END, taches[j])
#     i=i+1

#     # Label deadline :
# label_todolist_deadline= ttk.Label(fenetre_main, text='A faire avant le :')
# label_todolist_deadline.grid(column=1, row=8)
#     # Requête SQL de sélection des deadline des tâches :
# mycursor.execute("SELECT Deadline FROM taches WHERE Etat=1 OR Etat=2")
#     # Affichage des résultats de la requête :
# i=0 
# for dates in mycursor: 
#     for j in range(len(dates)):
#         e = Entry(fenetre_main) 
#         e.grid(row=9+i, column=1)
#         dateDMY = dates[j]
#         e.insert(END, dateDMY.strftime('%d-%m-%Y'))
#     i=i+1


# AJOUT DES BOUTONS DE REDIRECTION SUR LA FENÊTRE MAIN : ------------------------------------------------------------------------------------------------------
btn_redirection_ajout = ttk.Button(fenetre_main, text="Ajouter une tâche", command=redirection_ajout)
btn_redirection_ajout.grid(column=0, row=0)

# AFFICHAGE DE LA FENÊTRE : -----------------------------------------------------------------------------------------------------------------
fenetre_main.mainloop()