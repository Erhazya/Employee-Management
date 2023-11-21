import mysql.connector 
import logs

try:
    config = {
        'user': 'admin',
        'password': 'Azertyuiop$1',
        'host': '109.89.241.235',
        'port': '3306',
        'database': 'Employes_Informations',
        'raise_on_warnings': True
    }

    conn = mysql.connector.connect(**config)

    cursor = conn.cursor()
except mysql.connector.Error as err:
    logs.logging.error('Employes Informations : Erreur de connexion à la base de données : ' + format(err) + str(config))


def add_employes(id=100000, name="test", firstname="test", phone="2323233", address="add", diplome=0, salary=122):
    """
    Ajoute un employé à la base de données.

    Args:
        id (int): L'ID de l'employé (par défaut: 100000).
        name (str): Le nom de l'employé (par défaut: "test").
        firstname (str): Le prénom de l'employé (par défaut: "test").
        phone (str): Le numéro de téléphone de l'employé (par défaut: "2323233").
        address (str): L'adresse de l'employé (par défaut: "add").
        diplome (int): Le niveau de diplôme de l'employé (par défaut: 0).
        salary (int): Le salaire de l'employé (par défaut: 122).
    """

    query = "INSERT INTO employes (id, name, firstname, phone, address, diplome, salary) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (id, name, firstname, phone, address, diplome, salary)
    
    cursor.execute(query, values)
    result = cursor.fetchone()
    conn.commit()


def del_employes(id):
    """
    Supprime un employé de la base de données.

    Args:
        id (int): L'ID de l'employé à supprimer.
    """
    
    query = "DELETE FROM employes WHERE id = %s"
    values = (id)
    
    cursor.execute(query, values)
    conn.commit()
    


def list_employes():
    """
    Récupère la liste des employés dans la base de données.

    Returns:
        list: Une liste contenant les informations de tous les employés.
    """
    
    query = "SELECT * FROM employes ORDER BY name"
    cursor.execute(query)
    result = cursor.fetchall()
    return result



def update_employes(name, firstname, phone, address, diplome, salary, id):
    """
    Met à jour les informations d'un employé dans la base de données.

    Args:
        name (str): Le nouveau nom de l'employé.
        firstname (str): Le nouveau prénom de l'employé.
        phone (str): Le nouveau numéro de téléphone de l'employé.
        address (str): La nouvelle adresse de l'employé.
        diplome (int): Le nouveau niveau de diplôme de l'employé.
        salary (int): Le nouveau salaire de l'employé.
        id (int): L'ID de l'employé à mettre à jour.
    """
    
    query = "UPDATE employes SET name = %s, firstname = %s, phone = %s, address = %s, diplome = %s, salary = %s WHERE id = %s "
    cursor.execute(query, (name, firstname, phone, address, diplome, salary, id))
    conn.commit()
