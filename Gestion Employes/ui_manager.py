import tkinter as tk
import employes_informations
import ui_add_del_emloyes




def main():

    def sort_listbox():
        elements = list(listbox.get(0, tk.END))  # Récupérer tous les éléments actuels
        elements.sort()  # Trier les éléments dans l'ordre alphabétique
        listbox.delete(0, tk.END)  # Supprimer tous les éléments du Listbox

        for element in elements:
            listbox.insert(tk.END, element)  # Réinsérer les éléments triés dans le Listbox

    
    def on_select(event):
        
        
        liste_em = employes_informations.list_employes()
        selection = listbox.curselection()
        if selection:
            index = selection[0]
            employee = liste_em[index]

            # Clear the fields
            clear_fields()

            # Set the values in the Entry fields
            id_entry.configure(state="normal")
            id_entry.delete(0, tk.END)
            id_entry.insert(tk.END, employee[0])
            id_entry.configure(state="readonly")

            nom_entry.configure(state="normal")
            nom_entry.delete(0, tk.END)
            nom_entry.insert(tk.END, employee[1])
            nom_entry.configure(state="readonly")

            prenom_entry.configure(state="normal")
            prenom_entry.delete(0, tk.END)
            prenom_entry.insert(tk.END, employee[2])
            prenom_entry.configure(state="readonly")

            telephone_entry.configure(state="normal")
            telephone_entry.delete(0, tk.END)
            telephone_entry.insert(tk.END, employee[3])
            telephone_entry.configure(state="readonly")

            adresse_entry.configure(state="normal")
            adresse_entry.delete(0, tk.END)
            adresse_entry.insert(tk.END, employee[4])
            adresse_entry.configure(state="readonly")

            diplome_entry.configure(state="normal")
            diplome_entry.delete(0, tk.END)
            if employee[5] == 1 :
                status_diplome = "Diplômé"
            else :
                status_diplome = "Pas de diplôme"
            diplome_entry.insert(tk.END, status_diplome)
            diplome_entry.configure(state="readonly")

            salaire_entry.configure(state="normal")
            salaire_entry.delete(0, tk.END)
            salaire_entry.insert(tk.END, str(employee[6])+ " €")
            salaire_entry.configure(state="readonly")
            sort_listbox()

    def clear_fields():
        # Clear the Entry fields
        id_entry.delete(0, tk.END)
        nom_entry.delete(0, tk.END)
        prenom_entry.delete(0, tk.END)
        telephone_entry.delete(0, tk.END)
        adresse_entry.delete(0, tk.END)
        diplome_entry.delete(0, tk.END)
        salaire_entry.delete(0, tk.END)


    def configure_entry(entry):
        entry.configure(highlightthickness=0)
        entry.configure(justify='left')
        entry.configure(background="#f0f0f0",font=("Arial",15),borderwidth=0, justify='left')
        entry.configure(width=50)




    window = tk.Tk()
    window.title("Employee Management")
    window.geometry("1200x800")
    window.configure(background="#f0f0f0")

    title_label = tk.Label(window, text="Liste d'employés", font=("Arial", 20))

    title_label.grid(row=0, column=0)

    listbox = tk.Listbox(window, width=30, height=25, borderwidth=2)
    listbox.grid(row=1, column=0)

    listbox.configure(font=('Arial', 17))
    listbox.configure(fg='black', background='#f0f0f0')
    listbox.configure(state="normal")

    liste_em = employes_informations.list_employes()
    listbox.delete('0', 'end')

    for employes in liste_em:
        listbox.insert(tk.END, employes[1:3])

    listbox.bind('<<ListboxSelect>>', on_select)

    # Create Entry fields for employee information
    id_label = tk.Label(window, text="ID:",background="#f0f0f0",font=("Arial",15))
    id_label.grid(row=1, column=1, sticky=tk.N)
    id_entry = tk.Entry(window)
    id_entry.grid(row=1, column=2, sticky=tk.N)
    configure_entry(id_entry)


    nom_label = tk.Label(window, text="Nom de Famille:",background="#f0f0f0",font=("Arial",15))
    nom_label.grid(row=1, column=1, sticky=tk.N,pady=50)
    nom_entry = tk.Entry(window)
    nom_entry.grid(row=1, column=2,sticky=tk.N,pady=50)
    configure_entry(nom_entry)

    prenom_label = tk.Label(window, text="Prénom:",background="#f0f0f0",font=("Arial",15))
    prenom_label.grid(row=1, column=1,sticky=tk.N,pady=100)
    prenom_entry = tk.Entry(window)
    prenom_entry.grid(row=1, column=2,sticky=tk.N,pady=100)
    configure_entry(prenom_entry)



    telephone_label = tk.Label(window, text="Téléphone:",background="#f0f0f0",font=("Arial",15))
    telephone_label.grid(row=1, column=1,sticky=tk.N,pady=150)
    telephone_entry = tk.Entry(window)
    telephone_entry.grid(row=1, column=2,sticky=tk.N,pady=150)
    configure_entry(telephone_entry)


    adresse_label = tk.Label(window, text="Adresse:",background="#f0f0f0",font=("Arial",15))
    adresse_label.grid(row=1, column=1,sticky=tk.N,pady=200)
    adresse_entry = tk.Entry(window)
    adresse_entry.grid(row=1, column=2,sticky=tk.N,pady=200,columnspan=3)
    configure_entry(adresse_entry)


    diplome_label = tk.Label(window, text="Diplôme:",background="#f0f0f0",font=("Arial",15))
    diplome_label.grid(row=1, column=1,sticky=tk.N,pady=250)
    diplome_entry = tk.Entry(window)
    diplome_entry.grid(row=1, column=2,sticky=tk.N,pady=250)
    configure_entry(diplome_entry)


    salaire_label = tk.Label(window, text="Salaire:",background="#f0f0f0",font=("Arial",15))
    salaire_label.grid(row=1, column=1,sticky=tk.N,pady=300)
    salaire_entry = tk.Entry(window)
    salaire_entry.grid(row=1, column=2,sticky=tk.N,pady=300)
    configure_entry(salaire_entry)



    # Ajouter un bouton "Modifier les employés"
    update_button = tk.Button(window, text="Modifier les employés", command=ui_add_del_emloyes.main, font=("Arial", 15), width=20)
    update_button.grid(row=2, column=0, pady=10)