import tkinter as tk
from tkinter import ttk
import employes_informations
import ui_manager




def main():

    
    




    def on_select(event):
        # Get the selected item from the Listbox
            selection = tree.selection()
            if selection:
                item_value = tree.item(selection)
                employee_info = item_value['values']

                # Clear the fields

                # Set the values in the Entry fields
                entry_id.delete(0, tk.END)
                entry_id.insert(tk.END, employee_info[0])

                entry_last_name.delete(0, tk.END)
                entry_last_name.insert(tk.END, employee_info[1])

                entry_name.delete(0, tk.END)
                entry_name.insert(tk.END, employee_info[2])

                entry_telephone.delete(0, tk.END)
                entry_telephone.insert(tk.END, employee_info[3])

                entry_address.delete(0, tk.END)
                entry_address.insert(tk.END, employee_info[4])

                entry_diploma.delete(0, tk.END)
                if employee_info[5] == 1 :
                    status_diplome = "Diplômé"
                else :
                    status_diplome = "Pas de diplôme"
                entry_diploma.insert(tk.END, status_diplome)

                entry_salary.delete(0, tk.END)
                entry_salary.insert(tk.END, str(employee_info[6]))



    def reload_employee_list():

        tree.delete(*tree.get_children())


        list_em = employes_informations.list_employes()

        for employes in list_em :
            tree.insert("", "end", values=(employes[0], employes[1], employes[2], employes[3], employes[4], employes[5], employes[6]))


    def clear_entry():
        entry_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_last_name.delete(0, tk.END)
        entry_telephone.delete(0, tk.END)
        entry_address.delete(0, tk.END)
        entry_diploma.delete(0, tk.END)
        entry_salary.delete(0, tk.END)

    def add_employee():
        # Get employee information from the entry fields
        employee_id = entry_id.get()
        name = entry_name.get()
        last_name = entry_last_name.get()
        telephone = entry_telephone.get()
        address = entry_address.get()
        diploma = entry_diploma.get()
        salary = entry_salary.get()

        employes_informations.add_employes(employee_id, name, last_name, telephone, address, diploma, salary)

        # Insert the employee data into the treeview
        tree.insert("", "end", values=(employee_id, name, last_name, telephone, address, diploma, salary))

        # Clear the entry fields after adding the employee
        clear_entry()

        reload_employee_list()

    def delete_employee():
        # Get the selected employee from the treeview
        selected_item = tree.selection()
        if selected_item:
            item_value = tree.item(selected_item)
            employee_info = item_value['values']
            employes_informations.del_employes([employee_info[0]])
            tree.delete(selected_item)
        
        
        reload_employee_list()

        

    def update_employee():
        employee_id = entry_id.get()
        name = entry_name.get()
        last_name = entry_last_name.get()
        telephone = entry_telephone.get()
        address = entry_address.get()
        diploma = entry_diploma.get()
        if diploma == "Diplomé":
            diploma = 1
        else :
            diploma = 0
        salary = entry_salary.get()

        employes_informations.update_employes(name,last_name,telephone,address,diploma,salary,employee_id)
        reload_employee_list()
    
    # Create the main window
    window = tk.Tk()
    window.title("Employee Management")
    window.geometry("800x600")

    # Create a frame for the employee input fields
    input_frame = tk.Frame(window)
    input_frame.pack(pady=20)

    # Employee ID
    label_id = tk.Label(input_frame, text="ID:")
    label_id.grid(row=0, column=0, padx=5, sticky="w")
    entry_id = tk.Entry(input_frame)
    entry_id.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    # Employee Name
    label_name = tk.Label(input_frame, text="Nom:")
    label_name.grid(row=1, column=0, padx=5, sticky="w")
    entry_name = tk.Entry(input_frame)
    entry_name.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    # Employee Last Name
    label_last_name = tk.Label(input_frame, text="Prénom:")
    label_last_name.grid(row=2, column=0, padx=5, sticky="w")
    entry_last_name = tk.Entry(input_frame)
    entry_last_name.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    # Employee Telephone
    label_telephone = tk.Label(input_frame, text="Téléphone:")
    label_telephone.grid(row=3, column=0, padx=5, sticky="w")
    entry_telephone = tk.Entry(input_frame)
    entry_telephone.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    # Employee Address
    label_address = tk.Label(input_frame, text="Adresse:")
    label_address.grid(row=4, column=0, padx=5, sticky="w")
    entry_address = tk.Entry(input_frame)
    entry_address.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    # Employee Diploma
    label_diploma = tk.Label(input_frame, text="Diplôme:")
    label_diploma.grid(row=5, column=0, padx=5, sticky="w")
    entry_diploma = tk.Entry(input_frame)
    entry_diploma.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    # Employee Salary
    label_salary = tk.Label(input_frame, text="Salaire:")
    label_salary.grid(row=6, column=0, padx=5, sticky="w")
    entry_salary = tk.Entry(input_frame)
    entry_salary.grid(row=6, column=1, padx=5, pady=5, sticky="w")

    # Create a frame for the buttons
    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    # Add Employee Button
    button_add = tk.Button(button_frame, text="Ajouter Employé", command=add_employee)
    button_add.grid(row=0, column=0, padx=5)

    # Update Employee Button
    button_update = tk.Button(button_frame, text="Mettre à jour Employé",command=update_employee)
    button_update.grid(row=0, column=1, padx=5)

    # Delete Employee Button
    button_delete = tk.Button(button_frame, text="Supprimer Employé", command=delete_employee)
    button_delete.grid(row=0, column=2, padx=5)

    # Create a treeview to display the employee information
    tree_frame = tk.Frame(window)
    tree_frame.pack(pady=20)


    tree = ttk.Treeview(tree_frame, columns=("ID", "Nom", "Prénom", "Téléphone", "Adresse", "Diplôme", "Salaire"), show="headings")
    tree.column("ID", width=50)
    tree.column("Nom", width=100)
    tree.column("Prénom", width=100)
    tree.column("Téléphone", width=100)
    tree.column("Adresse", width=150)
    tree.column("Diplôme", width=100)
    tree.column("Salaire", width=100)
    tree.heading("ID", text="ID")
    tree.heading("Nom", text="Nom")
    tree.heading("Prénom", text="Prénom")
    tree.heading("Téléphone", text="Téléphone")
    tree.heading("Adresse", text="Adresse")
    tree.heading("Diplôme", text="Diplôme")
    tree.heading("Salaire", text="Salaire")
    tree.pack()

    tree.bind('<<TreeviewSelect>>', on_select)


    reload_employee_list()



    



    # Run the main window loop
    window.mainloop()




