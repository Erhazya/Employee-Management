import tkinter as tk
import user_connections
import ui_manager


def connect_callback(username, password):
    """Fonction de rappel pour la connexion à la base de données."""
    status = user_connections.connect(username, password)

    return status

def clear_error_text():
    """Efface le champ de texte d'erreur."""
    error_text.delete("1.0", tk.END)

def connect_and_clear():
    """Fonction appelée lors du clic sur le bouton 'Se connecter'."""
    clear_error_text()
    result = connect_callback(username_entry.get(), password_entry.get())
    print(result)
    if not result:
        error_text.insert(tk.END, "Erreur de connexion.")
    else:
        fenetre.destroy()
        ui_manager.main()
        
        
        


# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Gestion des employés")
fenetre.geometry("300x250")

# Etiquette pour le titre
titre_label = tk.Label(fenetre, text="Gestion des employés", font=("Helvetica", 16))
titre_label.pack(pady=10)

# Cadre pour le formulaire de connexion
ajout_cadre = tk.Frame(fenetre)
ajout_cadre.pack(pady=10)

# Etiquettes et des champs de saisie pour le formulaire de connexion
username_label = tk.Label(ajout_cadre, text="Nom d'utilisateur :")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(ajout_cadre)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(ajout_cadre, text="Mot de passe :")
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(ajout_cadre)
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Champ de texte pour l'affichage des erreurs
error_text = tk.Text(fenetre, height=2, width=30, bg=fenetre.cget("bg"), bd=0, font=("Helvetica", 10), wrap=tk.WORD)
error_text.pack()

# Bouton se connecter
connect_button = tk.Button(fenetre, text="Se connecter", command=lambda: connect_and_clear())
connect_button.pack(pady=10)

fenetre.mainloop()
